import arcade

import Constants as C

class Sprite(arcade.Sprite):
    def __init__(self, modelReference, defaultSprite):
        self.modelReference = modelReference
        self.lastKnownMoveState = self.modelReference.moveState

        super().__init__()
        self.texture = arcade.load_texture(defaultSprite)
        self.x_odometer = 0
        self.character_face_direction = C.RIGHT_FACING

    def on_update(self, dt):
        if self.lastKnownMoveState != self.modelReference.moveState:
            self.currentSpriteIndex = 0
            self.lastKnownMoveState = self.modelReference.moveState
        if self.timeSinceLastSpriteChange + dt >= self.spriteRotateDT:
            self.spriteSwap()
            img = self.spritesList[self.modelReference.moveState][self.currentSpriteIndex]
            self.texture = arcade.load_texture(img)
            self.timeSinceLastSpriteChange = 0
        else:
            self.timeSinceLastSpriteChange += dt

    def on_keypress(self, symbol, modifiers):
        return

    def spriteSwap(self):
        if (self.currentSpriteIndex + 1 >= len(self.spritesList[self.modelReference.moveState])-1):
            self.currentSpriteIndex = 1
        else:
            self.currentSpriteIndex += 1

    def pymunk_moved(self, physics_engine, dx, dy, d_angle):
        """ Handle being moved by the pymunk engine """
        # Figure out if we need to face left or right
        if dx < -C.DEAD_ZONE and self.character_face_direction == C.RIGHT_FACING:
            self.character_face_direction = C.LEFT_FACING
        elif dx > C.DEAD_ZONE and self.character_face_direction == C.LEFT_FACING:
            self.character_face_direction = C.RIGHT_FACING

        is_on_ground = physics_engine.is_on_ground(self)

        # Add to the odometer how far we've moved
        self.x_odometer += dx

        # Jumping animation
        if not is_on_ground:
            if dy > C.DEAD_ZONE:
                self.modelReference.moveState = "jump"
                return
            elif dy < -C.DEAD_ZONE:
                self.modelReference.moveState = "jump"
                return

        # Idle animation
        if abs(dx) <= C.DEAD_ZONE:
            self.modelReference.moveState = "idle"
            return

        # Have we moved far enough to change the texture?
        if abs(self.x_odometer) > C.DISTANCE_TO_CHANGE_TEXTURE:
            self.x_odometer = 0
            self.modelReference.moveState = "walk"

    #GameWindowReference = None
    timeSinceLastSpriteChange = 0
    currentSpriteIndex = 1
    lastKnownMoveState = None
    spriteRotateDT = .15
    modelReference = None
    spritesList = {
        "idle": [],
        "walk": [],
        "run": [],
        "jump": []
    }