from django.urls import path
from frontend import views

urlpatterns =[
    path('',views.newpg,name="newpg"),
    path('abtpage/',views.abtpage,name="abtpage"),
    path('cntpage/',views.cntpage,name="cntpage"),
    path('prodis/<itemcatg>',views.prodis,name="prodis"),
    path('singpro/<int:dataid>/',views.singpro,name="singpro"),
    path('contct/', views.contct, name="contct"),
    path('logpage/',views.logpage,name="logpage"),
    path('saveregister/', views.saveregister, name="saveregister"),
    path('customerloginpage/', views.customerloginpage, name="customerloginpage"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('washpg/',views.washpg,name="washpg"),
    path('savecartpage/', views.savecartpage, name="savecartpage"),
    path('viewcartpage/', views.viewcartpage, name="viewcartpage"),
    path('deletecartfont/<int:dataid>/', views.deletecartfont, name="deletecartfont"),
    path('appointment/', views.appointment, name="appointment"),
    path('savebookdb/', views.savebookdb, name="savebookdb"),
]