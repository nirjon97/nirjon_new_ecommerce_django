# Generated by Django 4.0.3 on 2022-03-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keyword', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('phone', models.IntegerField()),
                ('fax', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/')),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField()),
                ('contact', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
