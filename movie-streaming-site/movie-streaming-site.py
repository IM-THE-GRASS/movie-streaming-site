import reflex as rx

class State(rx.State):
    pass

def movie_card(title: str, year: str, duration: str, img:str = "https://via.placeholder.com/316x421"):
    return rx.box(
        rx.image(src=img, width="17vw", height="47vh"),
        rx.vstack(
            rx.hstack(
                rx.text(year, color="#C0C0C0", font_size="2vh", font_style="italic"),
                rx.text(duration, color="#C0C0C0", font_size="2vh", font_style="italic", text_align="right", width="100%"),
                width="100%"
            ),
            rx.heading(title, color="#F2F2F2", font_size="4vh", font_weight="800"),
            spacing="0.5vh",
            align_items="flex-start",
            padding="1.7vh",
        ),
        padding="1vw",
        width="19vw",
        #height="60.4vh",
        bg="#1A1A1A",
        border_radius="1vh",
        #border="0.1vh solid #D9D9D9",
    )



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