from django.db import models

# Create your models here.
class Destination():
    name: str
    price: int
    desc: str
    img: str
    offer: bool