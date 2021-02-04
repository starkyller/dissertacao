# Generated by Django 3.1.4 on 2021-02-03 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_auto_20201222_1110'),
        ('monitoring_solutions', '0006_auto_20210102_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSolutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(help_text='The patient to be associated with a specific solution', on_delete=django.db.models.deletion.CASCADE, to='users.patient', verbose_name='Patient')),
                ('solution', models.ForeignKey(help_text='The solution to be associated with a specific patient', on_delete=django.db.models.deletion.CASCADE, to='monitoring_solutions.solution', verbose_name='Solution')),
            ],
            options={
                'verbose_name': 'User Monitoring Solution',
                'verbose_name_plural': 'User Monitoring Solutions',
            },
        ),
    ]
