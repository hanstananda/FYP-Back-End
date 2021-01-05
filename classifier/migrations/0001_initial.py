# Generated by Django 3.1.4 on 2021-01-05 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnakeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SnakeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latin_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classifier.snakeimage')),
            ],
        ),
        migrations.CreateModel(
            name='ClassifySnakeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classifier.snakeinfo')),
                ('snake_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.snakeimage')),
            ],
        ),
    ]
