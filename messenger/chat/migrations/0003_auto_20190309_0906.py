# Generated by Django 2.1.7 on 2019-03-09 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_usercolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercolor',
            name='color',
            field=models.CharField(default='#00000', max_length=30),
        ),
    ]