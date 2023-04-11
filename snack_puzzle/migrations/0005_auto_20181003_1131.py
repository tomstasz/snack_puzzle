# Generated by Django 2.1.1 on 2018-10-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack_puzzle', '0004_auto_20181003_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='measure',
            field=models.CharField(choices=[('gram', 'g'), ('dekagram', 'dag'), ('sztuka', 'szt.'), ('szklanka', 'szklanka'), ('łyżka', 'łyżka'), ('łyżeczka', 'łyżeczka'), ('szczypta', 'szczypta'), ('pęczek', 'pęczek'), ('opakowanie', 'opak.')], default='dag', max_length=32, null=True, verbose_name='Miara'),
        ),
    ]