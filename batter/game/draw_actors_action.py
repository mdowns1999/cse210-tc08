from game.action import Action
from game.score import Score

class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this class of
    objects is use an output service to draw all actors on the screen.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service, score):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
        self._score = score

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()
