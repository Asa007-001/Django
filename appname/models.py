from django.db import models

class I(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bookname = models.CharField(max_length=200)  # 假設你有一個 bookname 欄位

    def __str__(self):
        return self.bookname + '  ' + self.author
