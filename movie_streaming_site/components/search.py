import reflex as rx
from movie_streaming_site.state import State
from reflex_motion import motion

def search():
    return rx.hstack(
        motion(
            rx.link(
                rx.icon(tag="search", color="white", size=30),
                href=State.search_url
            ),
            while_hover={"scale": 1.05},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        motion(
            rx.input(
                placeholder="Search",
                color="white",
                font_size="3.5vh",
                width="100%",
                background_color="rgba(255, 255, 255, 0)",
                border="none",
                border_width="0px",
                height="30",
                value=State.search_value,
                on_change=State.change_search_value
            ),
            width="100%",
            while_hover={"scale": 1.02},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        
        bg="rgba(0, 0, 0, 0.29)",
        border_radius="1087vh",
        padding="0.5vh",
        width="48vw",
        position="absolute",
        left="28vw",
        top="2vh",
    ),