from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('temperature', models.FloatField()),
                ('feels_like', models.FloatField(blank=True, null=True)),
                ('humidity', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('wind_speed', models.FloatField()),
                ('cloudiness', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
