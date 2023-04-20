from django.db.models import CASCADE, FloatField, Model, OneToOneField, TextField, ForeignKey
from common.models import choices, create_model, patient_model_location, create_model_serializer
from rest_framework.serializers import ModelSerializer


class BehaviorTroubleParent(Model):
    # 2-8-14-19-20-27-35-39
    insolent_wth_grown_ups = TextField(null=False, db_column="insolent_wth_grown_ups")
    feels_attacked_defensive = TextField(null=False, db_column="feels_attacked_defensive")
    destructive = TextField(null=False, db_column="destructive")
    deny_mistakes_blame_others = TextField(null=False, db_column="deny_mistakes_blame_others")
    quarrelsome_get_involved_fight = TextField(null=False, db_column="quarrelsome_get_involved_fight")
    bully_intimidate_comrades = TextField(null=False, db_column="bully_intimidate_comrades")
    constantly_fight = TextField(null=False, db_column="constantly_fight")
    unhappy = TextField(null=False, db_column="unhappy")
    patient = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)

    class Meta:
        db_table = 'behaviour_trouble_parent'


class LearningTroubleParent(Model):
    # 10-25-31-37
    has_learning_difficulties = TextField(null=False, db_column="has_learning_difficulties")
    trouble_finishing_things = TextField(null=False, db_column="trouble_finishing_things")
    easily_being_distracted = TextField(null=False, db_column="easily_being_distracted")
    enability_finish_when_do_effort = TextField(null=False, db_column="enability_finish_when_do_effort")
    patient = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)

    class Meta:
        db_table = 'learning_trouble_parent'


class SomatisationTroubleParent(Model):
    # 32-41-43-44
    headaches = TextField(null=False, db_column="headaches")
    upset_stomach = TextField(null=False, db_column="upset_stomach")
    physical_aches = TextField(null=False, db_column="physical_aches")
    vomiting_nausea = TextField(null=False, db_column="vomiting_nausea")

    patient = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)

    class Meta:
        db_table = 'somatisation_trouble_parent'


class HyperActivityTroubleParent(Model):
    # 4-5-11-13
    excitable_impulsive = TextField(null=False, db_column="excitable_impulsive")
    want_dominate = TextField(null=False, db_column="want_dominate")
    squirms = TextField(null=False, db_column="squirms")
    restless_needs_do_something = TextField(null=False, db_column="restless_needs_do_something")

    patient = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)

    class Meta:
        db_table = 'hyperactivity_trouble_parent'


class AnxityTroubleParent(Model):
    # 12-16-24-47
    afraid_new_things = TextField(null=False, db_column="afraid_new_things")
    shy = TextField(null=False, db_column="shy")
    worry_much = TextField(null=False, db_column="worry_much")
    being_crashed_manipulated = TextField(null=False, db_column="being_crashed_manipulated")

    patient = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)

    class Meta:
        db_table = 'anxiety_trouble_parent'


class FormAbrParent(Model):
    # 4-7-11-13-14-25-31-33-37-38
    excitable_impulsive = TextField(null=False, db_column="excitable_impulsive")
    cry_often_easily = TextField(null=False, db_column="cry_often_easily")
    squirms = TextField(null=False, db_column="squirms")
    restless_needs_do_something = TextField(null=False, db_column="restless_needs_do_something")
    destructive = TextField(null=False, db_column="destructive")
    trouble_finishing_things = TextField(null=False, db_column="trouble_finishing_things")
    easily_being_distracted = TextField(null=False, db_column="easily_being_distracted")
    moody = TextField(null=False, db_column="moody")
    enability_finish_when_do_effort = TextField(null=False, db_column="enability_finish_when_do_effort")
    disturb_other_children = TextField(null=False, db_column="disturb_other_children")

    patient = OneToOneField(null=False, on_delete=CASCADE, to=patient_model_location)
    score = FloatField(null=False)

    class Meta:
        db_table = 'forme_abr_parent'


class BehaviorTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = BehaviorTroubleParent
        fields = '__all__'


class LearningTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = LearningTroubleParent
        fields = '__all__'


class SomatisationTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = SomatisationTroubleParent
        fields = '__all__'


class HyperActivityTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = HyperActivityTroubleParent
        fields = '__all__'


class AnxityTroubleParentSerializer(ModelSerializer):
    class Meta:
        model = AnxityTroubleParent
        fields = '__all__'


class FormAbrParentSerializer(ModelSerializer):
    class Meta:
        model = FormAbrParent
        fields = '__all__'
