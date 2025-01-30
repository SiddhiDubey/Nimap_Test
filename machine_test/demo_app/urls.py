from django.urls import path
from .views import *


urlpatterns = [
    
    path(r'user_api/', user_api, name='user_api'),
    path(r'client_api/', client_api, name='client_api'),
    path(r'client_api/<int:id>/', client_api, name='client_api'), 
    path('project_api/', project_api, name='project_api'),



]