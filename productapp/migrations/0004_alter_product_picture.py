# Generated by Django 3.2.3 on 2021-05-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
