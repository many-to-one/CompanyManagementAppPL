# Generated by Django 4.2.1 on 2023-06-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_alter_vacations_days_to_use_in_current_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacations',
            name='days_planned',
            field=models.IntegerField(max_length=2, null=True, verbose_name='Zaplanowany urlop'),
        ),
        migrations.AlterField(
            model_name='vacations',
            name='days_to_use_in_current_year',
            field=models.IntegerField(max_length=2, null=True, verbose_name='Do użycia w bieżącym roku'),
        ),
        migrations.AlterField(
            model_name='vacations',
            name='days_to_use_in_last_year',
            field=models.IntegerField(max_length=2, null=True, verbose_name='Do użycia w poprzednim roku'),
        ),
        migrations.AlterField(
            model_name='vacations',
            name='days_used_in_current_year',
            field=models.IntegerField(max_length=2, null=True, verbose_name='Użyto w bieżącym roku'),
        ),
        migrations.AlterField(
            model_name='vacations',
            name='days_used_in_last_year',
            field=models.IntegerField(max_length=2, null=True, verbose_name='Użyto w poprzednim roku'),
        ),
    ]
