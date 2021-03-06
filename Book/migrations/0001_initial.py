# Generated by Django 3.1 on 2020-08-26 19:31

import Book.validators
from django.db import migrations, models
import django.db.models.deletion
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=30)),
                ('ISBN', isbn_field.fields.ISBNField(max_length=28, unique=True, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Book.author')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('rating', models.IntegerField(default=None, validators=[Book.validators.ratings_validator])),
                ('book', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to='Book.book')),
            ],
            options={
                'ordering': ['book'],
            },
        ),
    ]
