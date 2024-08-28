import reflex as rx
import requests
import dotenv
import os
import json
dotenv.load_dotenv()
auth = os.environ.get("auth")
class State(rx.State):
    now_playing:list[dict[str, str]]
    movie_iframe:str
    current_movie:dict[str, str]
    loading:bool = True
    search_results:list[dict[str, str]]
    search_focused:bool = False
    search_value:str
    def change_search_value(self, new):
        self.search_value = new
        
    @rx.var
    def search_url(self) -> str:
        return f"/search/{self.search_value}/"
    
    def search_focus(self):
        self.search_focused = True
    def search_blur(self):
        self.search_focused = False
    
    def go_search(self, _):
        if self.search_value and self.search_focused:
            return rx.redirect(f"/search/{self.search_value}/")
    
    
    @rx.var
    def search_query(self) -> str:
        
        return self.router.page.params.get("query", "")
    @rx.var
    def movie_id(self) -> str:
        
        return self.router.page.params.get("movieid", "")
    
    def search(self, query):
        url = f"https://api.themoviedb.org/3/search/movie?query={query}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.environ.get('auth')}"
        }

        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        print(data)
        results = data["results"]
        for result in results:
            result.pop("adult")
            result.pop("genre_ids")
            result["id"] = str(result["id"])
            result.pop("original_language")
            result.pop("original_title")
            result.pop("popularity")
            result["year"] = result["release_date"][:4]
            result.pop("release_date")
            result.pop("video")
            result.pop("vote_average")
            result.pop("vote_count")
            result["link"] = f"/movieplayer/{result['id']}"
            result["description"] = result["overview"]
            result["poster"] = f"https://image.tmdb.org/t/p/w300_and_h450_bestv2/{result['poster_path']}"
        print(results)
        return results
    
    
    def search_on_load(self):
        print(f"Searched for {self.search_query}")
        self.search_results = self.search(self.search_query)
    
    
    
    def get_current_movie(self):
        movie_id = self.movie_id
        data = self.get_movie_data(movie_id)
        print(data)
        try:
            result = {
                
                
                "imdb_link":f"https://www.imdb.com/title/{data['imdb_id']}/",
                "tmdb_link":f"https://www.themoviedb.org/movie/{data['id']}",
                "description":data["overview"],
                "runtime":f"{data['runtime']} min",
                "revenue":f"${data['revenue']}",
                "title":data["title"],
                "date":data["release_date"]
            }
        except:
            return
        try:
            result["site"]= data["homepage"]
        except:
            pass
        return result
        
    
    
    
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
                    "runtime":self.get_movie_data(result["id"])["runtime"],
                    "link":f"/movieplayer/{result['id']}"
                }
            )
        return result_list
    def on_load(self):
        self.loading = True
        print("start load")
        self.movie_iframe = f' <iframe src="https://moviesapi.club/movie/' + self.router.page.params.get("movieid", "123456") + '" frameborder="0" allowFullScreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" style="height:60vh; width:100%"></iframe>'
        print("load iframe")
        self.now_playing = self.get_now_playing_movies()
        print("load now playing")
        self.current_movie = self.get_current_movie()
        print("load current")
        self.loading=False
        return rx.toast("This website is for educational purposes only, I am not distrubuiting these movies, this is just a wrapper for https://moviesapi.club", duration=5000)
    
    