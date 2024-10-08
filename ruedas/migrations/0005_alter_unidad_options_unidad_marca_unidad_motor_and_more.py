# Generated by Django 5.1 on 2024-09-18 15:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruedas', '0004_alter_imagen_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unidad',
            options={'ordering': ['vendido'], 'verbose_name': 'Unidad', 'verbose_name_plural': 'Unidades'},
        ),
        migrations.AddField(
            model_name='unidad',
            name='marca',
            field=models.CharField(choices=[('Audi', 'Audi'), ('BMW', 'BMW'), ('Chery', 'Chery'), ('Chevrolet', 'Chevrolet'), ('Citroën', 'Citroën'), ('Dodge', 'Dodge'), ('Fiat', 'Fiat'), ('Ford', 'Ford'), ('Geely', 'Geely'), ('Great Wall', 'Great Wall'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('JAC', 'JAC'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Land Rover', 'Land Rover'), ('Lifan', 'Lifan'), ('Mazda', 'Mazda'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan'), ('Peugeot', 'Peugeot'), ('Porsche', 'Porsche'), ('Ram', 'Ram'), ('Renault', 'Renault'), ('SsangYong', 'SsangYong'), ('Subaru', 'Subaru'), ('Suzuki', 'Suzuki'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen')], default='Volkswagen', max_length=50),
        ),
        migrations.AddField(
            model_name='unidad',
            name='motor',
            field=models.IntegerField(choices=[(800, '0.8 L'), (1000, '1.0 L'), (1200, '1.2 L'), (1300, '1.3 L'), (1400, '1.4 L'), (1500, '1.5 L'), (1600, '1.6 L'), (1800, '1.8 L'), (2000, '2.0 L'), (2200, '2.2 L'), (2400, '2.4 L'), (2500, '2.5 L'), (2700, '2.7 L'), (3000, '3.0 L'), (3200, '3.2 L'), (3500, '3.5 L'), (3600, '3.6 L'), (4000, '4.0 L'), (4200, '4.2 L'), (4400, '4.4 L'), (4600, '4.6 L'), (5000, '5.0 L'), (5200, '5.2 L'), (5500, '5.5 L'), (6000, '6.0 L'), (6200, '6.2 L'), (6400, '6.4 L'), (7000, '7.0 L'), (7500, '7.5 L'), (8000, '8.0 L')], default=1600),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(upload_to='media/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])]),
        ),
    ]
