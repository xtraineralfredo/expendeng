# Generated by Django 2.1.7 on 2019-04-07 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.CharField(max_length=128)),
                ('frequency', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('BW', 'Bi-Weekly'), ('M', 'Monthly'), ('Q', 'Quarterly'), ('SA', 'Semi-Annually'), ('A', 'Annually')], max_length=2)),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expend.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date', models.DateField()),
                ('frequency', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('BW', 'Bi-Weekly'), ('M', 'Monthly'), ('Q', 'Quarterly'), ('SA', 'Semi-Annually'), ('A', 'Annually')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='income',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expend.Source'),
        ),
        migrations.AddField(
            model_name='expense',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expend.Source'),
        ),
    ]