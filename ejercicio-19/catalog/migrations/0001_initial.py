# Generated by Django 4.2.1 on 2023-05-25 16:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('AC', 'Action'), ('AD', 'Adventure'), ('AN', 'Animation'), ('BI', 'Biography'), ('CO', 'Comedy'), ('CR', 'Crime'), ('DO', 'Documentary'), ('DR', 'Drama'), ('FA', 'Family'), ('FA', 'Fantasy'), ('FI', 'Film-Noir'), ('HI', 'History'), ('HO', 'Horror'), ('MU', 'Musical'), ('MY', 'Mystery'), ('RO', 'Romance'), ('SC', 'Sci-Fi'), ('SH', 'Short'), ('SP', 'Sport'), ('TH', 'Thriller'), ('WA', 'War'), ('WE', 'Western'), ('NO', 'None')], default=0, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this movie', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('sypnosis', models.TextField(help_text='Brief summary of the movie', max_length=128)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.director')),
                ('genre', models.ManyToManyField(to='catalog.genre')),
            ],
        ),
    ]