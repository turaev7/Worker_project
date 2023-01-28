from django.db import models




class Organization(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"


class Worker(models.Model):
    worker_name = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    worker_adress = models.CharField(max_length=200)
    worker_staff = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)
    worker_age = models.DateField()
    worker_pic = models.ImageField(upload_to="rasm",null=False, blank=False)

    def __str__(self):
        return self.worker_name
    
    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

sex = [
    ('male','male'),
    ('female','female'),
]


class Worker_info(models.Model):
    name = models.ForeignKey(Worker, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    parent_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    sex = models.CharField(choices=sex, max_length=100)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Worker info"
        verbose_name_plural = "Worker info"



class Relatives(models.Model):
    worker = models.ForeignKey(Worker_info, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    date = models.DateField()
    addres = models.CharField(max_length=200)
    work = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Relatives"
        verbose_name_plural = "Relatives"