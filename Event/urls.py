from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings  

urlpatterns = [
    path('',views.home,name='home'),
   
    path('plan/',views.plan,name='plan'),
    path('blog/',views.blog,name='blog'),
    path('login/',views.user_login,name='login'),
    path('signin/',views.signin,name='signin'),
    path('feedback/',views.feedback,name='feedback'),
    path('logout/', views.user_logout, name='logout'), 
    path('booking/', views.booking, name='booking'), 
    path('payment/', views.payment, name='payment'), 
    path('chatbot',views.chatbot,name='chatbot'),
     
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
