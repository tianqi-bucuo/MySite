# Generated by Django 2.1.4 on 2019-12-06 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190810_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='ug',
        ),
        migrations.DeleteModel(
            name='UserGroup',
        ),
    ]
