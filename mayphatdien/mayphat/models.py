from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Setting(models.Model):
    title_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200, unique=True)
    number_phone = models.CharField(max_length=20, unique=True)
    contact = models.CharField(max_length=50, unique=True)
    adress = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=50, unique=True)
    image_logo = models.ImageField(upload_to='static/logo/', blank=True)

class Slide(models.Model):
    title_name = models.CharField(max_length=200, unique=True)
    image_slide = models.ImageField(upload_to='static/mayphat/slide_hinh/', blank=True)
    status_choices = (
        ('Slide', 'Slide'),
        ('Banner', 'Banner'),

    )
    status = models.CharField(max_length=15, choices=status_choices, default=status_choices[0][0])

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=180)
    description = RichTextField(blank=True, null=True)
    category_image = models.ImageField(upload_to='static/categories/', blank=True)
    price = models.IntegerField()
    detail = RichTextField(blank=True, null=True)

    stock = models.IntegerField()
    nation = models.IntegerField()
    status_choices = (
        ('New', 'New'),
        ('Old', 'Old'),


    )
    status = models.CharField(max_length=15, choices=status_choices, default=status_choices[0][0])


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    status_choices = (
        ('rental', 'rental'),
        ('repair', 'repair'),
        ('transport', 'transport'),
    )
    status = models.CharField(max_length=15, choices=status_choices, default=status_choices[0][0])
    def __str__(self):
        return self.title


class Imageslide(models.Model):
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE,blank = False,  default=1)
    image_product = models.ImageField(upload_to='static/mayphat/slide_hinh/', blank=True)
class rating(models.Model):
    id_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=180)
    text =models.CharField(max_length=500)
    rating=models.IntegerField(default=0)

class Email(models.Model):
    mail_name= models.CharField(max_length=50)
    def __str__(self):
        return self.mail_name

class Order(models.Model):
    payment_code = models.IntegerField()
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    number_phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    payment_methosd = models.CharField(max_length=400)
    payment_data = models.CharField(max_length=400,blank=True, null=True)
    tax_data = models.CharField(max_length=50,blank=True, null=True)
    company_name = models.CharField(max_length=100,blank=True, null=True)
    company_adress = models.CharField(max_length=100,blank=True, null=True)
    company_data = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    fulfilled = models.BooleanField(verbose_name='Payment already')
    user_update = models.CharField(max_length=50)
    update_date = models.DateTimeField(auto_now=True)
    status_order = (
        ('', ''),
        ('OK', 'OK'),
        ('Delivery', 'Delivery'),
        ('Cancel', 'Cancel'),

    )
    order_status=models.CharField(max_length=15, choices=status_order)
    def save(self, *args, **kwargs):
        if self.payment_code is None:
            self.payment_code = Order.objects.all().count() + 100000+1
        super().save(*args, **kwargs)
class Order_detail(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    price = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    price_update = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    ship_cost = models.DecimalField(max_digits=12, decimal_places=3, default=0)
    amount = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True)
class OrderSummary(Order_detail): #Extends funcs of model without creating a table in DB
    class Meta:
        proxy = True #important A proxy model extends the functionality of another model without creating an actual table in the database
        verbose_name = 'Order Summary'
        verbose_name_plural = 'Orders Summary'