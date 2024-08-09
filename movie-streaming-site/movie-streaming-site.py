import reflex as rx

class State(rx.State):
    pass

def movie_card(title: str, year: str, duration: str):
    return rx.box(
        rx.image(src="https://via.placeholder.com/316x421", width="316px", height="421px"),
        rx.vstack(
            rx.hstack(
                rx.text(year, color="#C0C0C0", font_size="20px", font_style="italic"),
                rx.text(duration, color="#C0C0C0", font_size="20px", font_style="italic", text_align="right"),
                width="100%"
            ),
            rx.heading(title, color="#F2F2F2", font_size="36px", font_weight="800"),
            spacing="4px",
            align_items="flex-start",
            padding="16px",
        ),
        padding="1vw",
        width="370px",
        height="555px",
        bg="#1A1A1A",
        border_radius="8px",
        border="1px solid #D9D9D9",
    )

def index():
    return rx.box(
        rx.box(
            rx.image(src="https://via.placeholder.com/1920x994", width="1920px", height="994px"),
            rx.box(
                width="1920px",
                height="994px",
                position="absolute",
                left="0",
                top="0",
                bg="linear-gradient(180deg, rgba(18, 18, 18, 0) 0%, rgba(18, 18, 18, 0.25) 37%, rgba(18, 18, 18, 0.77) 67%, rgba(18, 18, 18, 0.90) 77%, #121212 93%)",
            ),
            
            rx.button(
                "Watch Now",
                rx.icon(tag="play", size=70),
                bg="#FFE066",
                color="black",
                font_size="48px",
                font_weight="800",
                border_radius="1000px",
                border="6px solid #2C2C2C",
                padding="12px",
                position="absolute",
                left="130px",
                top="650px",
                width="462px",
                height="149px"
            ),
            rx.heading(
                "TORNADO MOVIE OR SOMETHING",
                font_size="128px",
                font_weight="900",
                color="white",
                position="absolute",
                left="130px",
                top="197px",
                width="830px",
                height="265px",
                line_height="128px"
            ),
            width="1920px",
            height="994px",
            position="relative",
        ),
        rx.hstack(
            rx.icon(tag="search", color="white"),
            rx.input(placeholder="Search", color="white", font_size="32px", width="100%", type="ghost"),
            bg="rgba(0, 0, 0, 0.29)",
            border_radius="9999px",
            padding="6px",
            width="924px",
            position="absolute",
            left="28vw",
            top="2vh",
        ),
        rx.grid(
            movie_card("Borderlands", "2024", "1 hr 31 min"),
            movie_card("Dealpool & Wolverine", "2024", "1 hr 21 min"),
            movie_card("Despicable Me 4", "2024", "1 hr 35 min"),
            movie_card("Joe Rogan", "2024", "1 hr 23 min"),
            movie_card("Trap", "2024", "2 hr 41 min"),
            movie_card("The Garfield Move", "2024", "101 min"),
            movie_card("Inside Out 2", "2024", "1 hr 31 min"),
            movie_card("The Mario Movie", "2023", "93 min"),
            spacing="24px",
            columns="4",
            position="absolute",
            left="24px",
            top="967px",
            width="100%"
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