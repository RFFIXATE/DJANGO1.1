# Generated by Django 4.2.5 on 2023-10-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favoritos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritos',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
