# Generated by Django 2.0.3 on 2018-06-02 07:57

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedAnt', '0023_post_postnum'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='名称')),
                ('Content', DjangoUeditor.models.UEditorField(verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='名称')),
                ('Content', DjangoUeditor.models.UEditorField(verbose_name='内容')),
            ],
        ),
    ]