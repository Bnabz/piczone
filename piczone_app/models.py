from django.db import models

class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length =60)
    description = models.CharField(max_length =240)
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    upload_date= models.DateTimeField(auto_now_add=True)
