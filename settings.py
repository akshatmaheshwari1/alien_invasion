class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #Ship Settings
        self.ship_speed = 5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 15.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 3.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 #1 represents right and -1 represents left