# This makes the config directory a Python package
from .database import DB_CONFIG

# You can also import other configs if you have them
# from .other_config import OTHER_CONFIG

__all__ = ['DB_CONFIG']