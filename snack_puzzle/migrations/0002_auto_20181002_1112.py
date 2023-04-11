# Generated by Django 2.1.1 on 2018-10-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack_puzzle', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Pie', 'Pieczywo'), ('Nab', 'Nabiał i jaja'), ('Mię', 'Mięso i ryby'), ('Syp', 'Sypkie'), ('Tłu', 'Tłuszcze'), ('Owo', 'Owoce'), ('Warz', 'Warzywa'), ('Sło', 'Słodycze'), ('Dod', 'Dodatki'), ('Zio', 'Zioła i przyprawy'), ('Nap', 'Napoje'), ('Grz', 'Grzyby')], default='brak', max_length=100, verbose_name='Kategoria'),
        ),
    ]
