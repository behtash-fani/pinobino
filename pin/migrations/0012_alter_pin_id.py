# Generated by Django 3.2 on 2021-05-12 00:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0011_alter_pin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
