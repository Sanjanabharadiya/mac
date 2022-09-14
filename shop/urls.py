
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="shop"),
    path('about/',views.about, name="aboutus"),
    path('contact/',views.contact, name="contactus"),
    path('tracker/',views.tracker, name="trackingstatus"),
    path('productview/',views.prodview, name="productview"),
    path('checkout/',views.checkout, name="checkout"),
   
   
    
    
    
    
    
    
    
 ]
 