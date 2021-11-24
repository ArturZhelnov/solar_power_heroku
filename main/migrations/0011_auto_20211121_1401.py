# Generated by Django 3.2.6 on 2021-11-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20211121_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='partners')),
                ('link', models.URLField()),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'ordering': ('id',),
            },
        ),
        migrations.AlterField(
            model_name='social_link',
            name='soc_img',
            field=models.FileField(upload_to='Social_images'),
        ),
    ]
