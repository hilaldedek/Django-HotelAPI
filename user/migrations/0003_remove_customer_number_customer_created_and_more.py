# Generated by Django 4.2 on 2023-06-02 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_remove_customer_email_remove_customer_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='number',
        ),
        migrations.AddField(
            model_name='customer',
            name='created',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('-', 'Prefer not to say')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='user_age',
            field=models.CharField(choices=[('0-12', 'ucretsiz'), ('12-65', 'tam'), ('65+', '%50 indirimli')], max_length=6, null=True),
        ),
    ]
