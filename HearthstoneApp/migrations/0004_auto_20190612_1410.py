# Generated by Django 2.2.2 on 2019-06-12 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HearthstoneApp', '0003_auto_20190612_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteshearthstone',
            name='couleur',
            field=models.CharField(choices=[('', ''), ('green', 'Green'), ('red', 'Red'), ('black', 'Black'), ('white', 'White'), ('blue', 'Blue')], default='', max_length=20),
        ),
    ]
