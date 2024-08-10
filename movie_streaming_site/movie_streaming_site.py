import reflex as rx
from movie_streaming_site.components.moviecard import movie_card
from movie_streaming_site.state import State
from movie_streaming_site.components.search import search
from movie_streaming_site.components.footer import footer
from reflex_lottiefiles import LottieFiles

@rx.page(on_load=State.on_load)
def index():
    return rx.box(
        
        rx.box(
            rx.image(src="https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/8torndado.jpg", width="100vw", height="108vh"),
            
            rx.box(
                width="100vw",
                height="108vh",
                position="absolute",
                left="0",
                top="0",
                bg="linear-gradient(180deg, rgba(18, 18, 18, 0) 0%, rgba(18, 18, 18, 0.25) 37%, rgba(18, 18, 18, 0.77) 67%, rgba(18, 18, 18, 0.90) 77%, #121212 93%)",
            ),
           
            rx.button(
                "Watch Now",
                rx.icon(tag="circle_play", size=70),
                bg="#FFE066",
                color="black",
                font_size="5vh",
                font_weight="800",
                border_radius="9999px",
                border="0.7vh solid #2C2C2C",
                padding="1.5vh",
                position="absolute",
                left="7vw",
                top="70vh",
                width="24vw",
                height="16vh"
            ),
            rx.heading(
                "TORNADO MOVIE OR SOMETHING",
                font_size="14vh",
                font_weight="900",
                color="white",
                position="absolute",
                left="7vw",
                top="20vh",
                width="43vw",
                height="30vh",
                line_height="14vh"
            ),
            width="100vw",
            height="111vh",
            position="relative",
        ),
        search(),
        rx.center(
            rx.grid(
                rx.foreach(
                    State.now_playing,
                    lambda info, index: movie_card(info["title"], info["year"], f"{info['runtime']} mins", info["link"], info["poster"], description=info["description"])
                    
                ),
                footer(),
                spacing="1.5vh",
                columns="4",
                position="absolute",
                left="1.5vw",
                top="105vh",
                width="100%"
            ),
            width="100%",
        ),
        
        bg="#121212",
        position="relative",
        overflow_x="hidden"
    )



@rx.page(route="/movieplayer/[movieid]", on_load=State.on_load)
def movieplayer():
    return rx.box(
        search(),
        
        
        rx.cond(
            State.loading,
            rx.center(
                rx.vstack(
                    rx.heading("Loading, please wait"),
                    LottieFiles(
                        src="https://lottie.host/5ff06a80-3f45-4dd3-8737-f4cf62ba3d48/X5hdVEjbNK.lottie",
                        autoplay=True,
                        loop=True,
                        width="20vw",
                        height="20vw",
                    )
                ),
                
                width="100%",
                height="90vh"
            ),
            
            rx.box(
                rx.text(State.current_movie["title"], font_size="10.5vh", font_weight="800"),
                rx.hstack(
                    rx.html(
                        State.movie_iframe,
                        width="50vw",
                        height="60vw"
                    ),
                    #rx.box(width="960px", height="540px", bg="#D9D9D9"),
                    rx.vstack(
                        rx.text(
                            "Description",
                            color="white",
                            font_size="4vh",
                            font_weight="800"
                        ),
                        rx.text(
                            State.current_movie["description"],
                            color="white",
                            font_size="3vh",
                            max_width="28vw"
                        ),
                        align_items="flex-start",
                    ),
                    rx.desktop_only(
                        rx.vstack(
                            movie_info_item(State.current_movie["date"], "calendar"),
                            movie_info_item(State.current_movie["revenue"], "dollar-sign"),
                            movie_info_item(State.current_movie["runtime"], "clock"),
                            
                            rx.cond(
                                State.current_movie["site"],
                                rx.link(
                                    movie_info_item("Site", "globe"),
                                    href=State.current_movie["site"],
                                    is_external=True
                                ),
                            ),
                            rx.cond(
                                State.current_movie["tmdb_link"],
                                rx.link(
                                    movie_info_item("TMDB", "clock"),
                                    href=State.current_movie["tmdb_link"],
                                    is_external=True
                                ),
                            ),
                            rx.cond(
                                State.current_movie["imdb_link"],
                                rx.link(
                                    movie_info_item("IMDB", "clock"),
                                    href=State.current_movie["imdb_link"],
                                    is_external=True
                                )
                            )
                            
                            
                            
                        ),
                    ),
                    
                    spacing="2vw",
                ),
            )
        ),
        
       
       
        width = "100%",
        padding="5.5vh",
    )

def movie_info_item(text, icon):
    return rx.hstack(
        rx.center(
            rx.icon(
                icon,
            ),
           
        ),
        rx.center(
            rx.text(text, color="white", font_size="2.5vh"),
        ),
       
        spacing="1vw",
    )





style = {
    "body":{
        "background-color":"#121212"
    }
}

app = rx.App(style = style)
app.add_page(index)