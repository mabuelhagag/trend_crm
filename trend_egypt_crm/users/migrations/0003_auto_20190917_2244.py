# Generated by Django 2.2.4 on 2019-09-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190917_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.FloatField(blank=True, verbose_name='Balance'),
        ),
    ]
