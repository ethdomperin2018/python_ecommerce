'''
Imports relevant django packages
'''
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    '''
    Migration dependencies for products
    '''
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('friendly_name', models.CharField(
                    blank=True,
                    max_length=300,
                    null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('sku', models.CharField(
                    blank=True,
                    max_length=300,
                    null=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(
                    blank=True,
                    decimal_places=2,
                    max_digits=6,
                    null=True)),
                ('image_url', models.URLField(
                    blank=True,
                    max_length=2000,
                    null=True)),
                ('image', models.ImageField(
                    blank=True,
                    null=True,
                    upload_to='')),
                ('category', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='products.category')),
            ],
        ),
    ]
