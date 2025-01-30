from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client,Project
from django.contrib.auth.models import User
from .serializer import ClientSerializer, UserSerializer,ProjectSerializer

# Create your views here.


#api to add users
@api_view(['POST', 'GET'])
def user_api(request):
    try:
        print(f'=== HTTP method: {request.method} ===')
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        elif request.method == 'GET':
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
    except Exception as e:
        print('Error', e)




#api to CRUD clients
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def client_api(request, id=None):
    try:
        print('===function start========')
        print(f'=== HTTP method: {request.method} ===')
        if request.method == 'POST':
            client_name = request.data.get('client_name')
            client = Client.objects.create(
                client_name=client_name,
                created_by=request.user.username 
            )
            serializer = ClientSerializer(client)
            return Response(serializer.data)

        elif request.method == 'GET':
            if id:
                client = Client.objects.get(id=id)
                projects = Project.objects.filter(client=client)

                project_data = []
                for project in projects:
                    project_data.append({
                        "id": project.id,
                        "name": project.project_name,
                    })

                response_data = {
                    "id": client.id,
                    "client_name": client.client_name,
                    "projects": project_data,
                    "created_at": client.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                    "created_by": client.created_by,
                    "updated_at": client.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                }

                return Response(response_data)

            else:
                clients = Client.objects.all()
                serializer = ClientSerializer(clients, many=True)
                return Response(serializer.data)

        elif request.method in ['PUT', 'PATCH']:
            client = Client.objects.get(id=id)
            print('client', client)
            if request.method == 'PUT':
                serializer = ClientSerializer(client, data=request.data)
            elif request.method == 'PATCH':
                serializer = ClientSerializer(client, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                print(f"validation failed: {serializer.errors}")

        elif request.method == 'DELETE':
            client = Client.objects.get(id=id)
            client.delete()
            return Response(status=204)

    except Exception as e:
        print('Error', e)


# api for Project Entity
@api_view(['GET', 'POST'])
def project_api(request):
    try:
        print(f'=== HTTP method: {request.method} ===')
        if request.method == 'POST':
            project_name = request.data.get("project_name")
            client_id = request.data.get("client_id")
            user_id = request.data.get("users", [])
            print('---------',project_name,client_id,user_id)

            client = Client.objects.filter(id=client_id).first()
            users = User.objects.filter(id__in=user_id)

            print('===client====',client,users)

            project = Project.objects.create(
                project_name=project_name,
                client=client,
                created_by=request.user.username  
            )
            project.users.set(users)

            response_data = {
                "id": project.id,
                "project_name": project.project_name,
                "client": client.client_name,  
                "users": [{"id": user.id, "name": user.username} for user in users], 
                "created_at": project.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                "created_by": project.created_by
            }

            return Response(response_data)

        elif request.method == 'GET':
            user = request.user

            projects = Project.objects.filter(users=user)

            response_data = []
            for project in projects:
                response_data.append({
                    "id": project.id,
                    "project_name": project.project_name,
                    "client_name": project.client.client_name, 
                    "created_at": project.created_at,
                    "created_by": project.created_by
                })

            return Response(response_data)

    except Exception as e:
        print('Error', e)

