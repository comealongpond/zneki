SCREEN_TITLE = "Zneki"

CAMERA_SPEED = 1.0
BACKGROUND_SCALE = 2.0

# Gravity
GRAVITY = 3000

# Damping - Amount of speed lost per second
DEFAULT_DAMPING = 1.0
PLAYER_DAMPING = 0.001

# Friction between objects
PLAYER_FRICTION = 1.0
WALL_FRICTION = 1.0
DYNAMIC_ITEM_FRICTION = 0.6

# Mass (defaults to 1)
PLAYER_MASS = 2.0

# Keep player from going too fast
PLAYER_MAX_HORIZONTAL_SPEED = 5000
PLAYER_MAX_VERTICAL_SPEED = 50000

PLAYER_MOVE_FORCE = 10000
# Force applied when moving left/right in the air
PLAYER_MOVE_FORCE_IN_AIR = 8000

# Strength of a jump
PLAYER_JUMP_IMPULSE = 4000

# How big are our image tiles?
SPRITE_IMAGE_SIZE = 128

# Scale sprites up or down
SPRITE_SCALING_PLAYER = .3
SPRITE_SCALING_TILES = 1

# Scaled sprite size for tiles
#SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

# Close enough to not-moving to have the animation go to idle.
DEAD_ZONE = 1.0

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

# How many pixels to move before we change the texture in the walking animation
DISTANCE_TO_CHANGE_TEXTURE = 20