# Generated by Django 4.2.1 on 2023-05-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_work_coffee_food_alter_work_fuel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='over_time',
            field=models.CharField(default='00:00', max_length=5, null=True, verbose_name='Nadgodziny'),
        ),
    ]