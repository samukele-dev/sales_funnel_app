# Generated by Django 4.2.4 on 2023-08-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_funnel_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='company',
            field=models.CharField(default='Unknown Company', max_length=100),
        ),
    ]
