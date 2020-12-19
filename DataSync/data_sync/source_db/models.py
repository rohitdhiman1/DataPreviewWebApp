from django.db import models

class SourceDatabase(models.Model):
    name = models.CharField(max_length = 200)
    database_id = models.IntegerField(default=0)

    def __str__(self):
        return f"DataBase Name :  {self.name}  |  DataBaseID : {self.database_id}"
