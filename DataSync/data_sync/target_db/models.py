from django.db import models

class TargetDatabase(models.Model):
    name = models.CharField(max_length = 200)
    date_created = models.DateField()
    database_id = models.IntegerField(default=0)

    def __str__(self):
        return f"DataBase Name :  {self.name}  |  Date of creation : {self.date_created}  |  DataBaseID : {self.database_id}"


