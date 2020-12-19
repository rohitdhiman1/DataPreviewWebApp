from django.db import models

class NewConnection(models.Model):
    schema_name = models.CharField(max_length=500)
    table_name = models.CharField(max_length=500)
    server_url = models.CharField(max_length=500)
    port_number = models.IntegerField(default=0)
    user_name = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

    def __str__(self):
        return f"Schema Name :  {self.schema_name}  |  Table Name : {self.table_name} " \
            f"| Server URL : {self.server_url} | Port Number : {self.port_number} " \
            f"| Username : {self.user_name} | Password : {self.password} "