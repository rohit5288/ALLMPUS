from django.db import models
import uuid
class products(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    product=models.CharField(max_length=100)
    img=models.ImageField(upload_to='static/product_img')
    cat_no=models.CharField(max_length=10)
    cas_no=models.CharField(max_length=50)
    mol_formula=models.CharField(max_length=50)
    inv_status=models.CharField(max_length=100)

class rfq(models.Model):
    product_id=models.ForeignKey(products,to_field='id',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    company=models.CharField(max_length=100)
    contact=models.IntegerField()
    package=models.IntegerField()
    package_unit=models.CharField(max_length=2,choices=(("MG","MG"),("G","G"),("KG","KG")),default="MG")



