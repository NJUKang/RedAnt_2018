# Generated by Django 2.0.3 on 2018-05-31 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedAnt', '0022_auto_20180531_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postNum',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]