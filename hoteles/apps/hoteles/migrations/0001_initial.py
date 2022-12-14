# Generated by Django 4.1.1 on 2022-09-23 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text=' (1 - 5) estrellas', max_length=50, verbose_name='(Que Nivel)')),
            ],
            options={
                'verbose_name': 'tipo categoria',
                'verbose_name_plural': 'tipo categorias',
            },
        ),
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Suites, Dobles, Individuales', max_length=50, verbose_name='(Escoja una de las 3)')),
            ],
            options={
                'verbose_name': 'tipo habitacion',
                'verbose_name_plural': 'tipo habitaciones',
            },
        ),
        migrations.CreateModel(
            name='Hoteles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreHoteles', models.CharField(help_text='Ingrese el Nombre del Hotel', max_length=100)),
                ('direccionHoteles', models.CharField(help_text='Ingrese la Direccion del Hotel', max_length=100)),
                ('telefonoHoteles', models.CharField(help_text='Ingrese el Telefono del Hotel', max_length=12)),
                ('añodeconstruccionHoteles', models.CharField(help_text='Ingrese el año de construcion del Hotel', max_length=100)),
                ('tipocategoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hoteles.categoria')),
                ('tipohabitacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hoteles.tipohabitacion')),
            ],
            options={
                'verbose_name': 'hotel',
                'verbose_name_plural': 'hoteles',
            },
        ),
    ]
