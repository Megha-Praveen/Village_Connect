# Generated by Django 5.0.3 on 2024-04-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village_website', '0005_alter_posts_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='mobilenumber',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visitors',
            name='mobilenumber',
            field=models.IntegerField(),
        ),
    ]
