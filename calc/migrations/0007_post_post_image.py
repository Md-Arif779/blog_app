# Generated by Django 4.2.3 on 2023-07-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
