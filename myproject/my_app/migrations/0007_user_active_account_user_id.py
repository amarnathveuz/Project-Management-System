# Generated by Django 4.1.4 on 2022-12-20 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_alter_user_permission_mapping_role_mapping_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_active_account',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='login_user_active_userid', to='my_app.user_details'),
        ),
    ]