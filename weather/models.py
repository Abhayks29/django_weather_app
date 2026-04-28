from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    temperature = models.FloatField()
    feels_like = models.FloatField(null=True, blank=True)
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    description = models.CharField(max_length=100)
    wind_speed = models.FloatField()
    cloudiness = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.city} - {self.temperature}°C"
    
    class Meta:
        ordering = ['-timestamp']
