# Generated by Django 3.1.3 on 2020-11-18 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='sponsors',
            field=models.ManyToManyField(through='shelter.Animal_sponsor', to='shelter.Sponsor', verbose_name='Apadrinamientos'),
        ),
    ]