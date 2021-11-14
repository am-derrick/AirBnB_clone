#!/usr/bin/python3
"""Module for State class."""

from models.base_model import BaseModel

class State(BaseModel):
    """Class representing a State."""
    name = ""
    
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
