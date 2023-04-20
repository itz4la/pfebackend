from django.db.models import CASCADE, ForeignKey, Model
from django.db.models.fields import FloatField, TextField
from rest_framework.serializers import ModelSerializer
from common.models import create_model_serializer, patient_model_location
from gestionusers.models import Teacher


class BehaviorTroubleTeacher(Model):
    # 4-5-6-10-11-12-23-27
    arrogant_impolite = TextField(null=False, db_column='arrogant_impolite')
    angry_unexpected_behavior = TextField(null=False, db_column='angry_unexpected_behavior')
    sensitive_criticism = TextField(null=False, db_column='sensitive_criticism')
    pout_sulk_easily = TextField(null=False, db_column='pout_sulk_easily')
    moody = TextField(null=False, db_column='moody')
    brawler = TextField(null=False, db_column='brawler')
    deny_mistakes_blame_others = TextField(null=False, db_column='deny_mistakes_blame_others')
    # question 27 :
    few_relations_school = TextField(null=False, db_column='few_relations_school')
    patient = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)
    teacher = OneToOneField(null=False, on_delete=CASCADE, to='gestionusers.Teacher')

    class Meta:
        db_table = 'behavior_trouble_teacher'


class HyperActivityTroubleTeacher(Model):
    #  1,  2,  3, 8, 14, 15, 16
    restless_squirms_chair = TextField(db_column='restless_squirms_chair', null=False)
    inappropriate_noises = TextField(null=False, db_column='inappropriate_noises')
    immediately_satisfied_needs = TextField(null=False, db_column='immediately_satisfied_needs')
    annoy_students = TextField(null=False, db_column='annoy_students')
    goes_left_right = TextField(null=False, db_column='goes_left_right')
    easily_turn_on_impulsive = TextField(null=False, db_column='easily_turn_on_impulsive')
    excessive_attention_from_teacher = TextField(null=False, db_column='excessive_attention_from_teacher')
    patient = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)
    teacher = OneToOneField(null=False, on_delete=CASCADE, to='gestionusers.Teacher')

    class Meta:
        db_table = 'hyperactivity_trouble_teacher'


class InattentionTroubleTeacher(Model):
    distracted = TextField(null=False, db_column='distracted')
    dreamer = TextField(null=False, db_column='dreamer')
    led_by_others = TextField(null=False, db_column="led_by_others")
    trouble_guiding_others = TextField(null=False, db_column='trouble_guiding_others')
    trouble_finishing_things = TextField(null=False, db_column='trouble_finishing_things')
    immature = TextField(null=False, db_column='immature')
    upset_easily_make_effort = TextField(null=False, db_column='upset_easily_make_eff')
    has_learning_difficulties = TextField(null=False, db_column='has_learning_difficulties')
    patient = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)
    teacher = OneToOneField(null=False, on_delete=CASCADE, to='gestionusers.Teacher')

    class Meta:
        db_table = 'inattention_form_teacher'

class FormAbrTeacher(Model):
    restless_squirms_chair = TextField(null=False, db_column="restless_squirms_chair")
    angry_unexpected_behavior = TextField(null=False, db_column="angry_unexpected_behavior")
    distracted = TextField(null=False, db_column="distracted")
    annoy_students = TextField(null=False, db_column="annoy_students")
    pout_sulk_easily = TextField(null=False, db_column="pout_sulk_easily")
    moody = TextField(null=False, db_column="moody")
    goes_left_right = TextField(null=False, db_column="goes_left_right")
    easily_turn_on_impulsive = TextField(null=False, db_column="easily_turn_on_impulsive")
    trouble_finishing_things = TextField(null=False, db_column="trouble_finishing_things")
    upset_easily_make_effort = TextField(null=False, db_column="upset_easily_make_effort")
    patient = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)
    teacher = OneToOneField(null=False, on_delete=CASCADE, to='gestionusers.Teacher')
    date = DateTime(auto_now_add=True)

    class Meta:
        db_table = 'form_abr_teacher'


class BehaviorTroubleTeacherSerializer(ModelSerializer):
    class Meta:
        model = BehaviorTroubleTeacher
        fields = '__all__'


class HyperActivityTroubleTeacherSerializer(ModelSerializer):
    class Meta:
        model = HyperActivityTroubleTeacher
        fields = '__all__'


class InattentionTroubleTeacherSerializer(ModelSerializer):
    class Meta:
        model = InattentionTroubleTeacher
        fields = '__all__'


class FormAbrSerializer(ModelSerializer):
    class Meta:
        model = FormAbrTeacher
        fields = '__all__'
