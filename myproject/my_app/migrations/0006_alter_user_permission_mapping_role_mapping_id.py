# Generated by Django 4.1.4 on 2022-12-20 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_user_permission_mapping_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_permission_mapping',
            name='role_mapping_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_permission_role_id', to='my_app.role_master'),
        ),
    ]
