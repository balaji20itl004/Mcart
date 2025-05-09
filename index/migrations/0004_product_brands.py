# Generated by Django 5.1.3 on 2025-01-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0003_alter_product_new_price_alter_product_original_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="brands",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Apple", "Apple"),
                    ("Vivo", "Vivo"),
                    ("Redmi", "Redmi"),
                    ("Oppo", "Oppo"),
                    ("Samsung", "Samsung"),
                    ("Oneplus", "Oneplus"),
                    ("Lenovo", "Lenovo"),
                    ("Dell", "Dell"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
