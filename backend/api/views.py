from .serializers import Student, Studentserializer
from .models import Student
from rest_framework.generics import ListAPIView

# Create your views here.
class Student(ListAPIView):
    queryset =Student.objects.all()
    serializer_class = Studentserializer