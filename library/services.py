import datetime

from django.db.models import Count, Avg, F

from library.models import Checkbox, UserBadge, HealthStatus, Test
from rest_framework import serializers

class UserService:
    min_result = 0
    max_result = 0

    def __init__(self, user_id: int):
        self.user_id = user_id

    def create_badges_entity(self) -> None:
        UserBadge.objects.create(user_id=self.user_id, current_days_steak=1, date=datetime.date.today())

    def update_day_steak(self):
        if UserBadge.objects.filter(user_id=self.user_id).last() is None:
            self.create_badges_entity()
        else:
            user_badge = UserBadge.objects.filter(user_id=self.user_id)
            if user_badge.last().date == datetime.date.today() - datetime.timedelta(days=1):
                user_badge.update(current_days_steak=F('current_days_steak') + 1)
            else:
                user_badge.update(current_days_steak=1)

    def get_current_day_steak(self) -> dict:
        if UserBadge.objects.filter(user_id=self.user_id).last() is None:
            self.create_badges_entity()
            days_count = 1
        else:
            days_count = UserBadge.objects.filter(user_id=self.user_id).last().current_days_steak
        return {
            "current_day_steak": days_count
        }

    def check_if_perfect_day(self, checkbox_id: int):
        health_status_id = Checkbox.objects.filter(id=checkbox_id).last().health_status_id
        total = Checkbox.objects.filter(health_status_id=health_status_id).aggregate(total=Count('id'))['total']
        completed = Checkbox.objects.filter(health_status_id=health_status_id, done=True).aggregate(
            completed=Count('id')
        )['completed']
        return total == completed

    def get_statistics(self):
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        checkboxes = Checkbox.objects.filter(user_id=self.user_id).select_related('user_id', 'health_status')
        number_of_total_tasks = checkboxes.aggregate(Count('id'))
        number_of_total_completed_tasks = checkboxes.filter(done=True).aggregate(Count('id'))
        number_of_weeks_total_tasks = checkboxes.filter(health_status__date__range=[start_week, end_week]).aggregate(Count('id'))
        number_of_weeks_completed_tasks = checkboxes.filter(health_status__date__range=[start_week, end_week], done=True).aggregate(Count('id'))
        number_of_todays_total_tasks = checkboxes.filter(health_status__date=date).aggregate(Count('id'))
        number_of_todays_completed_tasks = checkboxes.filter(health_status__date=date, done=True).aggregate(Count('id'))
        number_of_good_days = checkboxes.filter(health_status__mood_percentage__gte=60).aggregate(Count('id'))
        # number_of_perfect_days =
        average_mood_percent = checkboxes.aggregate(Avg('health_status__mood_percentage'))
        return {
            "number_of_total_tasks": number_of_total_tasks['id__count'],
            "number_of_total_completed_tasks": number_of_total_completed_tasks['id__count'],
            "number_of_weeks_total_tasks": number_of_weeks_total_tasks['id__count'],
            "number_of_weeks_completed_tasks": number_of_weeks_completed_tasks['id__count'],
            "number_of_todays_total_tasks": number_of_todays_total_tasks['id__count'],
            "number_of_todays_completed_tasks": number_of_todays_completed_tasks['id__count'],
            "number_of_good_days": number_of_good_days['id__count'],
            "average_mood_percent": average_mood_percent['health_status__mood_percentage__avg'],
        }

    def get_statistics_last_week(self):
        date = datetime.date.today()
        health_status = HealthStatus.objects.filter(user_id=self.user_id)
        seven_days_ago = 0
        six_days_ago = 0
        five_days_ago = 0
        four_days_ago = 0
        three_days_ago = 0
        two_days_ago = 0
        one_day_ago = 0
        if health_status.filter(date__exact=date - datetime.timedelta(days=7)).first() is not None:
            seven_days_ago = health_status.filter(date__exact=date - datetime.timedelta(days=7)).first().mood_percentage
        if health_status.filter(date__exact=date - datetime.timedelta(days=6)).first() is not None:
            six_days_ago = health_status.filter(date__exact=date - datetime.timedelta(days=6)).first().mood_percentage
        if health_status.filter(date__exact=date - datetime.timedelta(days=5)).first() is not None:
            five_days_ago = health_status.filter(date__exact=date - datetime.timedelta(days=5)).first().mood_percentage
        if health_status.filter(date__exact=date - datetime.timedelta(days=4)).first() is not None:
            four_days_ago = health_status.filter(date__exact=date - datetime.timedelta(days=4)).first().mood_percentage
        if health_status.filter(date__exact=date - datetime.timedelta(days=3)).first() is not None:
            three_days_ago = health_status.filter(date__exact=date - datetime.timedelta(days=3)).first().mood_percentage
        if health_status.filter(date__exact=date - datetime.timedelta(days=2)).first() is not None:
            two_days_ago = health_status.filter(date__exact=date - datetime.timedelta(days=2)).first().mood_percentage
        if health_status.filter(date__exact=date - datetime.timedelta(days=1)).first() is not None:
            one_day_ago = health_status.filter(date__exact=date - datetime.timedelta(days=1)).first().mood_percentage

        return {
            "seven_days_ago": seven_days_ago,
            "six_days_ago": six_days_ago,
            "five_days_ago": five_days_ago,
            "four_days_ago": four_days_ago,
            "three_days_ago": three_days_ago,
            "two_days_ago": two_days_ago,
            "one_day_ago": one_day_ago,
        }

    def get_test(self):
        # date = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
        test = Test.objects.filter(user_id=self.user_id)

        questions = [
            'Little interest or pleasure in doing things',
            'Feeling down, depressed, or hopeless',
            'Trouble falling or staying asleep, or sleeping too much',
            'Feeling tired or having little energy',
            'Poor appetite or everything',
            'Feeling bad about yourself-or that you are a failure or have let yourself or your family down',
            'Trouble concentrating on things, such as reading the newspaper or watching television',
            'Moving or speaking noticeably slower than usual or the opposite - faster than usual',
            'Thoughts that you would be better off dead or of hurting yourself in some way',
        ]
        # titles = [
        #     'Minimal or no symptoms of depression',
        #     'Mild depression',
        #     'Moderate depression',
        #     'Moderately severe depression',
        #     'Severe depression'
        # ]
        # description = [
        #     'Your results suggest minimal or no symptoms of depression.',
        #     'Your results suggest that you may be experiencing some symptoms of mild depression.While your symptoms are likely not having a major impact on your life, it is important to monitor them. If you have been mildly depressed for a period of a few months, consider talking to your doctor about Dysthymia.',
        #     'Your results suggest that you may be suffering from moderate depression.While this is not a diagnostic test, it might be worthwhile to start a conversation with your doctor of a trained mental health professional. Finding the right treatment plan can help you feel more like you again.',
        #     'Your results suggest that you may be suffering from moderate severe depression.While this is not a diagnostic test, people who scored similar to you typically receive a diagnosis of major depression and have sought professional treatment for this disorder. It would likely be beneficial for you to consult a trained mental professional immediately.',
        #     'Your results suggest that you may be suffering from moderate severe depression.While this is not a diagnostic test, people who scored similar to you typically receive a diagnosis of major depression and have sought professional treatment for this disorder. It would likely be beneficial for you to consult a trained mental professional immediately.',
        # ]

        # id_for_title = 0

        # if test.last().result % 5 == 0:
        #     id_for_title = test.last().result // 5 - 1
        # else:
        #     id_for_title = test.last().result // 5

        # self.min_result = min(test.last().result, self.min_result)
        # self.max_result = max(test.last().result, self.max_result)

        return {
            "questions": questions,
            # "time": test.last().date.__format__("%Y-%m-%d %H:%M"),
            # "result": test.last().result,
            # "max_result": self.max_result,
            # "min_result": self.min_result,
            # "result_title": titles[id_for_title],
            # "result_description": description[id_for_title],
        }
