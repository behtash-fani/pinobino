# Generated by Django 3.2 on 2021-05-12 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0010_alter_pin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='id',
            field=models.UUIDField(default='9793da073fd94eac9fd90cb984f82ff7', editable=False, primary_key=True, serialize=False),
        ),
    ]
