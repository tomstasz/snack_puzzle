# Generated by Django 2.1.1 on 2018-10-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack_puzzle', '0007_auto_20181003_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='measure',
            field=models.CharField(choices=[('g', 'g.'), ('dag', 'dag'), ('szt.', 'szt.'), ('szklan.', 'szklan.'), ('łyż.', 'łyż.'), ('łyżecz..', 'łyżecz.'), ('szczypt.', 'szczypt.'), ('pęcz.', 'pęcz.'), ('opak.', 'opak.'), ('l.', 'l.')], default='dag', max_length=32, null=True, verbose_name='Miara'),
        ),
    ]
