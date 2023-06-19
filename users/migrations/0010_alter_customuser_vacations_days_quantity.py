# Generated by Django 4.2.1 on 2023-06-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_customuser_vacations_days_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='vacations_days_quantity',
            field=models.IntegerField(max_length=2, null=True, verbose_name='Ilość przysługujących dni urlopu'),
        ),
    ]
