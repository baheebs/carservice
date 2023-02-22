from django.shortcuts import render,redirect
from backend.models import customer,carcategory,serdetails,msgdb,appointmentdb,cartdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def ind(request):
    return render(request,"index.html")

def adminpg(req):
    return render(req,"addadmin.html")

def savedata(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pas = request.POST.get('password')
        Con = request.POST.get('contactnumber')
        Em = request.POST.get('email')
        Us = request.POST.get('username')
        Img = request.FILES['image']
        obj = customer(Name=na, Contactnumber=Con, password=pas, Email=Em,username=Us,Image=Img)
        obj.save()
        return redirect(adminpg)

def displaypg(request):
    data = customer.objects.all()
    return render(request,"display.html",{'data':data})

def deletedata(req,dataid):
    data = customer.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypg)

def editadminpg(request,dataid):
    data = customer.objects.get(id=dataid)
    print(data)
    return render(request,"editadmin.html",{'data':data})

def updatedata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        pas = request.POST.get('password')
        Con = request.POST.get('contactnumber')
        Em = request.POST.get('email')
        Us = request.POST.get('username')
        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = customer.objects.get(id=dataid).Image
        customer.objects.filter(id=dataid).update(Name=na, Contactnumber=Con, password=pas, Email=Em,username=Us,Image=file)
        return redirect(displaypg)
def addcatpg(req):
    return render(req,"addcat.html")

def savecat(request):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        Img = request.FILES['image']
        obj = carcategory(Name=na,Desc=de, Image=Img)
        obj.save()
        return redirect(addcatpg)

def discatpg(request):
    data = carcategory.objects.all()
    return render(request,"discat.html",{'data':data})

def deletecatdata(req,dataid):
    data = carcategory.objects.filter(id=dataid)
    data.delete()
    return redirect(discatpg)

def editcatpg(request,dataid):
    data = carcategory.objects.get(id=dataid)
    print(data)
    return render(request,"editcat.html",{'data':data})

def updatecatdata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = carcategory.objects.get(id=dataid).Image
        carcategory.objects.filter(id=dataid).update(Name=na,Desc=de,Image=file)
        return redirect(discatpg)

def addserpg(req):
    data = carcategory.objects.all()
    return render(req,"addser.html",{'data':data})

def saveser(request):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        sm = request.POST.get('selmod')
        sf = request.POST.get('selful')
        mf = request.POST.get('manf')
        pr = request.POST.get('price')
        qu = request.POST.get('tity')
        ca = request.POST.get('category')
        Img = request.FILES['image']
        quan = request.POST.get('quantity')
        obj = serdetails(Name=na,Desc=de,price=pr,phone=qu,category=ca,Image=Img,selcar=sm,fuel=sf,manfact=mf,QUANTITY=quan)
        obj.save()
        return redirect(addserpg)

def disserpage(request):
    data = serdetails.objects.all()
    return render(request,"disser.html",{'data':data})

def deleteprodata(req,dataid):
    data = serdetails.objects.filter(id=dataid)
    data.delete()
    return redirect(disserpage)

def editserpage(request,dataid):
    data = serdetails.objects.get(id=dataid)
    da = carcategory.objects.all()
    print(data)
    return render(request,"editser.html",{'data':data, 'da':da})

def updateprodata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        sm = request.POST.get('selmod')
        sf = request.POST.get('selful')
        mf = request.POST.get('manf')
        pr = request.POST.get('price')
        qu = request.POST.get('tity')
        ca = request.POST.get('category')
        quan = request.POST.get('quantity')

        try:
            Img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(Img.name,Img)
        except MultiValueDictKeyError:
            file = serdetails.objects.get(id=dataid).Image
        serdetails.objects.filter(id=dataid).update(Name=na,Desc=de,price=pr,phone=qu,category=ca,Image=file,selcar=sm,fuel=sf,manfact=mf,QUANTITY=quan)
        data = carcategory.objects.all()
        return redirect(disserpage)

def loginpage(request):
    return render(request,"login.html")




def adminlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if customer.objects.filter(username=username_r, password=password_r).exists():
            req.session['username'] = username_r
            req.session['password'] = password_r
            return redirect(ind)
        else:
            return render(req, "login.html")




def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

def displaycontact(request):
    data = msgdb.objects.all()
    return render(request,"dismsg.html",{'data':data})

def deletecntdata(req,dataid):
    data = msgdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontact)

def displaybook(request):
    data =appointmentdb.objects.all()
    return render(request, "displaybook.html", {'data': data})
def Deletebook(req, dataid):
    data = appointmentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaybook)

def discartpg(request):
    data =cartdb.objects.all()
    return render(request, "displaycart.html", {'data': data})
def Deletecart(req, dataid):
    data = cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(discartpg)