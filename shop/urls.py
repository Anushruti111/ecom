from django.urls import path
from . import views
from . models import Product

# from django.views.static import serve
# from django.conf.urls import url
# 
urlpatterns = [
    path("", views.index, name="shop"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
#     url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}),
#     url(r'^static/(?P<path>.*)$', serve,{'document_root':  settings.STATIC_ROOT}),
]


