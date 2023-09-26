# Generated by Django 4.2.5 on 2023-09-25 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtorDiretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=100)),
                ('insta', models.CharField(max_length=50)),
                ('face', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.CharField(max_length=10)),
                ('sinopse', models.CharField(max_length=300)),
                ('siteOficial', models.CharField(max_length=50)),
                ('dataLancamento', models.DateTimeField()),
                ('notaAvaliacao', models.CharField(max_length=10)),
                ('diretor', models.ManyToManyField(to='app.atordiretor')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nomeContinente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.continente')),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.CharField(max_length=30)),
                ('sinopse', models.CharField(max_length=300)),
                ('siteOficial', models.CharField(max_length=50)),
                ('dataLancamento', models.DateTimeField()),
                ('notaAvaliacao', models.CharField(max_length=10)),
                ('diretor', models.ManyToManyField(to='app.atordiretor')),
                ('genero', models.ManyToManyField(to='app.genero')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SerieEp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ep', models.ManyToManyField(to='app.episodio')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
                ('temp', models.ManyToManyField(to='app.temporada')),
            ],
        ),
        migrations.CreateModel(
            name='FilmeAtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ator', models.ManyToManyField(to='app.atordiretor')),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.filme')),
            ],
        ),
        migrations.AddField(
            model_name='filme',
            name='genero',
            field=models.ManyToManyField(to='app.genero'),
        ),
        migrations.AddField(
            model_name='filme',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pais'),
        ),
        migrations.AddField(
            model_name='atordiretor',
            name='nacionalidade',
            field=models.ManyToManyField(to='app.pais'),
        ),
    ]
