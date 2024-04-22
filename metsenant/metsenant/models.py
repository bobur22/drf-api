from datetime import timezone

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def validation_payment_q(value):
    if value < 100000:
        raise ValidationError('You must have minimum of 100000 to pay students')


class SponsorModel(models.Model):
    PersonChoices = (('legal', 'legal'), ('physical', 'physical'))

    EventChoices = (
        ('New', 'new'), ('Moderinization', 'moderinization'), ('Approved', 'approved'), ('Rejected', 'rejected'))

    full_name = models.CharField(max_length=100)
    phone_n = models.CharField(max_length=12)
    payment_q = models.PositiveIntegerField(blank=True, null=True, validators=[validation_payment_q])
    person = models.CharField(max_length=30, choices=PersonChoices)
    event = models.CharField(max_length=30, choices=EventChoices, default='New')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'


class PhysicalPModel(models.Model):
    sponsor = models.OneToOneField(SponsorModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.sponsor.person


class LegalPModel(models.Model):
    sponsor = models.OneToOneField(SponsorModel, on_delete=models.CASCADE)
    organization_n = models.CharField(max_length=100)

    def __str__(self):
        return self.sponsor.person


class UniversitiesModel(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'


class StudentModel(models.Model):
    DEGREE_CHOICES = (
        ("bachelor's", "bachelor's"),
        ("master's", "master's"),
        ("doctoral", "doctoral")
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    degree = models.CharField(max_length=30, choices=DEGREE_CHOICES)
    contract_q = models.PositiveIntegerField()

    university = models.ForeignKey(UniversitiesModel, on_delete=models.CASCADE, related_name='student_university')
    # sponsor = models.ManyToManyField(SponsorModel, null=True, blank=True, related_name='student_sponsor')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

def validation_money(value):
    if value == 0:
        raise ValidationError(f"You cannot transfer money from sponsor to student because of lack of money from you sponsor's account")


class SponsorStudentModel(models.Model):
    sponsor = models.ForeignKey(SponsorModel, null=True, blank=True, on_delete=models.CASCADE,
                                related_name='sponsor')
    student = models.ForeignKey(StudentModel, null=True, blank=True, on_delete=models.CASCADE,
                                related_name='student')
    given_q = models.PositiveIntegerField(validators=[validation_money])

    def __str__(self):
        return f"{self.given_q}"

    # def calculate_money(self):
    #     payment_q = SponsorModel.objects.filter(payment_q=self)

    # def money_checker(self):
    #     sponsor = self.sponsor.full_name
    #     # print(sponsor)
    #     payment_q = self.sponsor.payment_q
    #     # print(payment_q)
    #     # student_contract_q = self.student.contract_q
    #     # print(student_contract_q)
    #     given_q = self.given_q
    #     # print(given_q)
    #     if given_q > payment_q:
    #         upmoney = given_q - payment_q
    #         raise ValidationError(
    #             f'You are using too much money in this {sponsor} have only {payment_q} so you can use up to {upmoney}')

class Overall(models.Model):
    overal_p = models.PositiveIntegerField()
    overal_ap = models.PositiveIntegerField()
    overal_np = models.PositiveIntegerField()