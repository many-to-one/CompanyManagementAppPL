# Generated by Django 4.2.1 on 2023-05-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_totalworkobject_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='workobject',
            name='coffee_food',
            field=models.CharField(default=0.0, max_length=100, null=True, verbose_name='Kawa/Posiłki'),
        ),
    ]