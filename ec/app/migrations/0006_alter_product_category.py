# Generated by Django 5.1.7 on 2025-03-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('1Y', 'FIRST YEAR'), ('2Y', 'SECOND YEAR'), ('3Y', 'THIRD YEAR'), ('4Y', 'FINAL YEAR'), ('OT', 'OTHER PRODUCTS')], max_length=2),
        ),
    ]
