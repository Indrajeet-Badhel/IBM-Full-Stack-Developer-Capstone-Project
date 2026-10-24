from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.name 


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('COUPE', 'Coupe'),
        ('EXOTIC', 'Exotic/Supercar'),
        ('HISTORIC', 'Historic'),
        ('HYBRID', 'Hybrid/EV'),
        ('RV', 'Recreational Vehicle'),
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('TRUCK', 'Truck'),
        ('WAGON', 'Wagon'),
        ('VAN', 'Van')
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2024,
        validators=[
            MaxValueValidator(2025),
            MinValueValidator(1886)
        ])

    def __str__(self):
        return self.name  # Return the name as the string representation

