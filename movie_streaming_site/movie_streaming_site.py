import reflex as rx
from movie_streaming_site.components.moviecard import movie_card
from movie_streaming_site.state import State
from movie_streaming_site.components.search import search
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
    wrapMode:rx.Var[str]
    autoplayInterval:rx.Var[int]
    scrollDistance:rx.Var[str]



@rx.page(on_load=State.on_load)
def index():
    return rx.box(
        
        rx.box(
            Slider(
                rx.image(src="https://media.themoviedb.org/t/p/w1920_and_h800_multi_faces/qGQf2OHIkoh89K8XeKQzhxczf96.jpg", width="110vw", height="108vh", object_fit = "cover"),
                rx.image(src="https://media.themoviedb.org/t/p/w1920_and_h800_multi_faces/stKGOm8UyhuLPR9sZLjs5AkmncA.jpg", width="110vw", height="108vh", object_fit = "cover"),
                rx.image(src="https://media.themoviedb.org/t/p/w1920_and_h800_multi_faces/eHz61dRrYZB16glXDttV0CnJf6j.jpg", width="110vw", height="108vh", object_fit = "cover"),
                rx.image(src="https://media.themoviedb.org/t/p/w1920_and_h800_multi_faces/mabuNsGJgRuCTuGqjFkWe1xdu19.jpg", width="110vw", height="108vh", object_fit = "cover"),
                autoplay=True,
                showDots=False,
                autoplayInterval=6000,
                scrollDistance="slide",
                wrapMode="wrap",
                overflow="hidden"
            ),
            
            
            rx.box(
                width="100vw",
                height="108vh",
                position="absolute",
                left="0",
                top="0",
                bg="linear-gradient(180deg,rgba(18, 18, 18, 0.25) 0%, rgba(18, 18, 18, 0.77) 50%, rgba(18, 18, 18, 0.90) 77%, #121212 93%)",
                overflow="hidden"
            ),
            motion(
                
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
                "OPENSTREAM",
                font_size="15vw",
                font_weight="bolder",
                text_wrap = "nowrap",
                letter_spacing = "-4px",
                color="white",
                position="absolute",
                left="2.5vw",
                top="20vh",
                width="85vw",
                height="30vh",
                line_height="10vw",
                display = ["block", "none", "none"]
            ),
            rx.heading(
                "Thousands of",
                font_size=["10vw", "12vw", "14vh"],
                font_weight="1000",
                text_wrap = "nowrap",
                color="white",
                position="absolute",
                left="7vw",
                top=["30vh","20vh", "20vh"],
                width=["85vw", "50vw","50vw"],
                height="30vh",
                line_height=["10vw", "10vw", "14vh"],
            ),
            rx.heading(
                "movies, right at",
                font_size=["10vw", "12vw", "14vh"],
                font_weight="1000",
                text_wrap = "nowrap",
                color="white",
                position="absolute",
                left="7vw",
                top=["39vh", "30vh", "34vh"],
                width=["85vw", "50vw","50vw"],
                height="30vh",
                line_height=["10vw", "10vw", "14vh"],
            ),
            rx.heading(
                "your fingertips",
                font_size=["10vw", "12vw", "14vh"],
                font_weight="1000",
                text_wrap = "nowrap",
                color="white",
                position="absolute",
                left="7vw",
                top=["48vh", "40vh", "48vh"],
                width=["85vw", "50vw","50vw"],
                height="30vh",
                line_height=["10vw", "10vw", "14vh"],
            ),
            search(),
            width="100vw",
            height="111vh",
            position="relative",
            overflow="hidden"
        ),
        
        rx.center(
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
            ),
            rx.desktop_only(
                rx.grid(
                    
                    rx.foreach(
                        State.now_playing,
                        lambda info, index: movie_card(info["title"], info["year"], f"{info['runtime']} mins", info["link"], info["poster"], description=info["description"])
                        
                    ),
                    spacing="1.5vh",
                    columns="4",
                    position="absolute",
                    left="1.5vw",
                    top="105vh",
                    width="100%",
                    overflow="hidden"
                    
                ),
            ),
            rx.mobile_and_tablet(
                rx.grid(
                    
                    rx.foreach(
                        State.now_playing,
                        lambda info, index: movie_card(info["title"], info["year"], f"{info['runtime']} mins", info["link"], info["poster"], description=info["description"])
                        
                    ),
                    spacing="1.5vh",
                    columns="1",
                    position="absolute",
                    left="1.5vw",
                    top="105vh",
                    width="100%",
                    overflow="hidden"
                    
                ),
            ),
            
            width="100%",
            overflow="hidden"
        ),
        
        bg="#121212",
        position="relative",
        overflow_x="hidden",
    )







Slider = slider.create

def testpage():
    return rx.box(
        Slider(
            rx.image(src="https://commerce.nearform.com/open-source/nuka-carousel/img/pexels-01.jpg"),
            rx.image(src="https://commerce.nearform.com/open-source/nuka-carousel/img/pexels-02.jpg"),
            rx.image(src="https://commerce.nearform.com/open-source/nuka-carousel/img/pexels-03.jpg"),
            rx.image(src="https://commerce.nearform.com/open-source/nuka-carousel/img/pexels-04.jpg"),
            autoplay=True,
            showDots=True,
            autoplayInterval=3000,
            wrapMode="wrap",
        )
    )



style = {
    "body":{
        "background-color":"#121212",
        "overflow":"hidden"
    },
    "html":{
        "overflow":"hidden"
    }
}

app = rx.App(style = style)
app.add_page(search_page)
app.add_page(movieplayer)
app.add_page(index)
app.add_page(testpage)