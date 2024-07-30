# Generated by Django 5.0.7 on 2024-07-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_order_customer_alter_order_transaction_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]