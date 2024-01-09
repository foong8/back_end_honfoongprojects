# Generated by Django 4.2.7 on 2023-12-25 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_actionitem_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actionitem',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='actionitem_created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
