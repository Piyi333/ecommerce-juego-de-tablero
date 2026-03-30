from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# ------------------------------------------------------------------------------
#  Función para listar productos
# ------------------------------------------------------------------------------

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products' : products})


# ------------------------------------------------------------------------------
#  Función para crear productos
# ------------------------------------------------------------------------------

@login_required
def product_create(request):
    if not request.user.is_superuser:
        return redirect('product_list')
    
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        messages.success(request, 'El producto ha sido creado correctamente')
        return redirect('product_list')
    
    return render(request, 'products/form.html', {'form' : form})


# ------------------------------------------------------------------------------
#  Función para editar productos
# ------------------------------------------------------------------------------

@login_required
def product_edit(request, id):
    if not request.user.is_superuser:
        return redirect('product_list')
    
    product = get_object_or_404(Product, id=id)

    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid():
        form.save()
        messages.success(request, 'El producto ha sido actualizado con éxito')
        return redirect ('product_list')
    
    return render(request, 'products/form.html', {'form' : form})


# ------------------------------------------------------------------------------
#  Función para eliminar productos
# ------------------------------------------------------------------------------

@login_required
def product_delete(request, id):
    if not request.user.is_superuser:
        return redirect('product_list')
    
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'El producto ha sido eliminado con éxito')
        return redirect('product_list')
    
    return render(request, 'products/delete.html', {'product' : product})

    
# ------------------------------------------------------------------------------
#  Función para ver productos en carrito 
# ------------------------------------------------------------------------------

@login_required
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total_cart = 0 

    for product_id, quantity in cart.items():
        
        product = get_object_or_404(Product, id=int(product_id))
        
        
        subtotal = product.price * quantity
        
        
        total_cart += subtotal

        items.append({
            'product': product,
            'quantity': quantity,
            'total': subtotal
        })

   
    return render(request, 'products/cart.html', {
        'items': items, 
        'total_cart': total_cart
    })


# ------------------------------------------------------------------------------
#  Función para agregar productos al carrito
# ------------------------------------------------------------------------------

@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    messages.success(request, 'Producto añadido al carrito')

    return redirect('product_list') 


# ------------------------------------------------------------------------------
#  Función para eliminar productos del carrito
# ------------------------------------------------------------------------------

@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]
        messages.success(request, 'Producto eliminado del carrito')

    request.session['cart'] = cart

    return redirect('cart')



# ------------------------------------------------------------------------------
#  Función Compra
# ------------------------------------------------------------------------------


@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.warning(request, 'El carrito está vacío')
        return redirect('product_list')

    order = Order.objects.create(user=request.user)

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id))

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )



# ------------------------------------------------------------------------------
#  Vaciar carrito
# ------------------------------------------------------------------------------

    request.session['cart'] = {}

    messages.success(request, 'Compra realizada con éxito')

    return redirect('product_list')

