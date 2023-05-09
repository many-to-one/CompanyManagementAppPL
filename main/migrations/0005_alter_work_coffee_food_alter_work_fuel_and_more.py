# Generated by Django 4.2.1 on 2023-05-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_work_coffee_food_alter_work_fuel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='coffee_food',
            field=models.FloatField(default=0.0, null=True, verbose_name='Kawa/Posiłki'),
        ),
        migrations.AlterField(
            model_name='work',
            name='fuel',
            field=models.FloatField(default=0.0, null=True, verbose_name='Paliwo'),
        ),
        migrations.AlterField(
            model_name='work',
            name='phone_costs',
            field=models.FloatField(default=0.0, null=True, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='work',
            name='prepayment',
            field=models.FloatField(default=0.0, null=True, verbose_name='Zaliczka'),
        ),
    ]