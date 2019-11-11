
def context(request):
    return {
        'on_page': request.session.get('total_page_visits'),
        'total': request.session.get('total')['total'],
        'all_time': request.session.get('all_time'),
        'page_time': request.session.get('page_time_visits')

            }
