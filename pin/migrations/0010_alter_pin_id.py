# Generated by Django 3.2 on 2021-05-11 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0009_alter_pin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='id',
            field=models.UUIDField(default='1813c3406b8147c69ef4d707c5f5a492', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
