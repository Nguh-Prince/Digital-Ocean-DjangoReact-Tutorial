from django.contrib import admin
from django.urls import path
from customers import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/customers/', views.customers_list),
    path('api/customers/<int:pk>', views.customers_detail),
]
