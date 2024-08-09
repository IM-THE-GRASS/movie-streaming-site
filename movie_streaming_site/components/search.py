import reflex as rx

def search():
    return rx.hstack(
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