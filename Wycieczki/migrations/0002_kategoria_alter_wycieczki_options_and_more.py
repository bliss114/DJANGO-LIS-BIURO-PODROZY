# Generated by Django 4.0.4 on 2022-05-14 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Wycieczki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Wycieczka',
                'verbose_name_plural': 'Wycieczki',
            },
        ),
        migrations.AlterModelOptions(
            name='wycieczki',
            options={'verbose_name': 'Wycieczka', 'verbose_name_plural': 'Wycieczki'},
        ),
        migrations.AlterField(
            model_name='wycieczki',
            name='nazwa',
            field=models.CharField(max_length=40),
        ),
        migrations.AddField(
            model_name='wycieczki',
            name='kategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Wycieczki.kategoria'),
        ),
    ]