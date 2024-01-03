# Generated by Django 4.2.7 on 2023-11-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('personal_photo', models.URLField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
