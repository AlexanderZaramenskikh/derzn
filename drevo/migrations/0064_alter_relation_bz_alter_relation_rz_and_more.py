# Generated by Django 4.1.1 on 2023-04-18 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0063_relation_director_relation_expert_relationstatuses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='bz',
            field=models.ForeignKey(help_text='укажите базовое знание', on_delete=django.db.models.deletion.CASCADE, related_name='base', to='drevo.znanie', verbose_name='Базовое знание'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='rz',
            field=models.ForeignKey(help_text='укажите связанное знание', on_delete=django.db.models.deletion.CASCADE, related_name='related', to='drevo.znanie', verbose_name='Связанное знание'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='tr',
            field=models.ForeignKey(help_text='укажите вид связи', on_delete=django.db.models.deletion.CASCADE, to='drevo.tr', verbose_name='Вид связи'),
        ),
        migrations.AlterField(
            model_name='relationstatuses',
            name='status',
            field=models.CharField(choices=[('WORK_PRE', 'ПредСвязь в работе'), ('WORK', 'Связь в работе'), ('PRE_READY', 'Готовая ПредСвязь'), ('PRE_FIN', 'Завершенная ПредСвязь'), ('FIN', 'Завершенная Связь'), ('PRE_EXP', 'Экспертизв ПредСвязи'), ('REJ', 'Отклоненная Связь'), ('PRE_REJ', 'Отклоненная ПредСвязь'), ('PUB_PRE', 'Опубликованная ПредСвязь'), ('PUB', 'Опубликованная Связь')], default=None, max_length=12, null=True, verbose_name='Статус'),
        ),
    ]
