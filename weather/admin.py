from django.contrib import admin
from .models import WeatherData

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('city', 'temperature', 'humidity', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('city', 'country')
