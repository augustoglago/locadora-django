# Generated by Django 4.2.5 on 2023-09-26 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_atordiretor_nacionalidade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atordiretor',
            name='nacionalidade',
        ),
        migrations.AddField(
            model_name='atordiretor',
            name='nacionalidade',
            field=models.ManyToManyField(to='app.pais'),
        ),
    ]