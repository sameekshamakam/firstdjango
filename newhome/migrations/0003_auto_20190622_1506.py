# Generated by Django 2.2.2 on 2019-06-22 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhome', '0002_auto_20190622_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='book_00name',
            new_name='book_name',
        ),
    ]