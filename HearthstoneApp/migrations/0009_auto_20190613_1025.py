# Generated by Django 2.2.2 on 2019-06-13 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HearthstoneApp', '0008_auto_20190612_1532'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Auteur',
        ),
    ]