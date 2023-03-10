# Generated by Django 4.1.3 on 2023-03-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsController',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='名字')),
                ('created_tm', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_tm', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('remark', models.TextField(blank=True, default='', null=True, verbose_name='备注')),
                ('project_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='定制化或者主线')),
                ('products_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='产品名称')),
                ('products_install_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='部署类型')),
                ('t_remake', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注2')),
                ('m_remake', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注3')),
                ('p_remake', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注4')),
            ],
            options={
                'db_table': 'projects_controller',
                'ordering': ['-id'],
                'unique_together': {('name',)},
            },
        ),
    ]
