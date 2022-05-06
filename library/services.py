import datetime

from django.db.models import Count, Avg

from library.models import Checkbox


class CheckboxService:
    def __init__(self):
        pass

    def get_statistics(self):
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        checkboxes = Checkbox.objects.select_related('user_id', 'health_status')
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
