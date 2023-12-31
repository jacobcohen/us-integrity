# Generated by Django 4.2.2 on 2023-06-09 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbr', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbr', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('league', models.ForeignKey(db_column='league_abbr', on_delete=django.db.models.deletion.CASCADE, to='myApp.league', to_field='abbr')),
            ],
        ),
    ]
