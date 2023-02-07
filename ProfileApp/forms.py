from  django import forms

class ProductForm(forms.Form):

    BRAND_LIST = [('Levi’s', 'Levi’s'),
                  ('Mc','Mc'),
                  ('LEE X LINE ', 'LEE X LINE '),
                  ('G-Star','G-Star'),
                  ('Era-Won','Era-Won'),]

    COLOR_LIST = [('White','White'),
                  ('Black','Black'),
                  ('Gray','Gray'),
                  ('Browm','Brown'),
                  ('Cream','Cream'),
                  ('Silver','Silver'),
                  ('Indigo','Indigo'),
                  ('Old Rose','Old Rose'),
                  ]
    TYPE_LIST = [('กางเกงยีนส์ทรงกระบอก','กางเกงยีนส์ทรงกระบอก'),
                 ('กางเกงยีนส์ทรงสลิม','กางเกงยีนส์ทรงสลิม'),
                 ('กางเกงยีนส์ทรงสกินนี่','กางเกงยีนส์ทรงสกินนี่'),
                 ('กางเกงยีนส์ทรงขากระดิ่ง','กางเกงยีนส์ทรงขากระดิ่ง'),
                 ('กางเกงยีนส์ทรงขาบาน','กางเกงยีนส์ทรงขาบาน'),
                 ('กางเกงยีนส์ทรงบอยเฟรนด์','กางเกงยีนส์ทรงบอยเฟรนด์'),
                 ('กางเกงยีนส์ทรงมัม','กางเกงยีนส์ทรงมัม'),
                 ]
    id = forms.CharField(max_length=13, label="รหัสสินค้า",
                         required=True,widget=forms.TextInput(attrs={'size':'15'}))
    brand = forms.CharField(max_length=30,label="ชื่อแบรนด์",required=True,widget=forms.Select(choices=BRAND_LIST))
    model = forms.CharField(max_length=30,label="ชื่อรุ่น",required=True,widget=forms.TextInput(attrs={'size':'35'}))
    color = forms.CharField(max_length=30,label="สี",required=True,widget=forms.RadioSelect(choices=COLOR_LIST))
    type = forms.CharField(max_length=30,label="ประเภท",required=True,widget=forms.Select(choices=TYPE_LIST))

    price = forms.IntegerField(label="ราคา",required=True,widget=forms.NumberInput(
        attrs={'size':'35','min':'2000','max':'1000000'}))
