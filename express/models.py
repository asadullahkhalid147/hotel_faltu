from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)
    price_per_night= models.IntegerField()
    hotel_img1 =models.ImageField(upload_to='photos/hotels')
    
    descriptions=models.TextField()
    slug = models.SlugField(max_length= 100, unique = True,default=None)
    customers = models.ManyToManyField(User, related_name='booked_hotel',blank = True)
    country_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.hotel_name
    




class Rating(models.Model):
    RATING= (
    (1, '1 out of 5'),
    (2, '2 out of 5'),
    (3, '3 out of 5'),
    (4, '4 out of 5'),
    (5, '5 out of 5'),  
)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='ratings')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    descrip = models.TextField()
    rating = models.IntegerField(choices=RATING) 


  
    