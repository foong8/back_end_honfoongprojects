# Generated by Django 4.2.7 on 2023-12-21 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_country_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subcat',
            field=models.CharField(blank=True, choices=[('Module_A', 'Module_A'), ('Module_B', 'Module_B'), ('Module_C', 'Module_C'), ('Module_D', 'Module_D')], default='Module_A', max_length=255, null=True),
        ),
    ]
