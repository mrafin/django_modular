from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import permission_required
from django.conf import settings
from django.contrib.auth.decorators import login_required

@permission_required('sample_module.view_product', raise_exception=True)
def product_list(request):
    print(123)
    if 'sample_module' not in settings.INSTALLED_APPS:
        return render(request, 'sample_module/not_installed.html')
     
    products = Product.objects.all()
    field_names = [field.name for field in Product._meta.fields if field.name != "id"]
    # print("masukkkkkkkkkkkkkkkkk")
    return render(request, 'sample_module/list.html', {'products': products, "field_names":field_names})

# @login_required
@permission_required('sample_module.add_product', raise_exception=True)
def product_add(request):
    # print("masukkkkkkkkkkkkkkkkk111111111111")
    if 'sample_module' not in settings.INSTALLED_APPS:
        return render(request, 'sample_module/not_installed.html')
    
    form = ProductForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('product_list')
    return render(request, 'sample_module/form.html', {'form': form})

@permission_required('sample_module.change_product', raise_exception=True)
def product_edit(request, pk):
    if 'sample_module' not in settings.INSTALLED_APPS:
        return render(request, 'sample_module/not_installed.html')
    
    prod = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=prod)
    if form.is_valid(): form.save(); return redirect('product_list')
    return render(request, 'sample_module/form.html', {'form': form})

@permission_required('sample_module.delete_product', raise_exception=True)
def product_delete(request, pk):
    if 'sample_module' not in settings.INSTALLED_APPS:
        return render(request, 'sample_module/not_installed.html')
    
    prod = get_object_or_404(Product, pk=pk)
    prod.delete()
    return redirect('product_list')