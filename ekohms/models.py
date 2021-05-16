from django.db import models

# Create your models here.


class User(models.Model):
    pass

class Receptionist(models.Model):
    pass

class Receptionist(models.Model):
    pass

class Room(models.Model):
    pass

class RoomStatus(models.Model):
    pass
class RoomType(models.Model):
    pass

class Booking(models.Model):
    id = models.UUIDField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

class Payment(models.Model):
    pass

class PaymentType(models.Model):
    pass