from django.urls import path
from backend import views

urlpatterns =[
    path('ind/',views.ind,name="ind"),
    path('adminpg/',views.adminpg,name="adminpg"),
    path('savedata/',views.savedata, name="savedata"),
    path('displaypg/',views.displaypg, name="displaypg"),
    path('deletedata/<int:dataid>/', views.deletedata, name="deletedata"),
    path('editadminpg/<int:dataid>/',views.editadminpg, name="editadminpg"),
    path('updatedata/<int:dataid>/',views.updatedata, name="updatedata"),
    path('addcatpg/',views.addcatpg,name="addcatpg"),
    path('savecat/', views.savecat, name="savecat"),
    path('discatpg/', views.discatpg, name="discatpg"),
    path('deletecatdata/<int:dataid>/', views.deletecatdata, name="deletecatdata"),
    path('editcatpg/<int:dataid>/', views.editcatpg, name="editcatpg"),
    path('updatecatdata/<int:dataid>/', views.updatecatdata, name="updatecatdata"),
    path('addserpg/',views.addserpg,name="addserpg"),
    path('saveser/', views.saveser, name="saveser"),
    path('disserpage/', views.disserpage, name="disserpage"),
    path('deleteprodata/<int:dataid>/', views.deleteprodata, name="deleteprodata"),
    path('editserpage/<int:dataid>/', views.editserpage, name="editserpage"),
    path('updateprodata/<int:dataid>/', views.updateprodata, name="updateprodata"),
    path('loginpage/',views.loginpage, name="loginpage"),
    path('adminlogin/',views.adminlogin, name="adminlogin"),
    path('adminlogout/',views.adminlogout, name="adminlogout"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecntdata/<int:dataid>/', views.deletecntdata, name="deletecntdata"),
    path('displaybook/', views.displaybook, name="displaybook"),
    path('Deletebook/<int:dataid>/', views.Deletebook, name="Deletebook"),
    path('discartpg/', views.discartpg, name="discartpg"),
    path('Deletecart/<int:dataid>/', views.Deletecart, name="Deletecart")

]