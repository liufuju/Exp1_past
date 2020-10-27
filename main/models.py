from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)



author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'main'
    players_per_group = None
    num_rounds = 8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age_year_before = models.IntegerField(label='')
    city_before = models.StringField(label='')
    emo = models.StringField()
    exact_time = models.StringField(label='')

    role_emo = models.IntegerField(label='')
    self_emo = models.IntegerField(label='')
    clear_emo = models.IntegerField(label='')
    isolate_emo = models.IntegerField(label='')
    sub_time = models.IntegerField(label='')
    strength_emo = models.IntegerField(label='')
    vivid_emo = models.IntegerField(label='')
    valence_emo = models.IntegerField(label='')
    diff_emo = models.IntegerField(label='')

    short_dscp = models.StringField(label='', max_length=30)
    dscp_emo = models.LongStringField(label='')

    cmp_ans1 = models.StringField()
    cmp_ans2 = models.StringField()
    cmp_ans3 = models.StringField()
    cmp_response1 = models.StringField()
    cmp_response2 = models.StringField()
    cmp_response3 = models.StringField()
    cmp_file1 = models.StringField()
    cmp_file2 = models.StringField()
    cmp_file3 = models.StringField()
