from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Add a simple homepage view
def homepage(request):
    return HttpResponse("Welcome to the E-Commerce site!")

urlpatterns = [
    path('', homepage, name='homepage'),  # This is the root URL
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
]
