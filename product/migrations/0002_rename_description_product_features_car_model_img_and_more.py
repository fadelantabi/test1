# Generated by Django 4.2.19 on 2025-05-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='features',
        ),
        migrations.AddField(
            model_name='car_model',
            name='img',
            field=models.ImageField(max_length=500, null=True, upload_to='imgs/car_model'),
        ),
        migrations.AddField(
            model_name='color',
            name='blue_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='color',
            name='green_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='color',
            name='red_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='engine',
            field=models.IntegerField(null=True),
        ),
    ]
