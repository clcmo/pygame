class SpriteAnimation:
    """Handles sprite animation cycles for entities."""
    
    def __init__(self, frames, duration_per_frame=0.1):
        """
        Initialize animation.
        
        Args:
            frames: List of frame colors or indices
            duration_per_frame: Time each frame is displayed (in seconds)
        """
        self.frames = frames
        self.duration_per_frame = duration_per_frame
        self.current_frame = 0
        self.elapsed_time = 0
    
    def update(self, dt):
        """Update animation frame based on elapsed time."""
        self.elapsed_time += dt
        if self.elapsed_time >= self.duration_per_frame:
            self.elapsed_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
    
    def get_current_frame(self):
        """Get the current frame."""
        return self.frames[self.current_frame]
    
    def reset(self):
        """Reset animation to first frame."""
        self.current_frame = 0
        self.elapsed_time = 0


def animate_sprite(entity, frames, dt):
    """Helper function to animate an entity's sprite."""
    if not hasattr(entity, 'animation'):
        entity.animation = SpriteAnimation(frames)
    
    entity.animation.update(dt)
    return entity.animation.get_current_frame()
