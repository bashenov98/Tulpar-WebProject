from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Company(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Employee(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    specialty = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, related_name='employees')

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'specialty': self.specialty
        }


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
