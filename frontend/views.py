from django.shortcuts import render,redirect
from backend.models import carcategory,serdetails,msgdb,cartdb,appointmentdb
from frontend.models import registerdb


from django.contrib import messages
# Create your views here.

def newpg(request):
    data = carcategory.objects.all()
    return render(request, "newpage.html",{'data' : data})

def abtpage(request):
    data = carcategory.objects.all()
    return render(request,"about.html",{'data' : data})

def prodis(request,itemcatg):
    print("===itemcatg===",itemcatg)
    catg = itemcatg.upper()
    products=serdetails.objects.filter(category  =itemcatg)
    context={
        'products':products,
        'catg':catg
    }
    return render(request,"prodisplay.html",context)

def singpro(request,dataid):
    data = serdetails.objects.get(id=dataid)
    return render(request,"singprod.html",{'dat':data})

def cntpage(request):
    return render(request,"contact.html")

def contct(request):
    if request.method == "POST":
        na = request.POST.get('nam2')
        Em = request.POST.get('mail2')
        su = request.POST.get('subj')
        Ms = request.POST.get('message')
        obj = msgdb(name=na, messge=Ms, sub=su, mail=Em)
        obj.save()
        messages.success(request, "Thank you for your valuable Feedback and queries")
        return redirect(cntpage)


def logpage(request):
    return render(request,"loginout.html")

def saveregister(request):
    if request.method == "POST":
        na = request.POST.get('nam1')
        Em = request.POST.get('mail1')
        pas = request.POST.get('pass1')
        Con = request.POST.get('conpass')
        obj = registerdb(name=na, conpassword=Con, password=pas, mail=Em)
        obj.save()
        messages.success(request,"register successfully")
        return redirect(logpage)

def customerloginpage(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if registerdb.objects.filter(name=username_r,password=password_r).exists():
            request.session['username']=username_r
            request.session['password']=password_r
            messages.success(request,"login successfully")
            return  redirect(newpg)

        else:
            messages.error(request,"invalid user")
    return render(request,'loginout.html')

def userlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"logout successfully")
    return redirect(logpage)

def washpg(req):
    return render(
        req,"wash.html")

def savecartpage(req):
    if req.method == "POST":
        pna = req.POST.get('productname')
        cat = req.POST.get('productcat')
        qty = req.POST.get('quantity')
        tprice = req.POST.get('price')
        obj = cartdb( PDCTNAME=pna, CATEGORY=cat, QUANTITY=qty, PRIZE=tprice)
        obj.save()
        return redirect(newpg)



def viewcartpage(req):
    data = cartdb.objects.all()
    return render(req,"cart.html",{'data':data})

def deletecartfont(req,dataid):
    data = cartdb.objects.get(id=dataid)
    data.delete()
    return redirect(viewcartpage)

def appointment(request):
    data =cartdb.objects.all()
    return render(request, "book.html", {'data': data})
def savebookdb(req):
    if req.method == "POST":
        na = req.POST.get('name')
        eml = req.POST.get('email')
        dep = req.POST.get('enquiry')
        num = req.POST.get('number')
        dt = req.POST.get('date')
        tm = req.POST.get('time')
        qn = req.POST.get('quantity')
        lc = req.POST.get('loc')
        py = req.POST.get('paym')
        obj=appointmentdb(Name=na,Emailadress=eml,proddb=dep,Phonenumber=num,Date=dt,Time=tm,QUANTITY=qn,LOCATION=lc,PAYMENT=py)
        obj.save()
        messages.success(req, "booked successfully and our Executive will Contact you soon")
        return redirect(newpg)