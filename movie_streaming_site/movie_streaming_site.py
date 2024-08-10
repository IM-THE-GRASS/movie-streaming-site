import reflex as rx
from movie_streaming_site.components.moviecard import movie_card
from movie_streaming_site.state import State
from movie_streaming_site.components.search import search
from movie_streaming_site.components.footer import footer


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
                    lambda info, index: movie_card(info["title"], info["year"], f"{info['runtime']} mins", info["poster"], description=info["description"])
                    
                ),
                # movie_card("Borderlands", "2024", "1 hr 31 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/7borders.jpg"),
                # movie_card("Dealpool & Wolverine", "2024", "1 hr 21 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/3dead_and_wolv.jpg"),
                # movie_card("Despicable Me 4", "2024", "1 hr 35 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/4minions_wer_despicible.jpg"),
                # movie_card("Joe Rogan", "2024", "1 hr 23 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/6joe.jpg"),
                # movie_card("Trap", "2024", "2 hr 41 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/5trap.jpg"),
                # movie_card("The Garfield Move", "2024", "101 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/2garlf.jpg"),
                # movie_card("Inside Out 2", "2024", "1 hr 31 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/1inside_out_2.jpg"),
                # movie_card("The Super Mario Bros Movie", "2023", "93 min", "https://cloud-6t0bvxvfn-hack-club-bot.vercel.app/0maro.jpg"),
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




def movieplayer():
    return rx.box(
        search(),
        rx.text("Despicable Me 4", font_size="96px", font_weight="800"),
        rx.hstack(
            rx.box(width="960px", height="540px", bg="#D9D9D9"),
            rx.vstack(
                rx.text(
                    "Description",
                    color="white",
                    font_size="40px",
                    font_weight="800"
                ),
                rx.text(
                    "Gru and Lucy and their girls---Margo, Edith and Agnes---welcome a new "
                    "member to the Gru family, Gru Jr., who is intent on tormenting his dad. "
                    "Gru also faces a new nemesis in Maxime Le Mal and his femme fatale "
                    "girlfriend Valentina, forcing the family to go on the run.",
                    color="white",
                    font_size="24px",
                    max_width="536px"
                ),
                align_items="flex-start",
            ),
            rx.vstack(
                movie_info_item("2024-06-20", "calendar"),
                movie_info_item("$100,000,000", "calendar"),
                movie_info_item("94min", "clock"),
                movie_info_item("Site", "globe"),
                movie_info_item("IMDB", "clock"),
                movie_info_item("TMDB", "clock"),
            ),
            spacing="40px",
        ),
        
        width="100%",
        padding="50px",
    )

def movie_info_item(text, icon):
    return rx.hstack(
        rx.icon(
            icon,
            color="#F5F5F5",
            bg="#2C2C2C",
            padding="12px",
            border_radius="32px",
        ),
        rx.text(text, color="white", font_size="24px"),
        spacing="12px",
    )





style = {
    "body":{
        "background-color":"#121212"
    }
}

app = rx.App(style = style)
app.add_page(index)
app.add_page(movieplayer)