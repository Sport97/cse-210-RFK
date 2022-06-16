from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """Responsibility:


    Attributes:

    """

    def __init__(self):
        """Constructs a new Artifact."""
        self.actor = Actor()
        self.actor._text = ""
        self.actor._font_size = ""
        self.actor._color = ""
        self.actor._position = ""
        self.actor._message = ""

    # def set_text(self, text):
    #     return self.actor._text

    # def set_font_size(self, font_size):
    #     return self.actor._font_size

    # def set_color(self, color):
    #     return self.actor._color
    
    # def set_position(self, position):
    #     return self.actor._position

    # def get_position(self):
    #     # self.actor._position = position

    #     self.actor.get_position()

    def set_message(self, message):
        self.actor._message = message

        return message
    
    def get_message(self):
        return self.actor._message