# Generated by Django 3.2.3 on 2021-06-09 12:29

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(db_index=True, default='Home', max_length=30, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Utask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Task')),
                ('date_create', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date_create')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Date_update')),
                ('achievement', models.BooleanField(blank=True, default=False, verbose_name='achevement')),
                ('category', models.ForeignKey(blank=True, default='Home', on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['-date_create'],
            },
        ),
    ]
