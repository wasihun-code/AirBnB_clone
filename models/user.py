#!/usr/bin/python3
"""Documentation for user class."""


from base_model import BaseModel


class User(BaseModel):
    """Class user which inherits from baseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
