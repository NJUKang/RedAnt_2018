# Generated by Django 2.0.3 on 2018-07-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedAnt', '0033_projectteam_outoftime'),
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=100)),
                ('Content', models.CharField(max_length=100)),
                ('Time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='projectteam',
            name='OutofTime',
            field=models.BooleanField(default=False, verbose_name='过期'),
        ),
    ]