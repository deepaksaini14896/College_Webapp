from rest_framework.serializers import ModelSerializer
from .models import Super_Admin, Teacher, Student

# super admin serializer
class Super_Admin_Serializer(ModelSerializer):
	class Meta:
		model = Super_Admin
		fields = '__all__'

# teacher serializer
class Teacher_Serializer(ModelSerializer):
	class Meta:
		model = Teacher
		fields = '__all__'

# student serializer
class Student_Serializer(ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'