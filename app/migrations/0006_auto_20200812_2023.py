# Generated by Django 2.2 on 2020-08-13 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200812_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='bagid',
            field=models.CharField(default='default_id', max_length=30),
        ),
        migrations.AlterField(
            model_name='bag',
            name='end',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='bag',
            name='start',
            field=models.CharField(default='0', max_length=30),
        ),

    ]