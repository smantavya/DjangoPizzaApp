from django.db import models


# Create your models here.

class Pizza(models.Model):
    type = models.CharField(max_length=30,
                            choices=[
                                ('R','regular'),
                                ('S','square'),
                            ])
    size = models.CharField(max_length=30,
                            choices=[
                                ('S','small'),
                                ('M','medium'),
                                ('L','large'),
                            ])
    TOPPINGS = [('ON','onion'),
                ('TM','tomato'),
                ('CN','corn'),
                ('CP','cpasicum'),
                ('CH','cheese'),
                ('JP','jalapeno'),
                ('PN','pepproni'),
                ('BO','black olives'),
                ]
    topping = models.CharField(max_length=122, choices=TOPPINGS)

