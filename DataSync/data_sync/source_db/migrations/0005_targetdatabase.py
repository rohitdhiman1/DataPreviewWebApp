# Generated by Django 3.0.8 on 2020-07-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source_db', '0004_sourcedatabase_database_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateField()),
                ('database_id', models.IntegerField(default=0)),
            ],
        ),
    ]
