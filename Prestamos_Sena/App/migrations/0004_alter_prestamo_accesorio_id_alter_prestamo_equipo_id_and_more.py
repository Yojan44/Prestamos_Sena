# Generated by Django 4.2.3 on 2023-09-23 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_prestamo_accesorio_id_alter_prestamo_equipo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='accesorio_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.accesorio'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='equipo_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.equipo'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateTimeField(null=True),
        ),
    ]
