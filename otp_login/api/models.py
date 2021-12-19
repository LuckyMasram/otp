from django.db import models

# Create your models here.


class TempUser(models.Model):
    id = models.AutoField(primary_key=True)
    mobile_number = models.CharField(max_length=10)
    otp = models.CharField(max_length=6, blank=True)
    created_time = models.DateTimeField(blank=True)
    expire_time = models.DateTimeField(blank=True)

    def __str__(self):
        return self.mobile_number


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True)
    token = models.CharField(max_length=255, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=True)
    mobile = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False, blank=False)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.customer_name)


class TradeType(models.Model):
    trade_id = models.IntegerField()
    trade_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False, blank=False)
    token = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.trade_id)


class Tradesman(models.Model):
    tm_id = models.CharField(max_length=50)
    tradesman_name = models.CharField(max_length=50)
    trade_id = TradeType().trade_id
    token = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, blank=False)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.tm_id)


class BookTradesman(models.Model):
    bt_id = models.AutoField(primary_key=True)
    cust_id = Customer().cust_id
    tm_id = Tradesman().tm_id
    token = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = ['Pending', 'Booked', 'Canceled']

    def __str__(self):
        return str(self.bt_id)


class ImageUpload(models.Model):
    image_id = models.AutoField(primary_key=True)
    cust_id = Customer().cust_id
    image_path = models.ImageField(upload_to=True)
    token = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    status = ['Active', 'Inactive']

    def __str__(self):
        return str(self.image_id)
