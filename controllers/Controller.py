

class Controller:
    
    def on_update(self, dt):
        self.update_position(dt)
        self.update_velocity(dt)
        return

    def on_keypress(self, symbol, modifiers):
        return
    
    def update_position(self, dt):
        if self.modelReference.velocity["x"] != 0:
            self.modelReference.position["x"] += self.modelReference.velocity["x"] * dt
        if self.modelReference.velocity["y"] != 0:
            self.modelReference.position["y"] = max(300, self.modelReference.position["y"] + self.modelReference.velocity["y"] * dt)
            if self.modelReference.position["y"] == 300:
                self.modelReference.velocity["y"] = 0

    def update_velocity(self, dt):
        change_x = 0
        change_y = 0
        drainingLeft = False
        drainingRight = False

        if self.modelReference.isMovingRight:
            change_x += self.modelReference.acceleration * dt
        elif self.modelReference.isMovingLeft:
            change_x -= self.modelReference.acceleration * dt
        else: # Drain velocity
            if self.modelReference.velocity["x"] > 0:
                change_x = min(0, self.modelReference.deceleration * dt)
                drainingLeft = True
            elif self.modelReference.velocity["x"] < 0:
                change_x = max(0, -1 * self.modelReference.deceleration * dt)
                drainingRight = True
                
        if self.modelReference.isMovingUp:
            change_y += self.modelReference.acceleration * dt
        elif self.modelReference.isMovingDown:
            change_y -= self.modelReference.acceleration * dt
        else: # grävity
            if self.modelReference.isAffectedGravity:
                change_y = min(0, change_y + self.modelReference.deceleration * dt)

        vx = self.modelReference.velocity["x"] + change_x
        if (drainingLeft and vx < 0) or (drainingRight and vx > 0):
            vx = 0
        self.modelReference.velocity["x"] = min(self.modelReference.speed, vx)
        self.modelReference.velocity["y"] = min(self.modelReference.speed, self.modelReference.velocity["y"] + change_y)

    modelReference: None