# Generated by Django 5.0.4 on 2024-05-12 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0002_rename_nome_alimento_id_cardapio_nome_alimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='nome_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alimentos.categoria'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='nome_alimento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alimentos.congelamento'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='nome_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alimentos.categoria'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='nome_refeicao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alimentos.refeicao'),
        ),
        migrations.AlterField(
            model_name='congelamento',
            name='tipo_prato_id',
            field=models.IntegerField(verbose_name=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alimentos.tipoprato')),
        ),
    ]