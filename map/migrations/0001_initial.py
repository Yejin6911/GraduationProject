# Generated by Django 2.2.9 on 2020-10-06 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('management', models.CharField(max_length=30)),
                ('S_address', models.TextField(null=True)),
                ('L_address', models.TextField(null=True)),
                ('purpose', models.TextField(null=True)),
                ('camera_num', models.IntegerField(null=True)),
                ('camera_pixel', models.IntegerField(null=True)),
                ('shoot_info', models.TextField(null=True)),
                ('storage_days', models.IntegerField(null=True)),
                ('installed_date', models.TextField(null=True)),
                ('phone', models.TextField(null=True)),
                ('latitude', models.TextField(null=True)),
                ('longitude', models.TextField(null=True)),
                ('data_date', models.DateField(null=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Station')),
            ],
        ),
    ]
