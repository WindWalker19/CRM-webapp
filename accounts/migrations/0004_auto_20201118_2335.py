# Generated by Django 3.1.3 on 2020-11-18 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_ordermod_productmod'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermod',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customermod'),
        ),
        migrations.AddField(
            model_name='ordermod',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.productmod'),
        ),
    ]
