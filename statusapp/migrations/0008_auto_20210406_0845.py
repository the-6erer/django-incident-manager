# Generated by Django 3.1.7 on 2021-04-06 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statusapp', '0007_auto_20210405_1547'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='notification',
            unique_together={('notification', 'address')},
        ),
    ]
