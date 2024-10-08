# Generated by Django 5.0.3 on 2024-06-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='upload/')),
                ('status', models.BooleanField(help_text='0-show,1-hide')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
