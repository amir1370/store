from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='نام دسته')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    up_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='category', null=True, blank=True, verbose_name='عکس')

    class Meta:
        ordering = ('name',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='دسته',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name='نام')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='نام لاتین')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت', null=True, blank=True)
    stock = models.PositiveIntegerField(verbose_name='مقدار موجودی', null=True, blank=True)
    available = models.BooleanField(default=True, verbose_name='موجود')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    length = models.FloatField(verbose_name='طول', null=True, blank=True)
    width = models.FloatField(verbose_name='عرض', null=True, blank=True)
    thickness = models.FloatField(verbose_name='ضخامت', null=True, blank=True)
    size = models.CharField(max_length=100, verbose_name='سایز', null=True, blank=True)
    brand = models.CharField(max_length=100, verbose_name='برند')
    color = models.CharField(max_length=200, verbose_name='رنگ', null=True, blank=True)
    color_code = models.CharField(max_length=200, verbose_name='کد رنگ', null=True, blank=True)
    standard = models.CharField(max_length=200, verbose_name='استاندارد', null=True, blank=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name
