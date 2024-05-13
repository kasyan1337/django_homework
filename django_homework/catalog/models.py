from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    ) # Свяжите продукт и категорию, используя связь между таблицами «Один ко многим».
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manufactured_at = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
