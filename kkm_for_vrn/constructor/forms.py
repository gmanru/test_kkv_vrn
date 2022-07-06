from django.forms import ModelForm
from .models import Ticket
#from people.models import Student


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


'''class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'''
