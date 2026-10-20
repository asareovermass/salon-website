from django import forms
from . models import Appointment, Service,GalleryImage


from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            'full_name',
            'phone',
            'email',
            'service',
            'appointment_date',
            'appointment_time',
            'message',
        ]

        widgets = {
            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'appointment_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name",  "price", "image", ]


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ["title", "image", "category", "is_featured"]

