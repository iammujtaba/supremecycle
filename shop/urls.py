from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='HomePage'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('productview/<int:myid>',views.productView,name="ProductView"),
    path('checkout/',views.checkout,name='Checkout'),
    path('handlerequest/',views.handlerequest,name='Handle Request'),
]