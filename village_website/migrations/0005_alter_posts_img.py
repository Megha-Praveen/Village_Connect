# Generated by Django 5.0.3 on 2024-04-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village_website', '0004_alter_posts_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]