from django.http import JsonResponse
from django.views import View

from .models import City
from .utils import calculate_score


class SuggestionsView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)

        suggestions = []
        for city in City.objects.filter(name__icontains=q):
            score = calculate_score(city, q, latitude, longitude)
            suggestion = {
                'name': city.name,
                'latitude': city.latitude,
                'longitude': city.longitude,
                'score': score
            }
            suggestions.append(suggestion)

        # Sort suggestions by score in descending order
        suggestions.sort(key=lambda x: x['score'], reverse=True)

        return JsonResponse({'suggestions': suggestions})
