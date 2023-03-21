import Constants as C

class GameObjectController:
    
    def on_update(self, dt):
        self.update_velocity(dt)
        return

    def on_keypress(self, symbol, modifiers):
        return

    def update_velocity(self, dt):
        is_on_ground = self.gameWindowReference.physics_engine.is_on_ground(self.spriteReference)

        if self.modelReference.isMovingRight:
            if is_on_ground:
                force = (self.modelReference.speed, 0)
            else:
                force = (C.PLAYER_MOVE_FORCE_IN_AIR, 0)
            self.gameWindowReference.physics_engine.apply_force(self.spriteReference, force)
            self.gameWindowReference.physics_engine.set_friction(self.spriteReference, 0)
        elif self.modelReference.isMovingLeft:
            if is_on_ground:
                force = (-self.modelReference.speed, 0)
            else:
                force = (-C.PLAYER_MOVE_FORCE_IN_AIR, 0)
            self.gameWindowReference.physics_engine.apply_force(self.spriteReference, force)
            self.gameWindowReference.physics_engine.set_friction(self.spriteReference, 0)


    modelReference: None
    gameWindowReference: None
    spriteReference: None