from django.db import models


# Create your models here.
class Produto(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    nome = models.CharField(
        max_length=104,
        null=False
    )

    class Meta:
        db_table = 'produto'
        managed = True
