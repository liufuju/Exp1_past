from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import os, pandas, random

class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Background(Page):
    def before_next_page(self):
        self.participant.vars['age_year_before'] = self.player.age_year_before
        self.participant.vars['city_before'] = self.player.city_before

    def is_displayed(self):
        criterion = self.round_number == 1
        return criterion

    form_model = 'player'
    form_fields = ['age_year_before', 'city_before']


class Composition(Page):
    def vars_for_template(self):
        pwd = os.getcwd()
        folder = 'reference'
        file_path = os.path.join(pwd, folder, 'composition.xlsx')
        cmp_data = pandas.read_excel(file_path)

        population = list(range(36))
        selection = random.sample(population, 4)
        information = []

        for i in selection:
            information += [[cmp_data['file'].iloc[i], cmp_data['big'].iloc[i], cmp_data['small'].iloc[i]]]


        self.player.cmp_ans1 = information[0][1]
        self.player.cmp_ans2 = information[1][2]
        self.player.cmp_ans3 = information[2][1]
        self.player.cmp_ans4 = information[3][1]

        return dict(
            cmp_pic1='compositions/' + information[0][0],
            cmp_pic2='compositions/' + information[1][0],
            cmp_pic3='compositions/' + information[2][0],
            cmp_pic4='compositions/' + information[3][0]
        )

    form_model = 'player'
    form_fields = ['cmp_response1', 'cmp_response2', 'cmp_response3', 'cmp_response4']


class Emo_evoketion(Page):
    def vars_for_template(self):
        emotion = self.participant.vars['emotions'][self.round_number - 1]
        emo_dscp = self.participant.vars['emo_dscp'][self.round_number - 1]
        age = self.participant.vars['age_year_before']
        city_before = self.participant.vars['city_before']
        emo_evoking_sound = 'sound/{}.m4a'.format(emotion)

        return dict(
            emotion=emotion,
            emo_dscp=emo_dscp,
            age=age,
            city_before=city_before,
            round_number=self.round_number,
            emo_evoking_sound=emo_evoking_sound
        )

    def before_next_page(self):
        self.player.emo = self.participant.vars['emotions'][self.round_number - 1]

    form_model = 'player'
    form_fields = ['short_dscp', 'exact_time']


class Imagination(Page):
    def vars_for_template(self):
        event = self.player.short_dscp
        return dict(
            event=event
        )


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


class Rest(Page):
    def is_displayed(self):
        A = self.round_number % 2 == 0
        B = self.round_number != len(self.participant.vars['emotions'])
        return A & B

    def vars_for_template(self):
        return dict(
            left_percentage=round(((1 + self.round_number) * 100) / 9)
        )


page_sequence = [Instructions, Background, Emo_evoketion, Composition, Imagination, Question_filling, Description, Rest]
