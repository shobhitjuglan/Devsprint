# Generated by Django 4.0.2 on 2022-04-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_payments_payment_id_alter_payments_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='payment_id',
        ),
        migrations.AddField(
            model_name='payments',
            name='id',
            field=models.BigAutoField(auto_created=True, default=123, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
