# Generated by Django 2.0.4 on 2018-05-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='Subject',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(),
        ),
    ]