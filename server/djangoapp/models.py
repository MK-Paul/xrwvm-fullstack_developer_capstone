from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()  # Description of the car make

    def __str__(self):
        return self.name  # String representation of the car make


# CarModel model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship with CarMake
    name = models.CharField(max_length=100)  # Name of the car model
    dealer_id = models.IntegerField()  # Dealer ID (from Cloudant database)
    
    # Car type choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')  # Type of car
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),  # Maximum year
            MinValueValidator(2015)  # Minimum year
        ]
    )  # Year of the car model

    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # String representation of the car model
