

class GameObjectModel():
    def __init__(self):
        return

    position = {
        'x': 0,
        'y': 0
    }

    velocity = {
        'x': 0,
        'y': 0
    }
    
    speed = 0
    acceleration = 0
    deceleration = 0
    isAffectedGravity = False
    isGroundBound = True
    moveState = "idle"
    rotation = 0
    isMovingRight = False
    isMovingLeft = False
    isMovingUp = False
    isMovingDown = False
