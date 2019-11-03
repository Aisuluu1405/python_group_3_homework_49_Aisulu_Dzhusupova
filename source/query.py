from datetime import datetime, timedelta
from webapp.models import Issue, Type, Project, Team
from django.db.models import Q

# Задание №2 запрос 1
start_date=datetime.now()-timedelta(days=30)
end_date=datetime.now()
Issue.objects.filter(Q(status__status__icontains='Done') & Q(update__range=(start_date, end_date)))


#Задание №2 запрос 2
Type.objects.filter(issues__project__project__icontains='Loans')

#Задание №2 запрос 3
Project.objects.filter(issues__description__icontains='create')

#Задание №2 бонус
Project.objects.filter(issues__status__status__contains='Done').values('project')

q_1=Project.objects.filter(project_team__user__username='Aidin')
q_2=Project.objects.filter(user)
q_1 = Team.objects.filter(user__user_profiles='2')
T