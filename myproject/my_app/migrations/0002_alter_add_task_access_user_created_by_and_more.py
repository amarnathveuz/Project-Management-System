# Generated by Django 4.1.4 on 2022-12-15 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_task_access_user',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='add_task_access_user',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='add_task_attachment',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='add_task_attachment',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='add_task_checklist',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='add_task_checklist',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='add_task_comments',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='add_task_comments',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='add_task_master',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='add_task_master',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company_master',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company_master',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='role_mapping',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='role_mapping',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='role_master',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='role_master',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='space_access_permission_user',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='space_access_permission_user',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='space_master',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='space_master',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sub_space_access_permission',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sub_space_access_permission',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sub_space_master',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sub_space_master',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_active_account',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_active_account',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_permission_mapping',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_permission_mapping',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
    ]
