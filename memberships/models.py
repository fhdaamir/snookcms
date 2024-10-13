from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_type = models.CharField(max_length=20, choices=[
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('vip', 'VIP')
    ])
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    booking_time = models.DateTimeField()
    duration = models.IntegerField(help_text="Duration in hours")

    def __str__(self):
        return f"{self.member.name} - Table {self.table_number}"
