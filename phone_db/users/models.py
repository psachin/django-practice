from django.db import models
# Create your models here.

class FullName(models.Model):
    """
    first, middle and last name of employee
    """
    first_name = models.CharField('First Name',max_length=15,help_text="type first name here")
    middle_name = models.CharField('Middle Name',max_length=15,help_text="type your middle name or father's name here")
    last_name = models.CharField('Last Name',blank=True,max_length=15,help_text="type your last name or surname here")

    def __unicode__(self):
        return u'%s %s %s' % (self.first_name, self.middle_name, self.last_name)


class Emp(models.Model):
    """
    employee details
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )

    id = models.AutoField('ID', primary_key=True)
    name = models.ForeignKey(FullName, help_text="type employee's full name here")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    emp_id = models.CharField(max_length=6,unique=True)
    mobile = models.IntegerField(unique=True)
    home = models.IntegerField('Home Phone',null=True,blank=True,unique=True)
    email = models.EmailField()
    address = models.TextField(max_length=500)

    def __unicode__(self):
        return u'%s' % (self.name)

class Record(models.Model):
    pass
#    emp = models.ForeignKey(Emp)
    
    # def __unicode__(self):
    #     return self.emp


