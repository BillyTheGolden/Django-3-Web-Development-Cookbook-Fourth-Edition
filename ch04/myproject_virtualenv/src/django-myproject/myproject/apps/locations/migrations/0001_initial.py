# Generated by Django 2.2.4 on 2019-09-30 08:37

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import myproject.apps.locations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('uuid', models.UUIDField(default=None, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('street_address', models.CharField(blank=True, max_length=255, verbose_name='Street address')),
                ('street_address2', models.CharField(blank=True, max_length=255, verbose_name='Street address (2nd line)')),
                ('postal_code', models.CharField(blank=True, max_length=255, verbose_name='Postal code')),
                ('city', models.CharField(blank=True, max_length=255, verbose_name='City')),
                ('country', models.CharField(blank=True, choices=[('BE', 'Belgium'), ('BG', 'Bulgaria'), ('CZ', 'Czechia'), ('DK', 'Denmark'), ('DE', 'Germany'), ('EE', 'Estonia'), ('IE', 'Ireland'), ('EL', 'Greece'), ('ES', 'Spain'), ('FR', 'France'), ('HR', 'Croatia'), ('IT', 'Italy'), ('CY', 'Cyprus'), ('LV', 'Latvia'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('HU', 'Hungary'), ('MT', 'Malta'), ('NL', 'Netherlands'), ('AT', 'Austria'), ('PL', 'Poland'), ('PT', 'Portugal'), ('RO', 'Romania'), ('SI', 'Slovenia'), ('SK', 'Slovakia'), ('FI', 'Finland'), ('SE', 'Sweden'), ('UK', 'United Kingdom')], max_length=255, verbose_name='Country')),
                ('geoposition', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('picture', models.ImageField(upload_to=myproject.apps.locations.models.upload_to, verbose_name='Picture')),
                ('rating', models.PositiveIntegerField(blank=True, choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], null=True, verbose_name='Rating')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
    ]
