from django.db import models
from user.models import User
from product.models import Product

# Create your models here.


class UserOrder(models.Model):  
    u_id = models.ForeignKey(User, on_delete=models.CASCADE) #유저 pk값
    uo_id = models.AutoField(primary_key = True)
    uo_date = models.DateTimeField(auto_now_add = True)
    uo_status = models.CharField(max_length = 20, default = '주문') # 배송중, 배송완료


class UserOrderDetail(models.Model):
    uod_id = models.AutoField(primary_key=True)
    uo_id = models.ForeignKey(UserOrder, on_delete = models.CASCADE)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1) # 이건 없어도 될듯
    p_id = models.ForeignKey(Product, on_delete= models.CASCADE)
    uod_quantity = models.IntegerField(default=1)
    uod_date = models.DateTimeField(auto_now_add = True, blank=True)




class UserRefund(models.Model):
    ur_id = models.AutoField(primary_key= True)
    uod_id = models.ForeignKey(UserOrderDetail, on_delete=models.CASCADE)
    ur_reason = models.CharField(max_length=300)


# class NonUserOrder(models.Model):
#     nuo_id = models.AutoField(primary_key=True)
#     nuo_date = models.DateTimeField(auto_now_add= True)
#     nuo_address1 = models.CharField(max_length=20) #우편번호
#     nuo_address1 = models.CharField(max_length=50) #주소
#     nuo_address1 = models.CharField(max_length=50) #상세주소
#     nuo_name = models.CharField(max_length=20)
#     num_phone = models.CharField(max_length=20)

# class NonUserOrderDetail(models.Model):
#     nuod_id = models.AutoField(primary_key=True)
#     nuo_id = models.ForeignKey(NonUserOrder, on_delete=models.CASCADE)
#     p_id = models.ForeignKey(Product, on_delete= models.CASCADE)
#     nuod_count = models.IntegerField(default=1)
#     nuod_status = models.CharField(max_length=10, default='주문') # 현재 상태

# class UserRefund(models.Model):
#     nur_id = models.AutoField(primary_key= True)
#     nuod_id = models.ForeignKey(NonUserOrderDetail, on_delete=models.CASCADE)
#     nur_reason = models.CharField(max_length=300)
    
