# Generated by Django 3.2.5 on 2021-07-24 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='name')),
                ('surname', models.CharField(max_length=50, verbose_name='surname')),
                ('othername', models.CharField(max_length=50, verbose_name='othername')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
                ('phone', models.CharField(max_length=50, verbose_name='phone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('resume', models.FileField(help_text='Upload a pdf file', upload_to='uploaded_resumes/', verbose_name='resume')),
            ],
            options={
                'verbose_name': 'Applicant',
                'verbose_name_plural': 'Applicants',
            },
        ),
    ]
