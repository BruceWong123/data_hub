# Generated by Django 2.2 on 2020-08-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200812_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='end',
            field=models.CharField(default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='bag',
            name='start',
            field=models.CharField(default='0', max_length=25),
        ),
    ]
