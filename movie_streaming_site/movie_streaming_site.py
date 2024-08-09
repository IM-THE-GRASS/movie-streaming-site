import reflex as rx
from movie_streaming_site.components.moviecard import movie_card
from movie_streaming_site.state import State





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
        rx.hstack(
            rx.icon(tag="search", color="white", size=30),
            rx.input(
                placeholder="Search",
                color="white",
                font_size="3.5vh",
                width="100%",
                background_color="rgba(255, 255, 255, 0)",
                border="none",
                border_width="0px",
                height="30"
            ),
            bg="rgba(0, 0, 0, 0.29)",
            border_radius="1087vh",
            padding="0.5vh",
            width="48vw",
            position="absolute",
            left="28vw",
            top="2vh",
        ),
        rx.center(
            rx.grid(
                movie_card("Borderlands", "2024", "1 hr 31 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/7borders.jpg"),
                movie_card("Dealpool & Wolverine", "2024", "1 hr 21 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/3dead_and_wolv.jpg"),
                movie_card("Despicable Me 4", "2024", "1 hr 35 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/4minions_wer_despicible.jpg"),
                movie_card("Joe Rogan", "2024", "1 hr 23 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/6joe.jpg"),
                movie_card("Trap", "2024", "2 hr 41 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/5trap.jpg"),
                movie_card("The Garfield Move", "2024", "101 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/2garlf.jpg"),
                movie_card("Inside Out 2", "2024", "1 hr 31 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/1inside_out_2.jpg"),
                movie_card("The Super Mario Bros Movie", "2023", "93 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/0maro.jpg"),
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "API attribution:",
                            font_size= "4vh",
                            font_weight="900",
                        ),
                        rx.link(
                            rx.image(
                            "https://www.themoviedb.org/assets/2/v4/logos/v2/blue_long_2-9665a76b1ae401a510ec1e0ca40ddcb3b0cfe45f1d51b77a308fea0845885648.svg",
                            height="4vh",

                            ),
                            href="https://www.themoviedb.org",
                            
                        ),
                        rx.link(
                            rx.image(
                                "https://moviesapi.club/assets/images/logo.png",
                                height="6vh",

                            ),   
                            href="https://moviesapi.club",
                            
                        ),
                    ),
                    rx.center(
                        rx.text(
                            "Movie Streaming Site",
                            font_size= "9vh",
                            font_weight="900",
                        ),
                        height="100%",
                        width="100%"
                    ),
                    
                    rx.center(
                        rx.vstack(
                            rx.text(
                                "Made with: ",
                                font_size= "4vh",
                                font_weight="900",
                            ),
                            rx.link(
                                rx.image(
                                    "https://reflex.dev/logos/dark/reflex.svg",
                                    height="4vh",
                                ),
                                href="https://reflex.dev",
                                
                            ),
                        ),
                        pading_right="5vw",
                        height="100%",
                        width="15vw"
                    ),
                    
                    background_color="rgba(255,255,255,0.02)",
                    left="-1.5vw",
                    position="relative",
                    width="100vw",
                    height="20vh"
                ),
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

style = {
    "body":{
        "background-color":"#121212"
    }
}

app = rx.App(style = style)
app.add_page(index)