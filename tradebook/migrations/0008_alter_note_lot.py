# Generated by Django 4.0.1 on 2022-01-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradebook', '0007_alter_note_lot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='lot',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default='1', max_length=9),
        ),
    ]