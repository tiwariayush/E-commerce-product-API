from django.db import models

class url_product(models.Model):
   url=models.URLField(verify_exists=False)
