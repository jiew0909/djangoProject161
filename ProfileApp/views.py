from django.shortcuts import render

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
    showName = "chiraporn chamkun"
    showAddress = "39 หมู่ 11 ต.กุดปลาดุก อ.เมือง จ.อำนาจเจริญ"
    showtel = "0969010112"
    showgender = "หญิง"
    showBirthday = "09 กันยายน 2544"
    showWeight = 55
    showHeight = 160
    showstatus = "นักศึกษา"
    showSchool = "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสานขอนแก่นวิทยาเขต"

    products = []

    product =['pro001','vans',1500.00]
    products.append(product)
    product =['pro002','Converse', 2400.00]
    products.append(product)
    product =['pro003','Nike',3200.00]
    products.append(product)
    product =['pro004','Adidas',1650.00]
    products.append(product)
    product =['pro005','keds', 2300.00]
    products.append(product)
    product = ['pro006', 'puna', 2500.00]
    products.append(product)
    product = ['pro007', 'New balance', 1300.00]
    products.append(product)
    product = ['pro008', 'onitsuka', 3000.00]
    products.append(product)
    product = ['pro009', 'Reebok', 2400.00]
    products.append(product)
    product = ['pro010', 'lacoste', 4300.00]
    products.append(product)

    context = {'showID':showID,'showName':showName,'showAddress':showAddress,'showtel':showtel,
               'showgender':showgender,'showBirthday':showBirthday,'showWeight':showWeight,'showHeight':showHeight,
               'showstatus':showstatus,'showSchool':showSchool, 'products':products}
    return render(request,'showMyData.html',context)






































