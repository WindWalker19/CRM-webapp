from django.db import models

# Create your models here.
# Create class that create Database Table.

class CustomerMod(models.Model):
    name    = models.CharField(max_length = 200, null = True)
    phone   = models.CharField(max_length = 200, null = True)
    email   = models.CharField(max_length = 200, null = True)
    date_created  = models.DateTimeField(auto_now_add = True,null = True)

# Displays the way how the Database looks.
    def __str__(self):
        return self.name

class Tag(models.Model):
    name            =  models.CharField(max_length=200, null =True)
    
    def __str__(self):
        return self.name

class ProductMod(models.Model):
    CATEGORY=  (
                ('Indoor','Indoor'),
                ('Out Door','Out Door')
               )
    name            =  models.CharField(max_length=200, null =True)
    price           =  models.FloatField(null=True)
    category        =  models.CharField(max_length=200, null =True,choices=CATEGORY)
    description     =  models.CharField(max_length=200, null =True, blank=True)
    date_created    =  models.DateTimeField(auto_now_add=True,null=True)
    tags            =  models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class OrderMod(models.Model):
    STATUS= (
            ('Pending','Pending'),
            ('Out for delivery','Out for delivery'),
            ('Delivered','Delivered')
            )

    #Creating a One to Many realtion.
    customer        =  models.ForeignKey(CustomerMod, null =True, on_delete= models.SET_NULL)
    product         =  models.ForeignKey(ProductMod, null =True, on_delete= models.SET_NULL)
    date_created    =  models.DateTimeField(auto_now_add=True,null=True)
    status          =  models.CharField(max_length=200,null=True,choices=STATUS)
    note            =  models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.product.name