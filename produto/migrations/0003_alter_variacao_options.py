# Generated by Django 4.0.5 on 2022-06-03 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_produto_imagem_variacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variação', 'verbose_name_plural': 'Variações'},
        ),
    ]
