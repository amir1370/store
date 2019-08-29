from itertools import chain

from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView

from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.db.models import Q
import datetime

from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.urls import reverse_lazy, reverse

import jdatetime

from production.forms import ColoredSheetSearchForm
from .models import Product, Category
from django.forms import inlineformset_factory, formset_factory, modelformset_factory


# Create your views here.
def index(request):
    product_list = Product.objects.all()
    print(product_list)
    return render(request, 'production/index.html', {"product_list": product_list})


def category(request):
    product_list = Product.objects.all()
    print(product_list)
    return render(request, 'production/category.html', {"product_list": product_list})


class AboutView(TemplateView):
    template_name = "about_us.html"

class StaticTableView(TemplateView):
    template_name = "production/static_table.html"


class ContactView(TemplateView):
    template_name = "contact_us.html"


class CategoryListView(ListView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'slug', 'up_category', 'image']
    success_url = '/category-list/'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'slug', 'up_category', 'image']
    success_url = '/category-list/'


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'pk' in self.kwargs.keys():
            queryset = queryset.filter(category=Category.objects.get(id=self.kwargs['pk'])).order_by("brand", "thickness")
        if self.request.GET:
            queryset = self.filter_queryset(queryset)
        return queryset


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'slug', 'category', 'description', 'price', 'stock', 'available', 'length', 'width', 'thickness',
              'size', 'brand', 'color', 'color_code']

    def get_success_url(self):
        return reverse('product_list', kwargs={'pk': self.object.category.id})


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'slug', 'category', 'description', 'price', 'stock', 'available', 'length', 'width', 'thickness',
              'size', 'brand', 'color', 'color_code']

    def get_success_url(self):
        return reverse('product_list', kwargs={'pk': self.object.category.id})


def update_prices(request, category_id):
    ProductFormSet = modelformset_factory(Product, fields=('price',), extra=0)
    if request.method == "POST":
        formset = ProductFormSet(request.POST)
        print(formset)
        if formset.is_valid():
            formset.save()

        # Do something. Should generally end with a redirect. For example:
        for form in formset:
            print(form)

        return HttpResponseRedirect('/product-list/{}'.format(category_id))
    else:
        product_list = list(Product.objects.filter(category_id=category_id))
        formset = ProductFormSet(queryset=Product.objects.filter(category_id=category_id))
        # for form in formset:
            # print(form)
    return render(request, 'production/update_prices.html', {'formset': formset, "product_list": product_list})


@method_decorator(csrf_exempt, name='dispatch')
class SheetListView(ListView):
    model = Product
    template_name = 'production/sheet_list.html'

    def get_context_data(self, **kwargs):
        context = super(SheetListView, self).get_context_data(**kwargs)
        filter_dict = {}
        search_list = ['width', 'thickness']
        for item in search_list:
            filter_dict[item] = self.request.GET.get(item)

        context.update({"filter": filter_dict})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'pk' in self.kwargs.keys():
            queryset = queryset.filter(category=Category.objects.get(id=self.kwargs['pk'])).order_by("brand", "thickness")
        if self.request.GET:
            queryset = self.filter_queryset(queryset)
        return queryset

    def filter_queryset(self, queryset):
        filter_dict = {}
        search_list = ['width', 'thickness']

        for item in search_list:
            filter_dict[item] = self.request.GET.get(item)

        queryset = queryset.filter(
            width__icontains=filter_dict['width'],
            thickness__icontains=filter_dict['thickness'],
        )
        return queryset


@method_decorator(csrf_exempt, name='dispatch')
class ColoredSheetListView(ListView):
    model = Product
    template_name = 'production/colored_sheet_list.html'
    form_class = ColoredSheetSearchForm

    def get_context_data(self, **kwargs):
        context = super(ColoredSheetListView, self).get_context_data(**kwargs)
        filter_dict = {}
        search_list = ['width', 'thickness', 'color', 'color_code']
        print(self.form_class())
        for item in search_list:
            filter_dict[item] = self.request.GET.get(item)

        filter_dict["color"] = "" if not filter_dict["color"] else filter_dict["color"]

        print(filter_dict)
        context.update({"filter": filter_dict})
        # print(list(context["product_list"])[0].color)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'pk' in self.kwargs.keys():
            queryset = queryset.filter(category=Category.objects.get(id=self.kwargs['pk'])).order_by("brand", "thickness")
        if self.request.GET:
            queryset = self.filter_queryset(queryset)
        return queryset

    def filter_queryset(self, queryset):
        filter_dict = {}
        search_list = ['width', 'thickness', 'color', 'color_code']

        for item in search_list:
            filter_dict[item] = self.request.GET.get(item)

        if filter_dict['thickness']:
            queryset = queryset.filter(thickness=filter_dict['thickness'])

        if filter_dict["color_code"]:
            queryset = queryset.filter(color_code=filter_dict["color_code"])

        queryset = queryset.filter(
            width__icontains=filter_dict['width'],
            color__icontains=filter_dict["color"]
        )

        return queryset


class TrapeziusFormView(TemplateView):
    template_name = "production/trapezius_sheet.html"


class SineFormView(TemplateView):
    template_name = "production/sine_sheet.html"


class CheadleinFormView(TemplateView):
    template_name = "production/cheadlein_sheet.html"


class StaticProductListView(ListView):
    model = Product
    template_name = "production/static_table.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'pk' in self.kwargs.keys():
            queryset = queryset.filter(category=Category.objects.get(id=self.kwargs['pk'])).order_by("brand", "thickness")
        if self.request.GET:
            queryset = self.filter_queryset(queryset)
        return queryset
