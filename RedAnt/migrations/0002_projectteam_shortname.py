# Generated by Django 2.0.3 on 2018-04-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedAnt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectteam',
            name='ShortName',
            field=models.CharField(max_length=20, null=True),
        ),
    ]