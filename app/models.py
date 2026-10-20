import uuid

from django.db import models

# Create your models here.


from django.db import models


class Appointment(models.Model):

    SERVICE_CHOICES = [
        ('Box Braids', 'Box Braids'),
        ('Knotless Braids', 'Knotless Braids'),
        ('Cornrows', 'Cornrows'),
        ('Ghana Braids', 'Ghana Braids'),
        ('Natural Hair', 'Natural Hair'),
        ('Locs', 'Locs'),
        ('Wig Installation', 'Wig Installation'),
        ('Bridal Hairstyles', 'Bridal Hairstyles'),
        ('Kids Hairstyles', 'Kids Hairstyles'),
        ('Hair Treatment', 'Hair Treatment'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    full_name = models.CharField(max_length=150)

    phone = models.CharField(max_length=30)

    email = models.EmailField(blank=True, null=True)

    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField() 
    message = models.TextField(
        blank=True,
        null=True
    )
    public_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    confirmation_sent_at = models.DateTimeField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.service} - {self.appointment_date}"



class Service(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="services/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name




class SalonSetting(models.Model):
    salon_name = models.CharField(max_length=150, default="Kora Hair & Beauty")
    phone = models.CharField(max_length=30, default="+2335555524063")
    email = models.EmailField(default="hello@korahairbeauty.com")
    address = models.CharField(max_length=250, default="Accra, Ghana")
    whatsapp_number = models.CharField(max_length=30, default="2335555524063")

    def __str__(self):
        return self.salon_name


class GalleryImage(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="gallery/")
    category = models.CharField(max_length=80, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title





import uuid


class Appointment_Status(models.Model):

    SERVICE_CHOICES = [
        ('Box Braids', 'Box Braids'),
        ('Knotless Braids', 'Knotless Braids'),
        ('Cornrows', 'Cornrows'),
        ('Ghana Braids', 'Ghana Braids'),
        ('Natural Hair', 'Natural Hair'),
        ('Locs', 'Locs'),
        ('Wig Installation', 'Wig Installation'),
        ('Hair Treatment', 'Hair Treatment'),
        ('Hair Styling', 'Hair Styling'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    # Appointment reference
    reference = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    # Customer information
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    # Appointment information
    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES
    )

    date = models.DateField()

    time = models.TimeField()

    # Optional stylist
    stylist = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    # Appointment status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    # Reason if rejected
    rejection_reason = models.TextField(
        blank=True,
        null=True
    )

    # Optional customer message
    message = models.TextField(
        blank=True,
        null=True
    )

    # Created and updated dates
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):

        if not self.reference:
            self.reference = f"APT-{uuid.uuid4().hex[:8].upper()}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference} - {self.name}"
