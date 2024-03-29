# Generated by Django 4.2.1 on 2023-05-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(blank=True, choices=[('AC', 'Action'), ('AD', 'Adventure'), ('AN', 'Animation'), ('BI', 'Biography'), ('CO', 'Comedy'), ('CR', 'Crime'), ('DO', 'Documentary'), ('DR', 'Drama'), ('FA', 'Family'), ('FA', 'Fantasy'), ('FI', 'Film-Noir'), ('HI', 'History'), ('HO', 'Horror'), ('MU', 'Musical'), ('MY', 'Mystery'), ('RO', 'Romance'), ('SC', 'Sci-Fi'), ('SH', 'Short'), ('SP', 'Sport'), ('TH', 'Thriller'), ('WA', 'War'), ('WE', 'Western')], default=0, max_length=2),
        ),
    ]
