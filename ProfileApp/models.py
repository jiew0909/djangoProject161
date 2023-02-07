from django.db import models

# Create your models here.

class Product:
    def __init__(self,id,brand,model,color,type,price,discount,vat,net):
        self.id =id
        self.brand = brand
        self.model = model
        self.color = color
        self.type = type
        self.price = price
        self.discount = discount
        self.vat = vat
        self.net = net

    def __str__(self):
        return "ID.{}, Name.{}, Brand.{}, Color.{}, Type.{}, Price.{}, Discount.{}, Vat.{}, Net.{},"\
            .format(self.id,self.brand,self.model,self.color,self.discount,self.price,
                    self.discount,self.vat,self.net)
