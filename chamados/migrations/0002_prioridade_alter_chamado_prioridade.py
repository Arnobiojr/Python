# Generated by Django 4.0.3 on 2022-03-13 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prioridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prioridade', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='chamado',
            name='prioridade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chamados.prioridade'),
        ),
    ]