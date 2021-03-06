# Generated by Django 4.0.5 on 2022-06-13 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SchemaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schemaname', models.CharField(blank=True, max_length=100)),
                ('changelog', models.TextField(blank=True, max_length=300)),
                ('changedfields', models.CharField(blank=True, max_length=500)),
                ('schemafile', models.FileField(default='sample.txt', upload_to='schemas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
