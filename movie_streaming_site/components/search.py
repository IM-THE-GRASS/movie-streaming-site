import reflex as rx
from movie_streaming_site.state import State
from reflex_motion import motion
from movie_streaming_site.components.keybind import Keybind

def search():
    return rx.hstack(
        Keybind(
            keys=["Enter"],
            bind=State.go_search
        ),
        motion(
            rx.button(
                rx.icon(tag="search", color="white", size=30),
                variant="ghost",
                on_click=lambda: State.go_search("A")
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
        on_focus= State.search_focus,
        on_blur=State.search_blur,
        bg="rgba(0, 0, 0, 0.29)",
        border_radius="1087vh",
        padding="0.5vh",
        width=["90vw", "90vw", "48vw"],
        position="absolute",
        left=["5vw","5vw", "28vw"],
        top="2vh",
    ),