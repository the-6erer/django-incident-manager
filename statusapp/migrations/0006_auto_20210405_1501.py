# Generated by Django 3.1.7 on 2021-04-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statusapp', '0005_notificationlist_all_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationlist',
            name='all_topic',
            field=models.BooleanField(default=False, help_text='If selected, unselect single topics above', verbose_name='All topics'),
        ),
    ]
