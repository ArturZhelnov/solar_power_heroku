# Generated by Django 3.2.6 on 2021-11-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_info_tab_tab_context'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab_context',
            name='tab_text',
            field=models.TextField(),
        ),
    ]