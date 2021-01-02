# Generated by Django 3.1.4 on 2021-01-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_solutions', '0004_auto_20201230_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='description',
            field=models.TextField(blank=True, help_text='Optional: Provide a description for your solution', max_length=350, verbose_name='Description'),
        ),
    ]
