# Generated by Django 5.1.5 on 2025-01-29 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0002_client_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
