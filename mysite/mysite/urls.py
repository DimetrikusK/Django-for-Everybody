from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('polls/', include('polls.urls')),
    path('hello/', include('home.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls'))
]
