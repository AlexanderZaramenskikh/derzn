# Generated by Django 3.2.4 on 2022-03-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0003_znrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('visits', models.ManyToManyField(blank=True, to='drevo.Znanie', verbose_name='ID')),
            ],
        ),
    ]
