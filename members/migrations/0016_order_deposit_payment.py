# Generated by Django 5.0.3 on 2024-05-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_order_deposit_proof'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deposit_payment',
            field=models.BooleanField(default=False),
        ),
    ]
