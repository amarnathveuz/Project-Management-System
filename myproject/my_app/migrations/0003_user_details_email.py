# Generated by Django 4.1.4 on 2022-12-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_add_task_access_user_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
