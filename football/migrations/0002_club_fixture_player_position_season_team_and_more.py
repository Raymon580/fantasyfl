# Generated by Django 4.1.3 on 2022-11-30 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('away_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away', to='football.club')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='players', to='football.club')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('bench', models.ManyToManyField(related_name='benched', to='football.player')),
                ('lineup', models.ManyToManyField(related_name='starters', to='football.player')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='pos_players', to='football.position'),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(default='', max_length=8, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leagues_created', to=settings.AUTH_USER_MODEL)),
                ('teams', models.ManyToManyField(to='football.team')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_goals', to='football.fixture')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='assists', to='football.player')),
                ('scorer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='football.player')),
            ],
        ),
        migrations.CreateModel(
            name='GameWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameweek', models.IntegerField()),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gameweeks', to='football.season')),
            ],
        ),
        migrations.AddField(
            model_name='fixture',
            name='gameweek',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='fixtures', to='football.gameweek'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='home_club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to='football.club'),
        ),
    ]
