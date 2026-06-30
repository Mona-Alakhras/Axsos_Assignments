from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from .models import Product, Order

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)

def buy(request):
    if request.method == "POST":
        quantity = int(request.POST['quantity'])
        product_id = request.POST['product_id'] # نعتمد على الـ ID وليس السعر المخفي
        
        product = get_object_or_404(Product, id=product_id)
        
        current_charge = product.price * quantity
        
        Order.objects.create(
            quantity_ordered=quantity,
            total_price=current_charge
        )
        
        request.session['current_charge'] = float(current_charge)
        
        return redirect('/amadon/checkout')
    return redirect('/amadon')

def checkout(request):
    stats = Order.objects.aggregate(
        total_items=Sum('quantity_ordered'),
        total_spent=Sum('total_price')
    )
    
    context = {
        'current_charge': request.session.get('current_charge', 0),
        'total_items': stats['total_items'] or 0,
        'total_spent': stats['total_spent'] or 0
    }
    return render(request, 'checkout.html', context)