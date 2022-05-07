from django.db import models

# Create your models here.
# super admin model
class Super_Admin(models.Model):
	name = models.CharField(max_length = 50)
	phone = models.IntegerField(unique = True)
	password = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

# teacher model
class Teacher(models.Model):
	name = models.CharField(max_length = 50)
	phone = models.IntegerField(unique = True)
	password = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

# student model
class Student(models.Model):
	name = models.CharField(max_length = 50)
	phone = models.IntegerField(unique = True)
	password = models.CharField(max_length = 50)

	def __str__(self):
		return self.name