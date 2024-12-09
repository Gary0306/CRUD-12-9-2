from django.shortcuts import render, redirect, get_object_or_404
from .form import ProductForm
from .models import Product


def index(request):
    if request.POST:
        form = ProductForm(request.POST)
        form.save()
        return redirect("products:index")
    products = Product.objects.order_by("-id")
    return render(request, "products/index.html", {"products": products})


def new(request):
    form = ProductForm()
    return render(request, "products/new.html", {"form": form})


def show(request, id):
    product = get_object_or_404(Product, id=id)
    if request.POST:
        form = ProductForm(request.POST, instance=product)
        form.save()
        return redirect("products:show", id=product.id)
    return render(request, "products/show.html", {"product": product})


def edit(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)
    return render(request, "products/edit.html", {"product": product, "form": form})


def delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.POST:
        product.delete()
        return redirect("products:index")
    return render(request, "products/delete.html", {"product": product})
