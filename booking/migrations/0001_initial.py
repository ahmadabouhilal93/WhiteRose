# Generated by Django 4.0.2 on 2022-03-01 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('paid', models.BooleanField(default=False)),
                ('booked', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='customer.customer')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='rooms.room')),
            ],
        ),
    ]