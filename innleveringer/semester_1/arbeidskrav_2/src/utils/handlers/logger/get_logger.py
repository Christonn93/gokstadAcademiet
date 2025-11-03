import logging

def get_logger(name, level=logging.INFO):
    logg = logging.getLogger(name)
    logg.setLevel(level)

    if not logg.handlers:

        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('error.log')
        c_handler.setLevel(logging.WARNING)
        f_handler.setLevel(logging.ERROR)

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        logg.addHandler(c_handler)
        logg.addHandler(f_handler)

    return logg


logger = get_logger(__name__)
