# Generated by Django 5.0.3 on 2024-04-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village_website', '0002_posts_visitors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
