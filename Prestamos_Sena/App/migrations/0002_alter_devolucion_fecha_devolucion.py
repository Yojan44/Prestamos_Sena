# Generated by Django 4.2.4 on 2023-09-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucion',
            name='fecha_devolucion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
