from django.urls import path, include
from django.contrib import admin

#from django.conf import settings
#from django.conf.urls.static import static
#Выключены, потому что некорректно работают

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
#] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT))