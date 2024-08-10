import reflex as rx
import requests
import dotenv
import os
import json
dotenv.load_dotenv()
auth = os.environ.get("auth")
class State(rx.State):
    now_playing:list[dict[str, str]]
    
    def get_movie_data(self, id):
        url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
        response = requests.get(
            url,
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {auth}"
            }
        )
        data = json.loads(response.text)
        return data
    
    def get_now_playing_movies(self):
        url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
        response = requests.get(
            url,
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {auth}"
            }
        )
        data = json.loads(response.text)
        results = data["results"]
        
        
        result_list = []
        for result in results:
            result_list.append(
                {
                    "poster":f"https://image.tmdb.org/t/p/w300_and_h450_bestv2/{result['poster_path']}",
                    "title": result["title"],
                    "year":result["release_date"][:4],
                    "description":result["overview"],
                    "runtime":self.get_movie_data(result["id"])["runtime"]
                }
            )
        return result_list
    def on_load(self):
        self.now_playing = self.get_now_playing_movies()
    
    