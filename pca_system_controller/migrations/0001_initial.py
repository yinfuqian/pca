# Generated by Django 4.1.3 on 2023-02-15 17:42

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PcaSshUserController',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('created_tm', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_tm', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
                ('password', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='SSH 密码')),
            ],
            options={
                'db_table': 'pca_ssh_user_controller',
                'ordering': ['-id'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='PcaUserController',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(help_text='用户名', primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='用户名', max_length=200, unique=True)),
                ('phone', models.CharField(max_length=11, null=True, unique=True, verbose_name='手机号')),
                ('password', models.SlugField(help_text='用户密码', max_length=128)),
                ('role', models.CharField(choices=[('dev-adm', '超级管理员'), ('dev-manage', '运维'), ('dev-devlop', '普通用户'), ('dev-pm', 'PM'), ('dev-tm', 'TM')], default='dev-manage', max_length=32)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '系统用户',
                'verbose_name_plural': '系统用户',
                'db_table': 'pca_user_controller',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
