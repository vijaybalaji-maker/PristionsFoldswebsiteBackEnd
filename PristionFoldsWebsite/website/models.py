from django.db import models

class PrsitionFoldsEnquiry(models.Model):
    company_name = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=25, blank=True)
    year_of_establishment = models.CharField(max_length=25, blank=True)
    district = models.CharField(max_length=25, blank=True)
    pincode = models.CharField(max_length=25, blank=True)
    number_of_branch = models.CharField(max_length=25, blank=True)
    email = models.EmailField(blank=False, max_length=50, null=True,unique=False, verbose_name="email address")
    mobile_number = models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    lastUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.guest_name

    class Meta:
        db_table = 'pristion_folds_enquiry'
