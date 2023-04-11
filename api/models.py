from django.db import models

class Dojo(models.Model):
    dojo_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.dojo_name

class Member(models.Model):
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    kyu = models.IntegerField(default=8)

    def __str__(self) -> str:
        return f"name: {self.name}, dojo: {self.dojo}"