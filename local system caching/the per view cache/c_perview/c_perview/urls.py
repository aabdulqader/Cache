from django.contrib import admin
from django.urls import path, include
from enroll.views import home, contact

# from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

    # path('', cache_page(30)(home), name = 'home'),
    path('contact/', contact),

]
