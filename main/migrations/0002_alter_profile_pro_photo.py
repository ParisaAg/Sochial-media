# Generated by Django 5.0.1 on 2024-01-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pro_photo',
            field=models.ImageField(default='blank-mages.png', upload_to='profilephotos'),
        ),
    ]
