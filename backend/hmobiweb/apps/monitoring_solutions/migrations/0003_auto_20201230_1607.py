# Generated by Django 3.1.4 on 2020-12-30 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_solutions', '0002_load_fixture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='category',
            field=models.OneToOneField(help_text='The monitoring category to which the solution belongs', on_delete=django.db.models.deletion.CASCADE, to='monitoring_solutions.monitoringcategory', verbose_name='Category'),
        ),
    ]