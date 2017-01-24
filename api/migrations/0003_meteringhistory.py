# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170113_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeteringHistory',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
                ('pm01', models.FloatField(help_text='PM 0.1 in ug/m^3')),
                ('pm25', models.FloatField(help_text='PM 2.5 in ug/m^3')),
                ('pm10', models.FloatField(help_text='PM 10 in ug/m^3')),
                ('temp_out1', models.FloatField(help_text='Outside temperature sensor1, in C.')),
                ('temp_out2', models.FloatField(blank=True, default=None, help_text='Outside temperature sensor2, optional, in C.', null=True)),
                ('temp_out3', models.FloatField(blank=True, default=None, help_text='Outside temperature sensor3, optional, in C.', null=True)),
                ('temp_int1', models.FloatField(help_text='Internal temperature sensor1 (air sucked by PM sensor), in C.')),
                ('hum_out1', models.FloatField(help_text='Outside relative humidity sensor1, in %.')),
                ('hum_out2', models.FloatField(blank=True, default=None, help_text='Outside relative humidity sensor2, optional, in %.', null=True)),
                ('hum_out3', models.FloatField(blank=True, default=None, help_text='Outside relative humidity sensor3, optional, in %.', null=True)),
                ('hum_int1', models.FloatField(help_text='Internal relative humidity sensor1 (air sucked by PM sensor), in %.')),
                ('rssi', models.FloatField(help_text='RSSI of WiFi (signal strength). For debugging "vanishing" stations.')),
                ('bpress_out1', models.FloatField(help_text='Outside absolute barometric pressure sensor1, in hPa.')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Station')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
