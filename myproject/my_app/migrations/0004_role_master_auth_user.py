# Generated by Django 4.1.4 on 2022-12-19 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0003_user_details_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='role_master',
            name='auth_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role_auth_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
