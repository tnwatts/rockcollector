# Generated by Django 4.1 on 2022-08-11 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_dirt_alter_cleaning_soap'),
    ]

    operations = [
        migrations.AddField(
            model_name='rock',
            name='dirt',
            field=models.ManyToManyField(to='main_app.dirt'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('rock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.rock')),
            ],
        ),
    ]