# Generated by Django 4.1.3 on 2022-11-03 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bins', '0003_bins_reg_date_alter_bins_x_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bins',
            old_name='x_location',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='bins',
            old_name='y_location',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='bins',
            old_name='reg_date',
            new_name='registeredTime',
        ),
    ]
