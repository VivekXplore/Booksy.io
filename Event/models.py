
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.db import models




class Feedback(models.Model):
    email=models.EmailField(max_length=200)
    name=models.CharField(max_length=30)
    suggestion=models.TextField(max_length=50)


def __str__(self):
    return f'{self.name} - {self.suggestion}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    date = models.DateField()
    time_slot = models.CharField(max_length=50)  # e.g., '9:00 AM - 12:00 PM'

    def __str__(self):
        return f"{self.event_type} - {self.date} ({self.time_slot})"
    

# advanced authenticatoin for the account starts form here !

class customUserManager(BaseUserManager):
    def create_user(self,email,password):
        if not email:
            raise ValueError(" email is very necessary")
        email=self.normalize_email(email) # diffrent case ma vako email eg:HEllo@gamil xa bhane hello@....
        user=self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

class CustomUser(AbstractBaseUser):
    email=models.EmailField(unique=True)
    is_active=models.BooleanField(default=False)
    objects=customUserManager()
    USERNAME_FIELD='email'