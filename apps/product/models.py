# apps/product/models.py

# Django modules
from django.db import models

# Create your models here.

# class name:Category
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(
    	max_length=255, 
    	blank=False,
    	help_text='Field ini tidak boleh dikosongkan.')
    url_slug=models.CharField(
    	max_length=255,
    	help_text='Field ini pre-populated diambil dari title.')
    thumbnail=models.FileField(
    	blank=True,
    	help_text='Field untuk foto produk kategori.')
    description=models.TextField(
    	blank=True,
    	help_text='Field untuk deskripsi produk, boleh dikosongkan.')
    created_at=models.DateTimeField(
    	auto_now_add=True,
    	help_text='Field waktu ini akan terisi secara otomatis.')
    is_active=models.IntegerField(
    	default=1,
    	help_text='Field ini bila nilainya lain selain 1, berarti tidak aktif.')

    # Meta class dipakai untuk membuat nama category dalam bentuk tunggal dan jamak
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # String method untuk mendisplai category title pada admin
    def __str__(self):
        return self.title 


# class name:SubCategory
class SubCategory(models.Model):
    id=models.AutoField(primary_key=True)
    '''Field category_id membuat hubungan/relationship antara
    Category dan SubCategory models.
    Dalam hal ini sebuah Category product boleh memiliki
    nol, satu, atau lebih SubCategory product.
    Atau paling tidak satu SubCategory product 
    merupakan bagian dari Category.
    '''
    category_id=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text='Klik untuk memilih satu kategori.')
    title=models.CharField(
        max_length=255, 
        blank=False,
        help_text='Field ini tidak boleh dikosongkan.')
    url_slug=models.CharField(
        max_length=255,
        help_text='Field ini pre-populated diambil dari title.')
    thumbnail=models.FileField(
        blank=True,
        help_text='Field untuk foto produk kategori.')
    description=models.TextField(
        blank=True,
        help_text='Field untuk deskripsi produk, boleh dikosongkan.')
    created_at=models.DateTimeField(
        auto_now_add=True,
        help_text='Field waktu ini akan terisi secara otomatis.')
    is_active=models.IntegerField(
        default=1,
        help_text='Field ini bila nilainya lain selain 1, berarti tidak aktif.')

    # Meta class dipakai untuk membuat nama category dalam bentuk tunggal dan jamak
    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    # String method untuk mendisplai category title pada admin
    def __str__(self):
        return self.title 