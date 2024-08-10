import reflex as rx
from reflex_lottiefiles import LottieFiles

def loading():
    return rx.center(
        rx.vstack(
            rx.heading("Loading, please wait"),
            LottieFiles(
                src="https://lottie.host/5ff06a80-3f45-4dd3-8737-f4cf62ba3d48/X5hdVEjbNK.lottie",
                autoplay=True,
                loop=True,
                width="20vw",
                height="20vw",
            )
        ),
        
        width="100%",
        height="90vh"
        
    ),


