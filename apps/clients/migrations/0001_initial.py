# Generated by Django 3.2.8 on 2021-10-21 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('fecha', models.DateField(verbose_name='fecha')),
                ('cedula', models.IntegerField(verbose_name='cedula')),
                ('casado', models.BooleanField(verbose_name='casado')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='ClienteProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.cliente', verbose_name='cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producto', verbose_name='producto')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='producto',
            field=models.ManyToManyField(through='clients.ClienteProducto', to='products.Producto'),
        ),
    ]