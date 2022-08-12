# Generated by Django 4.1 on 2022-08-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cleaning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaning',
            name='soap',
            field=models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1),
        ),
    ]
