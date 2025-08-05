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
   email=models.EmailField(max_length=250,default="chandumoger@123")
   profile_name=models.CharField(max_length=100,default='user')
def __str__(self):
    return f"{self.bio} {self.email}"

   


class Comment(models.Model):
    course = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:30]}"
    
    def is_reply(self):
        return self.parent is not None




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






















































































