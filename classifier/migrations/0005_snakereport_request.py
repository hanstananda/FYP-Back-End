# Generated by Django 3.1.4 on 2021-03-05 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0004_snakereport'),
    ]

    operations = [
        migrations.AddField(
            model_name='snakereport',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classifier.classifysnakerequest'),
        ),
    ]
