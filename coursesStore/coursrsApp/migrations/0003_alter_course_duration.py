# Generated by Django 4.0.4 on 2022-06-05 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursrsApp', '0002_alter_course_price_remove_order_course_order_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
