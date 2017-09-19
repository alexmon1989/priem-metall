from django.conf import settings


def google_analytics_id(request):
    """Возвращает значение id в сервисе Google Analytics."""
    try:
        return {'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID}
    except AttributeError:
        return {'GOOGLE_ANALYTICS_ID': None}
