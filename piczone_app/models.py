from django.db import models

class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length =60)
    description = models.CharField(max_length =240)
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    upload_date= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    def save_image(self):
        return self.save() 

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_image_by_category(cls, search_term):
        return cls.objects.filter(category__icontains = search_term)
 
    @classmethod
    def filter_by_location(cls, location):
        return cls.objects.filter(location__name=location).all()
        
    @classmethod
    def update_image(cls, id, new_img):
        cls.objects.filter(id=id).update(image=new_img)


class Category(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
