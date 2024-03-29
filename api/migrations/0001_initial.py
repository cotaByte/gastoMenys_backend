# Generated by Django 5.0 on 2023-12-28 22:52

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_category', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_month', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.UUIDField(default=uuid.UUID('fe3aa45d-ee67-4218-8f76-6d5249349000'), editable=False)),
                ('username', models.CharField(max_length=35)),
                ('name', models.CharField(max_length=35)),
                ('surnames', models.CharField(max_length=60)),
                ('image', models.TextField(null=True)),
                ('work_as', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_transaction', models.UUIDField(default=uuid.UUID('c346fbc6-d213-442f-842e-1768c778ce10'), editable=False)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.FloatField()),
                ('comments', models.CharField(max_length=150)),
                ('type_transaction', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('id_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
