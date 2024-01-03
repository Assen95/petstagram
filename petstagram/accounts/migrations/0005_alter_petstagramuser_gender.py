# Generated by Django 4.2.7 on 2023-12-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_petstagramuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Do Not Show')], default=3, max_length=1),
        ),
    ]
