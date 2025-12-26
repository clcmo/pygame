from pygame import Rect


class Button:
    """UI Button for menu interactions."""
    
    def __init__(self, x, y, width, height, text, action=None):
        """
        Initialize button.
        
        Args:
            x, y: Position
            width, height: Dimensions
            text: Button text
            action: Callback function when clicked
        """
        self.rect = Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.hovered = False
    
    def check_hover(self, pos):
        """Check if mouse is hovering over button."""
        self.hovered = self.rect.collidepoint(pos)
        return self.hovered
    
    def is_clicked(self, pos):
        """Check if button was clicked."""
        return self.rect.collidepoint(pos)
    
    def on_click(self):
        """Trigger button action."""
        if self.action:
            self.action()
    
    def draw(self, screen):
        """Draw button on screen."""
        color = "yellow" if self.hovered else "white"
        bg_color = (50, 50, 50) if self.hovered else (20, 20, 20)
        
        screen.draw.filled_rect(self.rect, bg_color)
        screen.draw.rect(self.rect, color)
        screen.draw.text(
            self.text,
            center=self.rect.center,
            fontsize=30,
            color=color
        )
