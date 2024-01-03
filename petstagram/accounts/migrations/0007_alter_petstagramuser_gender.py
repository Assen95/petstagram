# Generated by Django 4.2.7 on 2023-12-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_petstagramuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('D', 'Do not show')], max_length=1),
        ),
    ]
