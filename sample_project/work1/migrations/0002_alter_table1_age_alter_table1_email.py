# Generated by Django 5.0.4 on 2024-05-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='table1',
            name='email',
            field=models.EmailField(max_length=20),
        ),
    ]