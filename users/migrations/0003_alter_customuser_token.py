# Generated by Django 4.2.2 on 2024-06-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='token'),
        ),
    ]
