# Generated by Django 5.0.3 on 2024-05-08 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0018_remove_cancelorder_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CancelOrder',
            new_name='CancellationReason',
        ),
    ]