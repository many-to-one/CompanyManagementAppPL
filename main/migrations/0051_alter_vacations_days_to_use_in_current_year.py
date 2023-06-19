# Generated by Django 4.2.1 on 2023-06-13 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0050_remove_vacations_days_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacations',
            name='days_to_use_in_current_year',
            field=models.ForeignKey(max_length=2, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Do użycia w bieżącym roku'),
        ),
    ]
