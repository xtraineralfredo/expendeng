from django.db import models

periodical_choices = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('BW', 'Bi-Weekly'),
        ('M', 'Monthly'),
        ('Q', 'Quarterly')
        ('SA', 'Semi-Annually')
        ('A', 'Annually')
    )

class Source(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)


class Income(models.Model):
    description = models.CharField(max_length=128)
    amount = models.DecimalField(decimal_places=2)
    date = models.DateField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=2, choices=periodical_choices)


class Expense(models.Model):
    amount = models.DecimalField(decimal_places=2)
    description = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=2, choices=periodical_choices)
    date = models.DateField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

