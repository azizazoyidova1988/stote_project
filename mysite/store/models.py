from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "services"

    def __str__(self):
        return self.name



class Projects(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    title = models.CharField(max_length=250, blank=False, null=False)
    image_1 = models.ImageField(upload_to='images/', blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    aria = models.CharField(max_length=50, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=1)
    location = models.CharField(blank=False, null=False,max_length=100)
    project_start = models.CharField(blank=False, null=False, max_length=50)
    project_finish = models.CharField(blank=False, null=False, max_length=50)
    image_2 = models.ImageField(upload_to='images/', blank=False, null=False)
    image_3 = models.ImageField(upload_to='images/', blank=False, null=False)
    image_4 = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.name




class Teams(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    mobil_phone = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    telegram = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "team"

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    author = models.CharField(max_length=150, blank=False, null=False)
    description_1 = models.CharField(max_length=650, blank=False, null=False)
    description_2 = models.CharField(max_length=650, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    author_image = models.ImageField(upload_to='images/', blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "testimonial"

    def __str__(self):
        return self.name


class Commenter(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    comment = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "commenter"

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact"

    def __str__(self):
        return self.name

class User(models.Model):
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.email


class Image(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "image"

    def __str__(self):
        return self.name