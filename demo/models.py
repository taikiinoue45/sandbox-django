from django.db import models


class InputImage(models.Model):
    class Meta(object):
        db_table = "input_image"

    title = models.CharField(verbose_name="title", null=True, blank=True, max_length=255)
    input_image = models.ImageField(
        verbose_name="input_image", null=True, blank=True, upload_to="images/"
    )

    def __str__(self) -> str:
        return self.title
