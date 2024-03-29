# Generated by Django 3.1.4 on 2020-12-30 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_solutions', '0003_auto_20201230_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='objective',
            field=models.OneToOneField(help_text='The final objective of the solution in question', on_delete=django.db.models.deletion.CASCADE, to='monitoring_solutions.solutionobjective', verbose_name='Objective'),
        ),
    ]
