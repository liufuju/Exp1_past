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
    name_in_url = 'practice'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age_year_later = models.IntegerField(label='')
    city_later = models.StringField(label='')
    emo = models.StringField()

    exact_time = models.StringField(label='')
    sub_time = models.IntegerField(label='')
    role_emo = models.IntegerField(label='')
    self_emo = models.IntegerField(label='')
    clear_emo = models.IntegerField(label='')
    isolate_emo = models.IntegerField(label='')
    strength_emo = models.IntegerField(label='')
    vivid_emo = models.IntegerField(label='')
    valence_emo = models.IntegerField(label='')
    diff_emo = models.IntegerField(label='')

    short_dscp = models.StringField(label='', max_length=30)
    dscp_emo = models.LongStringField(label='')
