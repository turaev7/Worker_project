# Generated by Django 4.1.5 on 2023-01-28 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.CharField(max_length=200)),
                ('worker_adress', models.CharField(max_length=200)),
                ('worker_staff', models.FloatField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('worker_age', models.DateField()),
                ('worker_pic', models.ImageField(upload_to='rasm')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organization')),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
            },
        ),
        migrations.CreateModel(
            name='Worker_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.worker')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organization')),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='Relatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('addres', models.CharField(max_length=200)),
                ('work', models.CharField(max_length=200)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.worker')),
            ],
            options={
                'verbose_name': 'Relatives',
                'verbose_name_plural': 'Relatives',
            },
        ),
    ]
