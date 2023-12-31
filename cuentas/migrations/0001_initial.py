# Generated by Django 4.0.10 on 2023-12-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tienda', '0002_categoria_is_sub_categoria_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_manager', models.BooleanField(default=False)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to='tienda.producto')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
