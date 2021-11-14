#!/usr/bin/python3
"""Documentation for Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from basemodel class"""

    place_id = ""
    user_id = ""
    text = ""
