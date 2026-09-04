from django.db import models

NATIONALITY_CHOICES = [
    ('Ugandan', 'Ugandan'),
    ('Kenyan', 'Kenyan'),
    ('Tanzanian', 'Tanzanian'),
    ('Burundian', 'Burundian'),
    ('Rwandese', 'Rwandese'),
    ('Somalian', 'Somalian'),
    ('South Sudanese', 'South Sudanese'),
]

MARITAL_STATUS_CHOICES = [
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
]

SETTLEMENT_CAMP_CHOICES = [
    ('Gulu settlement camp', 'Gulu settlement camp'),
    ('Arua settlement camp', 'Arua settlement camp'),
    ('Mbara settlement camp', 'Mbara settlement camp'),
    ('Kasese settlement camp', 'Kasese settlement camp'),
    ('Busia settlement camp', 'Busia settlement camp'),
    ('Mbale settlement camp', 'Mbale settlement camp'),
    ('Kigezi settlement camp', 'Kigezi settlement camp'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class Beneficiary(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_joining_settlement = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Female')
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES)
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES)
    settlement_camp = models.CharField(max_length=100, choices=SETTLEMENT_CAMP_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"