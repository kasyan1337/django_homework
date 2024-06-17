# Generated by Django 5.0.6 on 2024-06-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='version',
            new_name='version_number',
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]