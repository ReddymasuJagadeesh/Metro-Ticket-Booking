# Generated by Django 5.1.6 on 2025-03-13 10:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0001_add_profile_model'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_routes', to='metro.station')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_routes', to='metro.station')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField(auto_now_add=True)),
                ('travel_date', models.DateField()),
                ('payment_status', models.BooleanField(default=False)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metro.route')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
