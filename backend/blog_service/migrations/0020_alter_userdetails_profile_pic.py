# Generated by Django 4.0.3 on 2022-04-23 09:37

import blog_service.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_service', '0019_alter_userdetails_user_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='profile_pic',
            field=models.ImageField(default='images/default.png', upload_to=blog_service.models.path_to_rename),
        ),
    ]
