from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import *
from .forms import OrderForm, CustomerForm
from .filters import OrderFilter

# Create your views here.

def home(request):
    orders =OrderMod.objects.all()
    customers = CustomerMod.objects.all()
    
    total_cutomers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status = "Delivered").count()

    pending = orders.filter(status = "Pending").count()

    context = {
        'orders':orders,
        'customers':customers,
        'total_cutomers':total_cutomers,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending
        }
    return render(request,'accounts/dashboard.html',context)

def product(request):
    products = ProductMod.objects.all()
    return render(request,'accounts/products.html',{'products':products})

def customer(request,pk_test):
    customer = CustomerMod.objects.get(id=pk_test)
    orders = customer.ordermod_set.all()
    total_orders = orders.count()

    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs
    context = {'customer':customer,'orders':orders,'total_orders':total_orders,'myFilter':myFilter}
    return render(request,'accounts/customer.html',context)

#Form Creation.
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(CustomerMod,OrderMod,fields=('product','status'), extra = 10)
    customer = CustomerMod.objects.get(id=pk)
    formset = OrderFormSet(queryset= OrderMod.objects.none(),instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    content ={'formset':formset}
    return render(request,'accounts/order_form.html',content)

#Update Form.
def updateOrder(request,pk):
    order = OrderMod.objects.get(id = pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    content ={'form':form}
    return render(request,'accounts/order_form.html',content)


#Delete Form.
def deleteOrder(request,pk):
    order = OrderMod.objects.get(id = pk)
    context = {'item':order}
    if request.method == "POST":
        order.delete()
        return redirect('/')
    return render(request,'accounts/delete.html',context)

def createCustomer(request):
    form = CustomerForm
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'accounts/Create_customer.html',context)


