import reflex as rx
from movie_streaming_site.state import State
from movie_streaming_site.components.search import search
from movie_streaming_site.components.moviecard import movie_card
@rx.page(route="/search/[query]", on_load=State.search_on_load)
def search_page():
    return rx.box(
        search(),
        rx.text(
            State.search_query,
            font_size="10.5vh",
            font_weight="800",
            padding_top="5vh"
        ),
        rx.desktop_only(
            rx.grid(
                
                rx.foreach(
                    State.search_results,
                    lambda info, index: movie_card(info["title"], info["year"], "", info["link"], info["poster"], description=info["description"])
                ),
                spacing="1.5vh",
                columns="4",
                width="100%"
            ),
        ),
        rx.mobile_and_tablet(
            rx.grid(
                
                rx.foreach(
                    State.search_results,
                    lambda info, index: movie_card(info["title"], info["year"], "", info["link"], info["poster"], description=info["description"])
                ),
                spacing="1.5vh",
                columns="1",
                width="100%"
            ),
        )
    )
        