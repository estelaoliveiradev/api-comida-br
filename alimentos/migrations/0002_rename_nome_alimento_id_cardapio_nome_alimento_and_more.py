# Generated by Django 5.0.4 on 2024-05-12 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardapio',
            old_name='nome_alimento_id',
            new_name='nome_alimento',
        ),
        migrations.RenameField(
            model_name='cardapio',
            old_name='nome_refeicao_id',
            new_name='nome_refeicao',
        ),
        migrations.RemoveField(
            model_name='alimento',
            name='nome_categoria_id',
        ),
        migrations.AddField(
            model_name='alimento',
            name='nome_categoria_str',
            field=models.CharField(default=100, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alimento',
            name='nome_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alimentos.categoria'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='kcal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='nome_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alimentos.categoria'),
        ),
        migrations.AlterField(
            model_name='congelamento',
            name='tipo_prato_id',
            field=models.IntegerField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alimentos.tipoprato')),
        ),
    ]
