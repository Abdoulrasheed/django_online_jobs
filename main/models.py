from django.db import models
from django.db.models.expressions import F
from django.utils.translation import ugettext as _


class Listing(models.Model):
    name = models.CharField(_("job name"), max_length=50)
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)
    status = models.BooleanField(_("status"), default=False)
    category = models.CharField(_("category"), choices=(("Full Time", "Full Time"), ("Contract", "Contract")), max_length=50)
    
    def __str__(self):
        return self.name
    
class Applicants(models.Model):
    job = models.ForeignKey(Listing, verbose_name=_(""), on_delete=models.CASCADE)
    firstname = models.CharField(_("name"), max_length=50)
    surname = models.CharField(_("surname"), max_length=50)
    othername = models.CharField(_("othername"), max_length=50)
    address = models.CharField(_("address"), max_length=50)
    phone = models.CharField(_("phone"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    resume = models.FileField(_("resume"), help_text="Upload your resume in pdf", upload_to="uploaded_resumes/", max_length=100)
    
    class Meta:
        verbose_name ="Applicant"
        verbose_name_plural = "Applicants"
    
    def get_resume(self):
        return self.resume if self.resume else "#"
    
    def __str__(self):
        return self.firstname