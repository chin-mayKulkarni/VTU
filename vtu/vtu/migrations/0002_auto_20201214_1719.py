# Generated by Django 3.1.4 on 2020-12-14 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masternotes',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Branch_owner', to='vtu.masterbranches'),
        ),
        migrations.AddField(
            model_name='masternotes',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Semester_owner', to='vtu.mastersemesters'),
        ),
    ]