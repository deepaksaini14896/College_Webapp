from django.shortcuts import render
from .models import Super_Admin, Teacher, Student
from .serializers import Super_Admin_Serializer, Teacher_Serializer, Student_Serializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from utils import create_token, check_token

# Create your views here.
class RegisterSuperAdminAPI(ViewSet):
	# register super admin api
	def create(self,request):
		serializers = Super_Admin_Serializer(data = request.data)

		if serializers.is_valid():
			serializers.save()
			return Response( { "Message" : "Super Admin Added" } )

		return Response(serializers.errors)

class RegisterTeacherAPI(ViewSet):
	# register teacher api
	def create(self,request):
		serializers = Teacher_Serializer(data = request.data)

		if serializers.is_valid():
			serializers.save()
			return Response( { "Message" : "Teacher Added" } )

		return Response(serializers.errors)

class RegisterStudentAPI(ViewSet):
	# register student api
	def create(self,request):
		serializers = Student_Serializer(data = request.data)

		if serializers.is_valid():
			serializers.save()
			return Response( { "Message" : "Student Added" } )

		return Response(serializers.errors)

class LoginSuperAdminAPI(ViewSet):
	# login super admin api
	def create(self, request):
		try:
			sadm = Super_Admin.objects.get( phone = request.data['phone'] )
		except Super_Admin.DoesNotExist:
			return Response( { "Message" : "Super admin not found" } )

		if request.data['password'] == sadm.password:
			user_type = 1
			token = create_token(sadm.phone, user_type)
			return Response( { "Token" : token } )

		return Response( { "Message" : "Password doesn't match" } )

class LoginTeacherAPI(ViewSet):
	# login teacher api
	def create(self, request):
		try:
			tchr = Teacher.objects.get( phone = request.data['phone'] )
		except Teacher.DoesNotExist:
			return Response( { "Message" : "Teacher not found" } )

		if request.data['password'] == tchr.password:
			user_type =2
			token = create_token(tchr.phone, user_type)
			return Response( { "Token" : token } )

		return Response( { "Message" : "Password doesn't match" } )

class LoginStudentAPI(ViewSet):
	# login student api
	def create(self, request):
		try:
			sdnt = Student.objects.get( phone = request.data['email_or_phone'] )
		except Student.DoesNotExist:
			return Response( { "Message" : "Student not found" } )

		if request.data['password'] == sdnt.password:
			user_type = 3
			token = create_token(sdnt.phone, user_type)
			return Response( { "Token" : token } )

		return Response( { "Message" : "Password doesn't match" } )

class TeacherAPI(ViewSet):
	# create teacher by super admin
	def create(self, request):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1:
				serializers = Teacher_Serializer(data = request.data)

				if serializers.is_valid():
					serializers.save()
					return Response( { "Message" : "Teacher Added" } )

				return Response(serializers.errors)

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# get all teacher by super admin
	def list(self, request):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1:
				tchr = Teacher.objects.all()

				if not len(tchr):
					return Response( { "Message" : "Teacher Not Found" } )
		
				serializers = Teacher_Serializer(tchr, many = True)
		
				return Response(serializers.data)

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# get one teacher by super admin
	def retrieve(self, request, pk):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1:
				try:
					tchr = Teacher.objects.get(id = pk)
				except Teacher.DoesNotExist:
					return Response( { "Message" : "Teacher not found" } )

				serializers = Teacher_Serializer(tchr)

				return Response(serializers.data)

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# updtae full data of teacher by super admin
	def update(self, request, pk):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1:
				try:
					tchr = Teacher.objects.get(id = pk)
				except Teacher.DoesNotExist:
					return Response( { "Message" : "Teacher not found" } )

				serializers = Teacher_Serializer(tchr, data = request.data)
				
				if serializers.is_valid():
					return Response(serializers.data)
		
				return Response(serializers.errors)

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# updtae partial data of teacher by super admin
	def partial_update(self, request, pk):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1:
				try:
					tchr = Teacher.objects.get(id = pk)
				except Teacher.DoesNotExist:
					return Response( { "Message" : "Teacher not found" } )

				serializers = Teacher_Serializer(tchr, data = request.data, partial = True)
				
				if serializers.is_valid():
					return Response(serializers.data)
		
				return Response(serializers.errors)

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# delete teacher by super admin
	def destroy(self, request, pk):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1:
				try:
					tchr = Teacher.objects.get(phone = pk)
				except Teacher.DoesNotExist:
					return Response( { "Message" : "Teacher not found" } )
		
				tchr.delete()
		
				return Response( { "Message" : "Teacher deleted" } )

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

