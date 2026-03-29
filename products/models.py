from django.db import models
from django.contrib.auth.models import User


# ----------------------------------------------------------------------------------------
# Clase Categoría
# ----------------------------------------------------------------------------------------

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# ----------------------------------------------------------------------------------------
# Clase Producto
# ----------------------------------------------------------------------------------------

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)


    def __str__(self):
        return self.name

# # ------------------------------------------------------------------------------
# #  Función Formato Precio clp
# # ------------------------------------------------------------------------------

#     @property
#     def price_format(self):
#         return f'${self.price:,.0f}'.replace(',','.')


# ----------------------------------------------------------------------------------------
# Clase Carrito
# ----------------------------------------------------------------------------------------

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantify = models.IntegerField(default=1)


# ----------------------------------------------------------------------------------------
# Clase Compra
# ----------------------------------------------------------------------------------------

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


