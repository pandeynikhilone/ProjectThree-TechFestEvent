# Generated by Django 5.1 on 2024-12-29 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(max_length=255)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.participant')),
            ],
        ),
    ]
