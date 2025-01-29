from django.contrib import admin
from django.urls import path, include

# from cruduser.views import Home

urlpatterns = [
    # path('', Home.as_view(), name='home'),  # Default path for the home page
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('myblogapp/', include('myblogapp.urls')),
    path('users/', include('users.urls')), 
    path('cruduser/', include('cruduser.urls'))
]
