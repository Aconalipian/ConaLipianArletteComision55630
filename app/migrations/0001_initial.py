# Generated by Django 4.2.3 on 2023-08-25 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cdirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'director',
                'verbose_name_plural': 'Directores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='cpelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_estreno', models.DateField()),
                ('productora', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'pelicula',
                'verbose_name_plural': 'Peliculas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='cproductora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'productora',
                'verbose_name_plural': 'Productoras',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='cAvatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
