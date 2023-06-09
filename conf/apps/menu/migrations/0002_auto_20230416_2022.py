# Generated by Django 3.2.3 on 2023-04-16 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='menu.foodcategory'),
        ),
        migrations.AlterField(
            model_name='food',
            name='toppings',
            field=models.ManyToManyField(related_name='foods', to='menu.Topping'),
        ),
    ]
