# Generated by Django 4.0.4 on 2022-05-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='image',
            field=models.FileField(default=None, upload_to='static/links/img/', verbose_name='Превью'),
        ),
    ]
