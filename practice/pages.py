from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Background(Page):
    def before_next_page(self):
        self.participant.vars['age_year_later'] = self.player.age_year_later
        self.participant.vars['city_later'] = self.player.city_later

    def is_displayed(self):
        criterion = self.round_number == 1
        return criterion

    form_model = 'player'
    form_fields = ['age_year_later', 'city_later']


class Emo_evoketion(Page):
    def vars_for_template(self):
        age = self.participant.vars['age_year_later']
        city_later = self.participant.vars['city_later']
        return dict(
            age=age,
            city_later=city_later,
            round_number=self.round_number
        )
    
    form_model = 'player'
    form_fields = ['short_dscp']


class Imagination(Page):
    def vars_for_template(self):
        event = self.player.short_dscp
        return dict(
            event=event
        )


class Question_reading(Page):
    pass


class Question_filling(Page):
    form_model = 'player'
    form_fields = [
        'role_emo',
        'self_emo',
        'clear_emo',
        'isolate_emo',
        'sub_time',
        'vivid_emo',
        'valence_emo',
        'diff_emo'
    ]


class Description(Page):
    def vars_for_template(self):
        event = self.player.short_dscp
        return dict(
            event=event
        )

    form_model = 'player'
    form_fields = ['dscp_emo']


page_sequence = [Instructions, Background, Emo_evoketion, Imagination, Question_reading, Question_filling, Description]
