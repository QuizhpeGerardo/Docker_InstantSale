# Generated by Django 4.0.5 on 2022-08-02 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Esqueleto', '0005_publicacionarticulo_dineroinicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crearpublicacion',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Autor', to='Esqueleto.usuario'),
        ),
    ]
