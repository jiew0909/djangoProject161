from django.shortcuts import render,redirect

def home(request):
    return render(request, 'home.html')
def personal(request):
    return render(request, 'personal.html')
def educational(request):
    return render(request, 'educational.html')
def interests(request):
    return render(request, 'interests.html')
def sale(request):
    return render(request, 'sale.html')
def rolemodel(request):
    return render(request, 'rolemodel.html')

def showMyData(request):
    showID = '65342310161-9'
    showName = "จิระพร  ชำกุล"
    showAddress = "39 หมู่ 11 ต.กุดปลาดุก อ.เมือง จ.อำนาจเจริญ"
    showtel = "0969010112"
    showgender = "หญิง"
    showBirthday = "09 กันยายน 2544"
    showWeight = 55
    showHeight = 160
    showstatus = "นักศึกษา"
    showSchool = "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน วิทยาเขตขอนแก่น"

    products = []

    product =['vans',3500.00,'../../static/images/vans.png']
    products.append(product)
    product =['Converse', 3400.00,'../../static/images/conver.png']
    products.append(product)
    product =['Nike',3500.00,'../../static/images/nike.png']
    products.append(product)
    product =['Adidas',1650.00,'../../static/images/adidas.png']
    products.append(product)
    product =['keds', 3210.00,'../../static/images/kede.png']
    products.append(product)
    product = [ 'puna', 2500.00,'../../static/images/puma.png']
    products.append(product)
    product = ['New balance', 1600.00,'../../static/images/new.png']
    products.append(product)
    product = [ 'onitsuka', 3150.00,'../../static/images/oski.png']
    products.append(product)
    product = [ 'Reebok', 999.00,'../../static/images/rebook.png']
    products.append(product)
    product = [ 'lacoste', 1900.00,'../../static/images/จระเข้.png']
    products.append(product)

    context = {'showID':showID,'showName':showName,'showAddress':showAddress,'showtel':showtel,
               'showgender':showgender,'showBirthday':showBirthday,'showWeight':showWeight,'showHeight':showHeight,
               'showstatus':showstatus,'showSchool':showSchool, 'products':products}
    return render(request,'showMyData.html',context)


lstOurProduct = []

from ProfileApp.models import *
from ProfileApp.forms import *

def listProduct(request):
    context = {'products': lstOurProduct}
    return render(request, 'listProduct.html', context)

def inputProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            brand = form.get('brand')
            model = form.get('model')
            color = form.get('color')
            type = form.get('type')
            price = form.get('price')

            if price <= 5000:
                discount = 0.05
            else:
                discount = 0.10

            vat = price * 0.07
            net = price - (price * discount) + vat
            pd = Product(id, brand, model, color, type, price, discount, vat, net)
            lstOurProduct.append(pd)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
        context = {'form': form}
        return render(request,'inputProduct.html', context)






































