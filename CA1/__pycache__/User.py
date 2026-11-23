"""Define the user account model."""

class User:
    """Represent a user who can log in to the application."""

    def __init__(self, id, name, password):
        """Create a user with an ID, name, and password."""
        self.id = id
        self.name = name
        self.password = password