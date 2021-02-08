# Generated by Django 3.1.6 on 2021-02-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_monitoring', '0005_collecteddata'),
    ]

    operations = [
        migrations.AddField(
            model_name='collecteddata',
            name='dataSample',
            field=models.JSONField(default={}, help_text='Data sample that was collected and that follows the specific schema defined in the solution', verbose_name='Data Sample'),
            preserve_default=False,
        ),
    ]
