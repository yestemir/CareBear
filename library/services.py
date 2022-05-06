import datetime

from django.db.models import Count, Avg, F

from library.models import Checkbox, UserBadge


class UserService:
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
        days_count = UserBadge.objects.filter(user_id=self.user_id).last().current_days_steak
        return {
            "current_day_steak" : days_count
        }

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
