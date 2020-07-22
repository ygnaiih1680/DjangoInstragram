from django.contrib import admin
from django.urls import path
from page import views
# media
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('profile/<int:content_id>', views.detail, name="detail")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
