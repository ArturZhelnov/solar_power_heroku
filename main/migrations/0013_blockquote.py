# Generated by Django 3.2.6 on 2021-11-21 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_footer_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blockquote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citate', models.TextField()),
                ('owner', models.CharField(blank=True, max_length=120)),
                ('position', models.CharField(blank=True, max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
