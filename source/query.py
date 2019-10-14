from datetime import datetime, timedelta
from webapp.models import Issue, Type, Project
from django.db.models import Q

# Задание №2 запрос 1
start_date=datetime.now()-timedelta(days=30)
end_date=datetime.now()
Issue.objects.filter(Q(status__status__icontains='Done') & Q(update__range=(start_date, end_date))


#Задание №2 запрос 2
Type.objects.filter(issues__project='3')

#Задание №2 запрос 3
Project.objects.filter(issues__description__icontains='create')

#Задание №2 бонус
Project.objects.filter(issues__status=3)