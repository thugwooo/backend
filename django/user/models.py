from ast import Delete
from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_strid = models.CharField(max_length=30)
    u_pw = models.CharField(max_length=20)
    u_name = models.CharField(max_length=20)
    u_phone = models.CharField(max_length=20, blank=True)
    u_date = models.DateTimeField(auto_now_add = True)
    u_drop = models.BooleanField(default=False) #탈퇴여부

    def __str__(self):
        return self.u_name

    def registerUser(request):
        user_info = User()
        user_info.u_strid = request.POST['u_strid']
        user_info.u_pw = request.POST['u_pw']
        user_info.u_name = request.POST['u_name']

        return user_info

class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=20)
    pet_type = models.CharField(max_length=20, default='강아지')
    pet_breed =models.CharField(max_length=20)
    pet_bcs = models.CharField(max_length=10)
    pet_birthYear = models.CharField(max_length=10)
    pet_birthMonth = models.CharField(max_length=10)
    pet_birthDay = models.CharField(max_length=10)
    pet_weight = models.CharField(max_length=10)
    pet_sex = models.CharField(max_length=10)
    pet_neu = models.CharField(max_length=10)
    pet_alg = ArrayField(models.CharField(max_length=20),default=list)
    pet_health = ArrayField(models.CharField(max_length=20),default=list)
    pet_petfood = ArrayField(models.CharField(max_length=20),default=list)

    def __str__(self):
        return self.pet_name
    
    def inputPet(request):
        pet_info = Pet()
        pet_info.u_id = User.objects.get(u_id = int(request.POST['u_id']))
        pet_info.pet_name = request.POST['pet_name']
        pet_info.pet_type = request.POST['pet_type']
        pet_info.pet_breed = request.POST['pet_breed']
        pet_info.pet_bcs = request.POST['pet_bcs']
        pet_info.pet_birthYear = request.POST['pet_birthYear']
        pet_info.pet_birthMonth = request.POST['pet_birthMonth']
        pet_info.pet_birthDay = request.POST['pet_birthDay']
        pet_info.pet_weight = request.POST['pet_weight']
        pet_info.pet_sex = request.POST['pet_sex']
        pet_info.pet_neu = request.POST['pet_neu']
        pet_info.pet_alg = request.POST['pet_alg']
        pet_info.pet_health = request.POST['pet_health']
        pet_info.pet_petfood = request.POST['pet_petfood']
        return pet_info

