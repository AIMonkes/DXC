# Generated by Django 4.1.7 on 2023-03-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsetaq', '0002_alter_expenses_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='categories',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='income',
            name='income',
            field=models.IntegerField(default=''),
        ),
    ]
