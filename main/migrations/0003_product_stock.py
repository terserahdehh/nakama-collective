# Generated by Django 5.1.1 on 2024-09-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_delete_moodentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
