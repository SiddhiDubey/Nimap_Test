from django.contrib import admin
from .models import Client, Project

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','client_name', 'created_at','updated_at', 'created_by')
    search_fields = ('id','client_name',)
    list_filter = ('id','created_at', 'updated_at','created_by')

admin.site.register(Client, ClientAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','project_name','client', 'created_at', 'created_by')
    search_fields = ('id','project_name',)
    list_filter = ('id','project_name','client','created_at','created_by')

admin.site.register(Project, ProjectAdmin)