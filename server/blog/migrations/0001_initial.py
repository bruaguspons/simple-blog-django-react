# Generated by Django 4.1.2 on 2022-10-29 17:41

import blog.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('content', models.TextField(null=True)),
                ('image', models.ImageField(default='', upload_to=blog.models.blog_directory)),
                ('published', models.DateField(default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]
