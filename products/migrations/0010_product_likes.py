'''
Imports relevant django packages
'''
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    '''
    Migrations
    '''
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0009_remove_product_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(
                blank=True,
                related_name='product_likes',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
