from django.db.models import Sum
from rest_framework import serializers
from .models import SponsorModel, UniversitiesModel, StudentModel, SponsorStudentModel, Overall


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        fields = '__all__'


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        exclude = ['event']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversitiesModel
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        # fields = '__all__'
        exclude = ['email']

    def to_representation(self, instance):
        data = super(StudentSerializer, self).to_representation(instance)
        student_id = instance.id
        student_sponsors = SponsorStudentModel.objects.filter(student_id=student_id).values_list('sponsor__full_name', 'given_q')
        data['university'] = instance.university.name
        data['sponsors'] = student_sponsors
        return data


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        # fields = '__all__'
        exclude = ['email']

    def to_representation(self, instance):
        data = super(StudentsSerializer, self).to_representation(instance)
        data['university'] = instance.university.name
        student_id = instance.id
        ss_given_q = SponsorStudentModel.objects.filter(student_id=student_id).values_list('given_q').aggregate(Sum('given_q'))
        if ss_given_q['given_q__sum'] == None:
            ss_given_q['given_q__sum'] = 0
        # print(ss_given_q['given_q__sum'], 'student sponsor given q')

        data['given_payment'] = ss_given_q['given_q__sum']
        return data


class OverallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overall
        fields = '__all__'

    def to_representation(self, instance):
        data = super(OverallSerializer, self).to_representation(instance)
        given_q = SponsorStudentModel.objects.all().values_list('given_q').aggregate(Sum('given_q'))
        # print(given_q['given_q__sum'])
        data['overal_p'] = given_q['given_q__sum']

        overal_ap = StudentModel.objects.all().values_list('contract_q').aggregate(Sum('contract_q'))
        # print(overal_ap['contract_q__sum'])
        data['overal_ap'] = overal_ap['contract_q__sum']

        overal_np = overal_ap['contract_q__sum'] - given_q['given_q__sum']
        # print(overal_np)
        data['overal_np'] = overal_np

        return data


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'

    def to_representation(self, instance):
        data = super(StudentCreateSerializer, self).to_representation(instance)
        data['university'] = instance.university.name

        return data


class StudentAddSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorStudentModel
        fields = ['sponsor', 'student', 'given_q']
        extra_kwargs = {'given_q': {'required': True}}
        validators = []

    def validate(self, data):
        student = data.get('student')
        sponsor = data.get('sponsor')
        given_q = data.get('givan_q')
        student_fn = student.full_name
        # print(student_fn)
        s_cq = student.contract_q
        # print(s_cq)
        q = sponsor.id
        # print(q)
        sponsor_fn = sponsor.full_name
        # print(sponsor_fn)
        payment = sponsor.payment_q
        # print(payment)
        given_q = SponsorStudentModel.objects.filter(student_id=student.id)
        # print(given_q)
        overall_g = SponsorStudentModel.objects.filter(student_id=student.id).values_list('given_q').aggregate(Sum('given_q'))
        # print(overall_g, "overal")
        # print(overall_g['given_q__sum'])

        if overall_g['given_q__sum'] == None:
            overall_g['given_q__sum'] = 0

        if data['given_q'] <= payment:
            if data['given_q'] <= (s_cq - overall_g['given_q__sum']):
                return data
            elif overall_g['given_q__sum'] == s_cq:
                raise serializers.ValidationError({'given_q':
                    f"You cannot pay because this {student_fn} student's contract has been payed by sponsors !!!"})

            else:
                raise serializers.ValidationError({'given_q':
                    f"You cannot pay this {data['given_q']} amount of money to  this {student_fn} because you are paying too much overal contract payment it is {s_cq}, and you can pay {s_cq - overall_g['given_q__sum']} this amount of money !!!"})
        else:
            raise serializers.ValidationError({'given_q':
                        f"You are using too much money in this sponsor: {sponsor_fn} has only {payment} so you can use up to {payment}"})
        return data

    # def to_representation(self, instance):
    #     data = super(StudentAddSponsorSerializer, self).to_representation(instance)

    #     student_fn = instance.student.full_name
    #     # print(student_fn)
    #     s_cq = instance.student.contract_q
    #     # print(s_cq)
    #     q = instance.sponsor.id
    #     # print(q)
    #     sponsor_fn = instance.sponsor.full_name
    #     # print(sponsor_fn)
    #     payment = instance.sponsor.payment_q
    #     # print(payment)
    #     given_q = SponsorStudentModel.objects.filter(student_id=instance.student.id)
    #     # print(given_q)
    #
    #     s = 0
    #     for i in given_q:
    #         s += i.given_q
    #         print(s)
    #     print(s)
    #     q = 0
    #     if s == s_cq and q != 2:
    #         q += 1
    #
    #     p = 0
    #     if payment == 0 and p != 2:
    #         p += 1
    #
    #     if s < s_cq:
    #         if data['given_q'] <= s_cq:
    #             if data['given_q'] <= payment:
    #                 return data
    #             elif p == 2:
    #                 raise serializers.ValidationError(
    #                     f"You cannot transfer money from {sponsor_fn} to {student_fn} because your sponsor has no money left to pay !!!")
    #
    #             else:
    #                 data['upmoney'] = data['given_q'] - payment
    #                 raise serializers.ValidationError(
    #                     f"You are using too much money in this sponsor: {sponsor_fn} has only {payment} so you can use up to {payment}")
    #         elif data['given_q'] > s_cq:
    #             raise serializers.ValidationError(
    #                 f"You cannot pay this {data['given_q']} amount of money to  this {student_fn} because you are paying too much overal contract payment it is {s_cq} !!!")
    #     elif q == 2 or s > s_cq:
    #         raise serializers.ValidationError(
    #             f"You cannot pay because this {student_fn} student's contract has been payed by sponsors !!!")

    # def create(self, validated_data):
    #     # firstname = self.initial_data['first_name']
    #     # lastname = self.initial_data['last_name']
    #     # fullname = str(firstname) + " " + str(lastname)
    #     # email = self.initial_data['username'].lower()
    #
    #     sponsor = self.initial_data['sponsor']
    #     student = self.initial_data['student']
    #     given_q = self.initial_data['given_q']
    #
    #     try:
    #         customer = SponsorStudentModel.create(
    #             sponsor=sponsor,
    #             student=student,
    #             given_q=given_q)
    #
    #     except Error as e:
    #         error = {'message': e._message or 'Unknown error'}
    #         return Response(error, status=status.HTTP_400_BAD_REQUEST)

    def to_internal_value(self, data):
        student_id = data['student']
        # print(student_id)
        student_fn = [i.full_name for i in StudentModel.objects.filter(id=student_id)]
        # print(student_fn)
        s_cq = [i.contract_q for i in StudentModel.objects.filter(id=student_id)]
        # print(s_cq)
        sponsor_id = data['sponsor']
        # print(sponsor_id)
        sponsor_fn = [i.full_name for i in SponsorModel.objects.filter(id=sponsor_id)]
        # print(sponsor_fn)
        payment = [i.payment_q for i in SponsorModel.objects.filter(id=sponsor_id)]
        # print(payment)
        # given_q = SponsorStudentModel.objects.filter(student_id=student_id).values_list('given_q').aggregate(Sum('given_q'))
        # print(given_q['given_q__sum'], 'given_q')
        overall_g = SponsorStudentModel.objects.filter(student_id=student_id).values_list('given_q').aggregate(Sum('given_q'))
        if overall_g['given_q__sum'] == None:
            overall_g['given_q__sum'] = 0

        # print(given_q['given_q__sum'], s_cq[0])
        if int(data['given_q']) <= payment[0]:
            if int(data['given_q']) <= (s_cq[0] - overall_g['given_q__sum']) and overall_g['given_q__sum'] != s_cq[0] or overall_g['given_q__sum'] > s_cq[0]:
                sponsor_obj = SponsorModel.objects.get(id=sponsor_id)
                # print(sponsor_obj)
                sponsor_obj.payment_q = payment[0] - int(data['given_q'])
                # print(sponsor_obj.payment_q)
                sponsor_obj.save()
                return super().to_internal_value(data)
        return super().to_internal_value(data)

