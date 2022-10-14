# Generated by Django 4.1.2 on 2022-10-13 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Estudiantes',
        ),
        migrations.AlterField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
