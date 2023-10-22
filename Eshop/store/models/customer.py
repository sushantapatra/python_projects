from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def getCustomerByEmail(email):
        try:
            # customer = Customer.objects.filter(email=email) # get a multiple record
            customer = Customer.objects.get(email=email)  # get a single record
            return customer
        except:
            return False

    # check email duplicate

    def ifEmailExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
