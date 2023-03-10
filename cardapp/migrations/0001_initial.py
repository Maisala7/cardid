# Generated by Django 4.1.7 on 2023-02-23 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_center', models.CharField(blank=True, choices=[('Bahri', 'Bahri'), ('Khartoum', 'Khartoum'), ('Omdurman', 'Omdurman')], max_length=25, null=True)),
                ('statu', models.CharField(choices=[('waiting', 'waiting'), ('accept', 'accept'), ('reject', 'reject')], default='waiting', max_length=25)),
                ('FirstName', models.CharField(max_length=25)),
                ('SecondName', models.CharField(max_length=25)),
                ('ThirdName', models.CharField(max_length=25)),
                ('FourtName', models.CharField(max_length=25)),
                ('Birthdate', models.DateField()),
                ('Placeof_Birth', models.CharField(max_length=25)),
                ('Blood_Type', models.CharField(max_length=25)),
                ('Job', models.CharField(max_length=25)),
                ('Address', models.CharField(max_length=25)),
                ('Phone', models.CharField(max_length=25)),
                ('Old_id', models.CharField(max_length=25, unique=True)),
                ('card_date', models.DateField(auto_now_add=True)),
                ('date_of_expiry', models.DateField(blank=True, null=True)),
                ('date_of_accept', models.DateField(blank=True, null=True)),
                ('date_of_reject', models.DateField(blank=True, null=True)),
                ('card_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_number', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='requestes_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardapp.card')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardapp.card')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_Notification', models.ImageField(upload_to=None)),
                ('process_number', models.IntegerField(blank=True, null=True)),
                ('payment_date', models.DateField(auto_now=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardapp.card')),
            ],
        ),
    ]