class StudentAPI(ViewSet):
	# create student by super admin and teacher
	def create(self, request):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1 or 2:
				serializers = Student_Serializer(data = request.data)

				if serializers.is_valid():
					serializers.save()
					return Response( { "Message" : "Student Added" } )

				return Response(serializers.errors)

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# get all student by super admin and teacher
	def list(self, request):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1 or 2:
				sdnt = Student.objects.all()

				if not len(sdnt):
					return Response( { "Message" : "Student Not Found" } )
		
				serializers = Student_Serializer(sdnt, many = True)
		
				return Response(serializers.data)

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# get one student by super admin and teacher
	def retrieve(self, request, pk):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1 or 2:
				try:
					sdnt = Student.objects.get(id = pk)
				except Student.DoesNotExist:
					return Response( { "Message" : "Student not found" } )

				serializers = Student_Serializer(sdnt)

				return Response(serializers.data)

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# updtae full data of student by super admin and teacher
	def update(self, request, pk):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1 or 2:
				try:
					sdnt = Student.objects.get(id = pk)
				except Student.DoesNotExist:
					return Response( { "Message" : "Student not found" } )

				serializers = Student_Serializer(sdnt, data = request.data)
				
				if serializers.is_valid():
					return Response(serializers.data)
		
				return Response(serializers.errors)

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# updtae partial data of student by super admin and teacher
	def partial_update(self, request, pk):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1 or 2:
				try:
					sdnt = Student.objects.get(id = pk)
				except Student.DoesNotExist:
					return Response( { "Message" : "Student not found" } )

				serializers = Student_Serializer(sdnt, data = request.data, partial = True)
				
				if serializers.is_valid():
					return Response(serializers.data)
		
				return Response(serializers.errors)

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# delete student by super admin and teacher
	def destroy(self, request, pk):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1 or 2:
				try:
					sdnt = Student.objects.get(phone = pk)
				except Student.DoesNotExist:
					return Response( { "Message" : "Student not found" } )
		
				sdnt.delete()
		
				return Response( { "Message" : "Student deleted" } )

			else:
				return Response( { "Message" : "User unauthorized" } )

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

class ProfileAPI(ViewSet):
	# get all 3 profile data
	def list(self, request):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1:
				sadm = Super_Admin.objects.get(phone = data['phone'])
				serializers = Super_Admin_Serializer(sadm)

				return Response(serializers.data)

			elif data['user_type'] == 2:
				tchr = Teacher.objects.get(phone = data['phone'])
				serializers = Teacher_Serializer(tchr)

				return Response(serializers.data)

			elif data['user_type'] == 3:
				sdnt = Student.objects.get(phone = data['phone'])
				serializers = Student_Serializer(sdnt)

				return Response(serializers.data)

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# updtae full data of all 3 profile
	def update(self, request, pk=None):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1:
				sadm = Super_Admin.objects.get(phone = data['phone'])

				serializers = Super_Admin_Serializer(sadm, data = request.data)
				
				if serializers.is_valid():
					return Response(serializers.data)
		
				return Response(serializers.errors)

			elif data['user_type'] == 2:
				tchr = Teacher.objects.get(phone = data['phone'])

				serializers = Teacher_Serializer(tchr, data = request.data)
				
				if serializers.is_valid():
					return Response(serializers.data)
		
				return Response(serializers.errors)

			elif data['user_type'] == 3:
				sdnt= Student.objects.get(phone = data['phone'])

				serializers = Student_Serializer(sdnt, data = request.data)
				
				if serializers.is_valid():
					return Response(serializers.data)
		
				return Response(serializers.errors)

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )

	# updtae partial data of all 3 profile
	def partial_update(self, request, pk=None):
		try:
			return_type, data = check_token(request.headers['token'])
		except KeyError:
			return Response( { "Message" : "Token missing" } )

		if return_type == 1:
			if data['user_type'] == 1:
				sadm = Super_Admin.objects.get(phone = data['phone'])

				serializers = Super_Admin_Serializer(sadm, data = request.data, partial = True)
				
				if serializers.is_valid():
					return Response(serializers.data)
		
				return Response(serializers.errors)

			elif data['user_type'] == 2:
				tchr = Teacher.objects.get(phone = data['phone'])

				serializers = Teacher_Serializer(tchr, data = request.data, partial = True)
				
				if serializers.is_valid():
					return Response(serializers.data)
		
				return Response(serializers.errors)

			elif data['user_type'] == 3:
				sdnt= Student.objects.get(phone = data['phone'])

				serializers = Student_Serializer(sdnt, data = request.data, partial = True)
				
				if serializers.is_valid():
					return Response(serializers.data)
		
				return Response(serializers.errors)

		elif return_type == 2:
			return Response( { "Message" : "Token invalid" } )

		elif return_type == 3:
			return Response( { "Message" : "Token expired" } )