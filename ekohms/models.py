from django.db import models
from django.db.models.deletion import CASCADE

class User(models.Model):
    id=models.UUIDField(primary_key=True)
    username= models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    phone_number=models.CharField(max_length=12)
    password=models.CharField(max_length=10)
    otp_code= models.CharField(max_length=10)
    email_verified=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superadmin= models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
class Receptionist(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user_id =models.OneToOneField(Users,
                                  on_delete=CASCADE,
                                  primary_key=True)
    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gender= models.CharField(max_length=1,choices=GENDER)
    avatar_url=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name,self.last_name

class Booking(models.Model):
    id = models.UUIDField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.id
