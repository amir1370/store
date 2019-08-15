"""simorgh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^category/$', views.category),
    url(r'^about/$', views.AboutView.as_view(), name='about_us'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact_us'),
]
# category
urlpatterns += [
    url(r'^category-list/$', views.CategoryListView.as_view(), name='category_list'),
    url(r'^category/(?P<pk>[0-9]+)/edit$', views.CategoryUpdateView.as_view(), name='edit_category'),
    url(r'^category/create$', views.CategoryCreateView.as_view(), name='create_category'),
    url(r'^category/update-prices/(?P<category_id>[0-9]+)$', views.update_prices, name='update_prices')
]
# product
urlpatterns += [
    url(r'^product-list/(?P<pk>[0-9]+)$', views.ProductListView.as_view(), name='product_list'),
    url(r'^product/(?P<pk>[0-9]+)/edit$', views.ProductUpdateView.as_view(), name='edit_product'),
    url(r'^product/create$', views.ProductCreateView.as_view(), name='create_product'),
    url(r'^محصولات/ورق/(?P<pk>[0-9]+)$', views.SheetListView.as_view(), name='sheet_list'),
]
# form
urlpatterns += [
    url(r'^product/form/trapezius$', views.TrapeziusFormView.as_view(), name='trapezius_form'),
    url(r'^product/form/sine$', views.SineFormView.as_view(), name='sine_form'),
    url(r'^product/form/cheadlein$', views.CheadleinFormView.as_view(), name='cheadlein_form'),
]
