# Generated by Django 5.0.6 on 2024-05-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_avatar_alter_customuser_vk_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='vk_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
