# Generated by Django 2.0.3 on 2018-04-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedAnt', '0015_remove_blog_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='shortname',
            field=models.CharField(default=True, max_length=100),
        ),
    ]