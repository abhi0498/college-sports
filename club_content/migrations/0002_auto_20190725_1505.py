# Generated by Django 2.2.3 on 2019-07-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images_for_club',
            name='image_field',
            field=models.ImageField(upload_to='image'),
        ),
    ]
