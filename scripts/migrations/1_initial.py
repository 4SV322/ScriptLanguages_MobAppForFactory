from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Лицевой счёт',
                'verbose_name_plural': 'Лицевые счёта',
            },
        ),
    ]
