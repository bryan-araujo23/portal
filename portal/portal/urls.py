"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('contas/', include('contas.urls')),  
    path('perfil/', include('perfil.urls')),
    path('', include('post.urls')), 
    

    # Template Static
    path('about/', TemplateView.as_view(template_name='fixo/about.html'), name='about'),
    path('como-usar/', TemplateView.as_view(template_name='fixo/howtouse.html'), name='howtouse'),
    path('faq/', TemplateView.as_view(template_name='fixo/faq.html'), name='faq'),
    path('contato/', TemplateView.as_view(template_name='fixo/contact.html'), name='contact'), 

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
