# Generated by Django 3.2 on 2024-02-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20240218_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_az',
            field=models.CharField(choices=[('POPULAR', 'POPULAR'), ('RECENT', 'RECENT')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='date_en',
            field=models.CharField(choices=[('POPULAR', 'POPULAR'), ('RECENT', 'RECENT')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='type_az',
            field=models.CharField(choices=[('TOP TIPS', 'TOP TIPS'), ('NEW IN', 'NEW IN'), ('HOW TO', 'HOW TO'), ('MASKS', 'MASKS'), ('SUNCARE', 'SUNCARE'), ('BESTSELLERS', 'BESTSELLERS')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='type_en',
            field=models.CharField(choices=[('TOP TIPS', 'TOP TIPS'), ('NEW IN', 'NEW IN'), ('HOW TO', 'HOW TO'), ('MASKS', 'MASKS'), ('SUNCARE', 'SUNCARE'), ('BESTSELLERS', 'BESTSELLERS')], max_length=50, null=True),
        ),
    ]
