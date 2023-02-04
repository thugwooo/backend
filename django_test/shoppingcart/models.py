from django.db import models
from product.models import Product
from user.models import User
# Create your models here.

class Shoppingcart(models.Model):
    s_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(Product, on_delete= models.CASCADE)
    u_id = models.ForeignKey(User, on_delete= models.CASCADE)
    s_count = models.IntegerField(default=1)

    def inputShoppingcart(request):
        cart_info = Shoppingcart()
        cart_info.u_id = User.objects.get(u_id = int(request.POST['u_id']))
        cart_info.p_id = Product.objects.get(p_id = int(request.POST['p_id']))
        return cart_info
    
