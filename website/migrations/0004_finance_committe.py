# Generated by Django 2.2.3 on 2019-07-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190720_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance_Committe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Details', models.CharField(max_length=30)),
                ('Designation', models.CharField(max_length=10)),
            ],
        ),
    ]
