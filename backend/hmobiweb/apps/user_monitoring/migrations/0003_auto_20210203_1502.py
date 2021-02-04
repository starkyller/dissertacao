# Generated by Django 3.1.4 on 2021-02-03 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_solutions', '0006_auto_20210102_1447'),
        ('user_monitoring', '0002_auto_20210203_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersolutions',
            name='solution',
            field=models.ForeignKey(help_text='The solution to be associated with a specific patient', on_delete=django.db.models.deletion.CASCADE, to='monitoring_solutions.solution', verbose_name='Solution'),
        ),
    ]