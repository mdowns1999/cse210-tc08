import random
import sys
from game import constants
from game.action import Action
from game.point import Point
from game.score import Score

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, score):

        self._score = score
        self._points = 0
        self._count = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        bricks = cast["brick"]

        # handles ball contacting paddle 
        paddle_position = paddle.get_position()
        paddle_x = paddle_position.get_x()
        paddle_y = paddle_position.get_y()

        for i in range(len(paddle.get_text()) + 1):
            if (ball.get_position().get_x() == paddle_x) and (ball.get_position().get_y() == paddle_y):
                # change ball velocity
                velocity = ball.get_velocity()
                x = (velocity.get_x()) 
                y = (velocity.get_y())

                if x == 1 and y == 1: 
                    velocity = Point(x, y * -1)

                elif x == -1 and y == 1:
                    velocity = Point(x, y * -1)

                ball.set_velocity(velocity)

            else:
                paddle_x += 1
            
        # handles ball contacting brick
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                # remove the brick
                bricks.remove(brick)

                self._points = 1
                # change ball velocity
                velocity = ball.get_velocity()
                x = (velocity.get_x()) 
                y = (velocity.get_y())

                if x == 1 and y == -1: 
                    velocity = Point(x, y * -1)

                elif x == -1 and y == -1:
                    velocity = Point(x, y * -1)

                elif x == 1 and y == 1:
                    velocity = Point(x, y * -1)
                
                elif x == -1 and y == 1:
                    velocity = Point(x, y * -1)
                
                ball.set_velocity(velocity)
                self._score.add_points(self._points)
        
        if ball.get_position().get_y() == constants.MAX_Y - 1:
            if self._count != 3:
                ball_x = int(constants.MAX_X / 2)
                ball_y = int(constants.MAX_Y / 2)
                position = Point(ball_x, ball_y)
                ball.set_position(position)

                paddle_x = int(constants.MAX_X / 2)
                paddle_y = int(constants.MAX_Y - 2)
                position = Point(paddle_x, paddle_y)
                paddle.set_position(position)

                self._count += 1

            else:
                print("Game over!")
                print(f"Final Score: {self._score.get_points()}")
                sys.exit()
        
        elif ball.get_position().get_x() == constants.MAX_X - 79:
            velocity = ball.get_velocity()
            x = (velocity.get_x()) 
            y = (velocity.get_y())

            if x == -1 and y == -1: 
                velocity = Point(x * -1, y)

            elif x == -1 and y == 1:
                velocity = Point(x * -1, y)
            
            ball.set_velocity(velocity)
        
        elif ball.get_position().get_x() == constants.MAX_X - 1:
            velocity = ball.get_velocity()
            x = (velocity.get_x()) 
            y = (velocity.get_y())

            if x == 1 and y == -1: 
                velocity = Point(x * -1, y)

            elif x == 1 and y == 1:
                velocity = Point(x * -1, y)

            ball.set_velocity(velocity)

        elif ball.get_position().get_y() == constants.MAX_Y - 19:
            velocity = ball.get_velocity()
            x = (velocity.get_x()) 
            y = (velocity.get_y())

            if x == 1 and y == -1: 
                velocity = Point(x, y * -1)

            elif x == -1 and y == -1:
                velocity = Point(x, y * -1)

            ball.set_velocity(velocity)
