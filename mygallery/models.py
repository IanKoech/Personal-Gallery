from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    name  = models.CharField(max_length=30)
    image_url = models.ImageField(upload_to = 'galleries/')
    description = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, updates):
        cls.objects.filter(id=id).update(updates)

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id = id )
        return image

    @classmethod
    def search_image(cls, searchterm):
        category_searched = Category.objects.filter(name=searchterm)
        images = cls.objects.filter(category=category_searched)
        return images

    @classmethod
    def filter_image(cls, category):
        images = cls.objects.filter(category=category)
        return images