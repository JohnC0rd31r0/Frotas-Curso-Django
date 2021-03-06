# Generated by Django 3.2.8 on 2021-11-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_itensentrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='acompanhamento',
            name='motorista',
            field=models.ManyToManyField(default=' ', to='core.Motorista'),
        ),
        migrations.AlterField(
            model_name='acompanhamento',
            name='status',
            field=models.IntegerField(choices=[(1, 'Saída da Portaria'), (2, 'A caminho'), (3, 'Entregue no endereço de destino'), (4, 'Viagem de retorno Iniciada'), (5, 'Se encontra na cede')], default=5),
        ),
    ]
