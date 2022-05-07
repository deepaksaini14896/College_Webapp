from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router =  DefaultRouter()

# super admin api's
router.register('register/super_admin', views.RegisterSuperAdminAPI, basename='RegisterSuperAdminAPI')
router.register('login/super_admin', views.LoginSuperAdminAPI, basename='LoginSuperAdminAPI')
router.register('add/teacher', views.TeacherAPI, basename='TeacherAPI')

# teacher api's
router.register('register/teacher', views.RegisterTeacherAPI, basename='RegisterTeacherAPI')
router.register('login/teacher', views.LoginTeacherAPI, basename='LoginTeacherAPI')

# student api's
router.register('register/student', views.RegisterStudentAPI, basename='RegisterStudentAPI')
router.register('login/student', views.LoginStudentAPI, basename='LoginStudentAPI')

# super admin, teacher and student api's
router.register('profile', views.ProfileAPI, basename='ProfileAPI')

# super admin and teacher api's
router.register('add/student', views.StudentAPI, basename='StudentAPI')

urlpatterns = [
	path('', include(router.urls))
]