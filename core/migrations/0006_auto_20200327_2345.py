# Generated by Django 2.2.2 on 2020-03-28 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200327_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_sub_one',
            field=models.ImageField(default='default.png', upload_to='', verbose_name='Sub Image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_sub_three',
            field=models.ImageField(default='default.png', upload_to='', verbose_name='Sub Image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_sub_two',
            field=models.ImageField(default='default.png', upload_to='', verbose_name='Sub Image'),
        ),
    ]