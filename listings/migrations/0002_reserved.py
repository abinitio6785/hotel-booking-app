# Generated by Django 3.2 on 2021-12-08 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('booking_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserved', to='listings.bookinginfo')),
                ('hotel_room_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserved', to='listings.hotelroom')),
            ],
        ),
    ]
