# Generated by Django 4.2.4 on 2023-08-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0006_remove_regionandmulticultural_like_users_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionandmulticultural',
            name='already_like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='regionandmulticultural',
            name='like',
            field=models.TextField(default='좋아요'),
        ),
    ]
