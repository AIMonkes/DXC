# Generated by Django 4.1.7 on 2023-04-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsetaq', '0006_alter_expenses_expenses_alter_expenses_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]