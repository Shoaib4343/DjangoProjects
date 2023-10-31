# Generated by Django 4.2.6 on 2023-10-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0003_alter_user_is_admin_alter_user_is_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(choices=[('admin', 'Admin'), ('customer', 'Customer'), ('employee', 'Employee')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(choices=[('admin', 'Admin'), ('customer', 'Customer'), ('employee', 'Employee')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(choices=[('admin', 'Admin'), ('customer', 'Customer'), ('employee', 'Employee')]),
        ),
    ]