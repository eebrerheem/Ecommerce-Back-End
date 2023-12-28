from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=30)
    description = models.TextField()
    slug = models.SlugField()
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return str(self.name)


class Attribute(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Attributes"

    def __str__(self):
        return str(self.name)


class AttributeValue(models.Model):
    attribute = models.ForeignKey(
        Attribute, related_name="attribute", on_delete=models.CASCADE)
    value = models.CharField(max_length=10)

    def __str__(self):
        return str(self.value)


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute_value = models.ManyToManyField(AttributeValue)
    sku = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Inventory"

    def __str__(self):
        return str(self.product.name)


class InventoryAttributeValue(models.Model):
    inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(
        AttributeValue, on_delete=models.CASCADE)


class ProductCategory(models.Model):
    inventory_id = models.OneToOneField(Inventory, on_delete=models.CASCADE)
    category_id = models.OneToOneField(Category, on_delete=models.CASCADE)


class StockControl(models.Model):
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE)
    last_check = models.DateTimeField(auto_now_add=True, editable=False)
    units = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Stock Control"


class Image(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    url = models.ImageField(upload_to='product images')
    alternative_text = models.CharField(max_length=50)
    is_feature = models.BooleanField(default=False)
