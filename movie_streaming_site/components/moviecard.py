import reflex as rx
def movie_card(title: str, year: str, duration: str, img:str = "https://via.placeholder.com/316x421", description:str = ""):
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.box(
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
            ),
        ),
        rx.hover_card.content(
            rx.hstack(
                rx.vstack(
                    rx.heading(
                        title,
                        width="30vh"
                    ),
                    rx.image(
                        src=img,
                        width="30vh"
                    ),
                    width="90vh"
                ),
                rx.text(
                    description
                )
            ),
            side="right"
        ),
        
    )

    