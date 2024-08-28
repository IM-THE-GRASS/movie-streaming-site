import reflex as rx
from reflex_lottiefiles import LottieFiles

def loading():
    rx.center(
        rx.vstack(
            rx.center(
                rx.heading("Loading, please wait"),
                width="90vw",
            ),
            LottieFiles(
                src="https://lottie.host/5ff06a80-3f45-4dd3-8737-f4cf62ba3d48/X5hdVEjbNK.lottie",
                autoplay=True,
                loop=True,
                width="90vw",
                height=["40vh", "40vh", "40vh"],
            )
        ),
        
        width="90vw",
        height="80vh"
        
    ),


