from django.db import models


class Personality(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    descrip = models.TextField()
    
    def __str__(self):
        return self.name

class Resume(models.Model):
    cv = models.FileField(upload_to="uploads/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def get_resume_path(self):
        return self.cv.url

class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"
    
    def formatted_start_date(self):
        return self.start_date.strftime("%B %Y")
    
    def formatted_end_date(self):
        return self.end_date.strftime("%B %Y") if self.end_date else "Present"

class Experience(models.Model):
    
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    def formatted_start_date(self):
        return self.start_date.strftime("%B %Y")
    
    def formatted_end_date(self):
        return self.end_date.strftime("%B %Y") if self.end_date else "Present"

class Skills(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="skills_icons/")
    
    def __str__(self):
        return self.title

class Awards(models.Model):
    icons = {
        "flaticon-medal":"Medal",
        "flaticon-trophy":"Trophy",
    }
    image = models.ImageField(upload_to="awards/")
    icon = models.CharField(max_length=100,choices=icons)
    name = models.CharField(max_length=200)
    event_name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=200)
    owned_date = models.DateField()
    location =models.CharField(max_length=100)
    credential_URL = models.URLField()
    
    class Meta:
        ordering = ['-owned_date']
    
    def formatted_date(self):
        return self.owned_date.strftime("%B %Y")
    
    def __str__(self):
        return self.name

class Project(models.Model):
    icons = {
        'flaticon-camp':"Camp",
        'icon-book':'Book',
        'icon-terminal':"Terminal",
        'icon-whatsapp':"Whatsapp",
        'flaticon-circuit-board':"Circuit Board",
        'flaticon-bomberman':"Bomberman",
        'icon-music':"Music",
        'icon-search':"search",
        'icon-envelope-o':"loop",
        'icon-heart':"heart",
        'icon-user':"user",
        'icon-film':"film",
        'icon-gear':"gear",
        'icon-file-o':"file",
        'icon-clock-o':"clock",
        'icon-road':"road",
        'icon-download':"download",
        'icon-headphones':"headphones",
        'icon-headphones':"QRcode",
        'icon-barcode':"Barcode",
        'icon-camera':"camera",
        'icon-video-camera':"video camera",
        'icon-image':"image",
        'icon-map-marker':"map marker",
        'icon-pencil':"pencil",
        'icon-photo':"photo",
        'icon-picture-o':"picture",
        'icon-html5':"html",
        'icon-css3':"css",
        'icon-compress':"compress",
        'icon-mail-forward':"mail",
        'icon-keyboard':"keyboard",
        'icon-web':"web",
        'icon-server':"server",
        'icon-network_wifi':"wifi",
        'icon-network_cell':"network",
        'icon-dollar':"dollar",
        'icon-bank':'bank',
    }
    
    icon = models.CharField(max_length=200,choices=icons)
    url = models.URLField()
    name = models.CharField(max_length=200)
    skills_used = models.ManyToManyField(Skills)
    discrip = models.TextField()
    
    def __str__(self):
        return self.name