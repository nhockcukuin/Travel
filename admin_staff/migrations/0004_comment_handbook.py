# Generated by Django 3.0.8 on 2020-09-07 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_staff', '0003_posts_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Handbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_hb', models.CharField(max_length=255)),
                ('img_hb', models.ImageField(null=True, upload_to='')),
                ('content_hb', models.TextField(null=True)),
                ('date_cr', models.DateField(auto_now_add=True)),
                ('date_up', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('user_cr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_cmt', models.TextField(null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_staff.Posts')),
                ('user_cmt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]