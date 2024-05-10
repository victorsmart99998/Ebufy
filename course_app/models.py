from django.db import models
from userauths.models import User


# Create your models here.
RATING = (
        ('Draft', 'Draft'),
        ('Disabled', 'Disabled'),
        ('Rejected', 'Rejected'),
        ('In_review', 'In_review'),
        ('Published', 'Published'),
    )

class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='category/')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Author(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='author/')
    bio = models.TextField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


class Course(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='author/')
    video_link = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    descriptions = models.TextField(null=True, blank=True)
    price = models.IntegerField(default='0', null=True)
    discount = models.IntegerField(default='0', null=True)
    status = models.CharField(choices=STATUS, max_length=200, null=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


class What_to_learn(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    points = models.CharField(max_length=700, null=True)

    def __str__(self):
        return self.points


class Requirements(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    points = models.CharField(max_length=700, null=True)

    def __str__(self):
        return self.points


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=700, null=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    serial_number = models.IntegerField(null=True)
    image = models.ImageField(upload_to='video/')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=700, null=True)
    youtube_id = models.CharField(max_length=700, null=True, blank=True)
    time_duration = models.IntegerField(null=True, blank=True)
    preview = models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


class User_course(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    paid = models.BooleanField(default=False)
    points = models.CharField(max_length=700, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.CharField(max_length=700, choices=RATING, default=None, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "product review"

    def __str__(self):
        return self.review