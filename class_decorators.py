import logging
from os import path

file_path = path.abspath(__file__)
file_folder_path = path.dirname(file_path)
log_file_path = path.join(file_folder_path, "app.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class decorators:

    def __init__(self, fun):
        logging.info(f"Start the program")
        self.fun = fun

    def __call__(self, *args, **arkgs):
        logging.info("Entered in wrapped function")
        return self.fun(*args, **arkgs)


@decorators
def display(name, size):
    logging.info("Entered in display(original function)")
    logging.info(
        "the name of the display is {} and the size of the display is {}".format(
            name, size
        )
    )
    logging.info("End the program")


# display = decorators(display) #display --> act like instantce object
display("digita", 67)  # called --> the object with () -->called directly __call__()
