# from django.http import JsonResponse
# from django.views import View
# from .recommenderSystem import GameRecommended  # Import the function from test.py
# import requests
# class RecommendationView(View):
#
#     def fetch_image_url(self,game_name: str):
#         api_key = 'YOUR_BING_API_KEY'
#         search_url = "https://api.bing.microsoft.com/v7.0/images/search"
#         headers = {"Ocp-Apim-Subscription-Key": api_key}
#         params = {"q": game_name, "license": "public", "imageType": "photo"}
#         response = requests.get(search_url, headers=headers, params=params)
#         response.raise_for_status()
#         search_results = response.json()
#         if search_results["value"]:
#             return search_results["value"][0]["contentUrl"]
#         return None
#
#     def get(self, request, game_name):
#         try:
#             recommendations = GameRecommended(game_name.lower())
#             response_data = recommendations.to_dict(orient='records')
#             for game in response_data:
#                 print(game['Game'])
#             return JsonResponse({'recommendations': response_data}, safe=False)
#         except KeyError:
#             return JsonResponse({'error': 'Game not found'}, status=404)


from django.http import JsonResponse
from django.views import View
from .recommenderSystem import GameRecommended  # Import the function from test.py
import requests


class RecommendationView(View):
    def get(self, request):
        try:
            game_name = request.GET['game_name']
            recommendations = GameRecommended(game_name.lower())
            response_data = recommendations.to_dict(orient='records')

            # Fetch images for each recommended game
            for game in response_data:
                image_url = self.fetch_game_image(game['Game'])
                game['Image'] = image_url

            return JsonResponse({'recommendations': response_data}, safe=False)
        except KeyError:
            return JsonResponse({'error': 'Game not found'}, status=404)

    def fetch_game_image(self, game_name):
        api_key = 'AIzaSyDSQixL83HanPv_68QdMjrj1Orb49VRzvw'
        engine_id = '3608f5ada5ef24a14'
        search_url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={engine_id}&q={game_name}&searchType=image&num=1'

        try:
            response = requests.get(search_url)
            if response.status_code == 200:
                data = response.json()
                if 'items' in data and data['items']:
                    image_url = data['items'][0]['link']
                    return image_url
        except requests.RequestException as e:
            print(f"Error fetching image for {game_name}: {e}")

        return None
