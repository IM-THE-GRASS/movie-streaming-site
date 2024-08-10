import reflex as rx
from movie_streaming_site.components.moviecard import movie_card
from movie_streaming_site.state import State
from movie_streaming_site.components.search import search
from movie_streaming_site.components.footer import footer
from reflex_lottiefiles import LottieFiles
from movie_streaming_site.components.loading import loading
from movie_streaming_site.pages.player import movieplayer
from movie_streaming_site.pages.search import search_page
from reflex_motion import motion

class slider(rx.Component):
    library = "nuka-carousel"
    tag = "Carousel"
    autoplay:rx.Var[bool]
    showDots:rx.Var[bool]
    autoplayInterval:rx.Var[int]


Slider = slider.create


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
            motion(
                
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
                    width="24vw",
                    height="16vh"
                ),
                position="absolute",
                left="7vw",
                top="70vh",
                width="24vw",
                height="16vh",
                while_hover={"scale": 1.2},
                while_tap={"scale": 0.9},
                transition={"type": "spring", "stiffness": 400, "damping": 17},
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
                    height="90vh",
                    margin_bottom="20vh"
                ),

            ),
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



def testpage():
    return rx.box(
        Slider(
            rx.image(src="https://commerce.nearform.com/open-source/nuka-carousel/img/pexels-01.jpg"),
            rx.image(src="https://commerce.nearform.com/open-source/nuka-carousel/img/pexels-01.jpg"),
            autoplay=True,
            showDots=True,
            autoplayInterval=3000
        )
    )




style = {
    "body":{
        "background-color":"#121212"
    }
}

app = rx.App(style = style)
app.add_page(search_page)
app.add_page(movieplayer)
app.add_page(index)
app.add_page(testpage)