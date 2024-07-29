from django.db import models


class BaseUUIDModel(models.Model):
    id = models.CharField(max_length=32, primary_key=True,
                          unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid1().hex
        super(BaseUUIDModel, self).save(*args, **kwargs)


class Authors(BaseUUIDModel):
    autor = models.CharField(max_length=128)

    def __str__(self):
        return self.autor

    class Meta:
        db_table = "autores"


class Categories(BaseUUIDModel):
    categoria = models.CharField(max_length=128)

    def __str__(self):
        return self.categoria

    class Meta:
        db_table = "categorias"


class Publishers(BaseUUIDModel):
    editorial = models.CharField(max_length=128)

    def __str__(self):
        return self.editorial

    class Meta:
        db_table = "editorial"


class Books(BaseUUIDModel):
    titulo = models.CharField(max_length=256)
    fecha_de_publicacion = models.DateField()
    autor = models.ForeignKey(Authors, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categories, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    idioma = models.CharField(max_length=32)
    paginas = models.IntegerField()

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "libros"
        ordering = ["titulo"]
