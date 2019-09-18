# Generated by Django 2.2.1 on 2019-09-16 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hn', models.CharField(max_length=200)),
                ('pincode', models.IntegerField(max_length=6)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('book_desc', models.TextField()),
                ('book_date', models.DateTimeField(auto_now_add=True)),
                ('book_image', models.ImageField(default='bk.png', upload_to='Books')),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bookCot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BookCot')),
                ('book_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Signup')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Location')),
            ],
        ),
    ]
