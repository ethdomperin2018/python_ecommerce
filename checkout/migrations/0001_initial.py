'''
Imports relevant django packages
'''
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    '''
    Migration dependencies for the checkout
    '''
    initial = True

    dependencies = [
        ('products', '0003_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('order_number', models.CharField(
                    editable=False,
                    max_length=30)),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=250)),
                ('country', models.CharField(max_length=50)),
                ('town_or_city', models.CharField(max_length=50)),
                ('postcode', models.CharField(
                    blank=True,
                    max_length=20,
                    null=True)),
                ('street_address1', models.CharField(max_length=100)),
                ('street_address2', models.CharField(
                    blank=True,
                    max_length=100,
                    null=True)),
                ('county', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('delivery_cost', models.DecimalField(
                    decimal_places=2,
                    default=0,
                    max_digits=6)),
                ('order_total', models.DecimalField(
                    decimal_places=2,
                    default=0,
                    max_digits=12)),
                ('grand_total', models.DecimalField(
                    decimal_places=2,
                    default=0,
                    max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(
                    decimal_places=2,
                    editable=False,
                    max_digits=6)),
                ('order', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='lineitems',
                    to='checkout.order')),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='products.product')),
            ],
        ),
    ]
