
def context(request):
    return {
        'on_page': request.session.get('total_page_visits')

            }
