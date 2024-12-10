# Generated by Django 5.0.6 on 2024-05-28 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('known_for_department', models.CharField(blank=True, max_length=255, null=True)),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('profile_path', models.URLField(blank=True, null=True)),
                ('original_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
