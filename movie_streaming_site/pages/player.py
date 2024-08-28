import reflex as rx
from reflex_lottiefiles import LottieFiles
from movie_streaming_site.state import State 
from movie_streaming_site.components.search import search


@rx.page(route="/movieplayer/[movieid]", on_load=State.on_load)
def movieplayer():
    return rx.box(
        search(),
        
        rx.cond(
            State.loading,
            rx.center(
                rx.vstack(
                    rx.center(
                        rx.heading("Loading, please wait"),
                        width="90vw",
                    ),
                    LottieFiles(
                        src="https://lottie.host/5ff06a80-3f45-4dd3-8737-f4cf62ba3d48/X5hdVEjbNK.lottie",
                        autoplay=True,
                        loop=True,
                        width="90vw",
                        height=["40vh", "40vh", "40vh"],
                    )
                ),
                
                width="90vw",
                height="80vh"
                
            ),

            
            rx.box(
                rx.text(State.current_movie["title"], font_size="10.5vh", font_weight="800"),
                rx.hstack(
                    rx.desktop_only(
                        rx.html(
                            State.movie_iframe,
                            width="50vw"
                        ),
                    ),
                    rx.mobile_and_tablet(
                        rx.html(
                            State.movie_iframe,
                            width="85vw"
                        ),
                    ),
                    #rx.box(width="960px", height="540px", bg="#D9D9D9"),
                    rx.desktop_only(
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
