# Generated by Django 4.0.5 on 2022-08-10 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esqueleto', '0010_alter_articulo_imgarticulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='ImgArticulo',
            field=models.ImageField(default='Articulos/Nada.jpg', null=True, upload_to='Articulos'),
        ),
    ]
