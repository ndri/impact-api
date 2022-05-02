# Generated by Django 4.0.4 on 2022-05-02 10:04

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charity_name', models.CharField(max_length=200)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MaxImpactFundGrant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField(validators=[api.models.validate_year])),
                ('start_month', models.IntegerField(validators=[api.models.validate_month])),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField(validators=[api.models.validate_year])),
                ('start_month', models.IntegerField(validators=[api.models.validate_month])),
                ('cents_per_output', models.IntegerField()),
                ('short_output_description', models.CharField(max_length=100)),
                ('long_output_description', models.CharField(max_length=5000)),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.charity')),
            ],
        ),
        migrations.CreateModel(
            name='Allotment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_in_cents', models.IntegerField()),
                ('number_outputs_purchased', models.IntegerField()),
                ('short_output_description', models.CharField(max_length=100)),
                ('long_output_description', models.CharField(max_length=5000)),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.charity')),
                ('max_impact_fund_grant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.maximpactfundgrant')),
            ],
        ),
    ]
