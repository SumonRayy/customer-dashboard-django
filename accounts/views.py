from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import OrderForm, CreateUserForm

# Create your views here.


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)

            return redirect("login")

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def loginPage(request):
    form = CreateUserForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    context = {
        "orders": orders,
        "customers": customers,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "delivered": delivered,
        "pending": pending,
    }
    return render(request, "accounts/dashboard.html", context)


def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {"products": products})


def contact(request):
    return render(request, "accounts/about.html")


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {"customer": customer, "orders": orders, "order_count": order_count}
    return render(request, "accounts/customer.html", context)


def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={"customer": customer})
    if request.method == "POST":
        # print("Printing POST:", request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


def updateOrder(request, pk_up):
    order = Order.objects.get(id=pk_up)
    form = OrderForm(instance=order)
    if request.method == "POST":
        # print("Printing POST:", request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


def deleteOrder(request, pk_del):
    order = Order.objects.get(id=pk_del)
    if request.method == "POST":
        order.delete()
        return redirect("/")

    context = {"item": order}
    return render(request, "accounts/delete.html", context)
