from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Author(models.Model):
   name=models.CharField(max_length=150)

   def __str__(self):
       return f"{self.name}"
  




class Book(models.Model):
   title=models.CharField(max_length=150)
   author=models.ForeignKey(Author,on_delete=models.CASCADE)
   image=models.ImageField(upload_to='image/')

   def __str__(self):
       return f"{self.title}"
   






class Profile(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   bio=models.TextField()
   image2=models.ImageField(upload_to='photos/',default='photos/default.jpg',null=True)

   



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return f"{self.comment} {self.created_at}"




class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    def __str__(self):
       return f"{self.stars}"



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    saved_on = models.DateTimeField(auto_now_add=True)




class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)




class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)

    quantity=models.PositiveIntegerField(default=1)






















































































