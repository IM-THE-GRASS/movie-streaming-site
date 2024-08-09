import reflex as rx

def footer():
    return rx.hstack(
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