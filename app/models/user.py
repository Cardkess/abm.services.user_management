from tortoise import Model, fields
import uuid


class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    username = fields.CharField(max_length=100, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=128)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    gender = fields.CharField(max_length=10, null=True)  
    phone_number = fields.CharField(max_length=20, null=True)
    address = fields.TextField(null=True)  # To store the user's full address
    city = fields.CharField(max_length=100, null=True)
    state = fields.CharField(max_length=100, null=True)
    country = fields.CharField(max_length=100, null=True)
    postal_code = fields.CharField(max_length=20, null=True)
    date_of_birth = fields.DateField(null=True)  # Optional for demographic info
    preferred_payment_method = fields.CharField(max_length=50, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"