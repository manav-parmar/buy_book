# Generated by Django 4.1.3 on 2022-11-07 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=200)),
                ('bookprice', models.IntegerField()),
                ('bookpage', models.IntegerField()),
                ('authername', models.CharField(max_length=300)),
                ('booklanguage', models.CharField(max_length=300)),
                ('bookquantity', models.CharField(max_length=10)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Buybook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('buydate', models.DateField()),
                ('returndate', models.DateField()),
                ('buybookquantity', models.CharField(max_length=10)),
                ('buy', models.BooleanField()),
                ('phone', models.CharField(max_length=10)),
                ('deleted', models.BooleanField(default=False)),
                ('bookdetail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.book')),
            ],
        ),
    ]
