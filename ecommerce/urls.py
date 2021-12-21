from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        #Leave as empty string for base url
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order")


]

#if settings.DEBUG:
#	urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATICFILES_DIR)    
#	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)