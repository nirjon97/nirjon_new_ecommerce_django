# Generated by Django 4.0.3 on 2022-05-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_alter_category_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='In_stock',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('False', 'False'), ('True', 'True')], max_length=20),
        ),
    ]
