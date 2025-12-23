# Utility functions for a 2D game

def play_music(level):
    music.stop()
    music.play(f"level{level}")

def reset_game(game):
    game.__init__()

def update_score(game, points):
    game.score += points
    if game.score > game.high_score:
        game.high_score = game.score

def toggle_pause(game):
    game.paused = not game.paused
    if game.paused:
        music.pause()
    else:
        music.unpause()

def save_game_state(game, filename="savegame.dat"):
    with open(filename, "wb") as f:
        pickle.dump(game, f)

def load_game_state(filename="savegame.dat"):
    with open(filename, "rb") as f:
        return pickle.load(f)

def display_message(screen, message, position, font_size=36, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text = font.render(message, True, color)
    screen.blit(text, position)

def check_collision(sprite1, sprite2):
    return sprite1.rect.colliderect(sprite2.rect)

def get_random_position(screen_width, screen_height, sprite_width, sprite_height):
    x = random.randint(0, screen_width - sprite_width)
    y = random.randint(0, screen_height - sprite_height)
    return x, y

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def normalize_vector(vector):
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    if length == 0:
        return (0, 0)
    return (vector[0] / length, vector[1] / length)

def lerp(start, end, t):
    return start + t * (end - start)

def fade_in(screen, color=(0, 0, 0), speed=5):
    fade = pygame.Surface(screen.get_size())
    fade.fill(color)
    for alpha in range(0, 255, speed):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

def fade_out(screen, color=(0, 0, 0), speed=5):
    fade = pygame.Surface(screen.get_size())
    fade.fill(color)
    for alpha in range(255, 0, -speed):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

def get_current_time():
    return time.time()

def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02}:{secs:02}"

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

def clamp_vector(vector, max_length):
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    if length > max_length:
        scale = max_length / length
        return (vector[0] * scale, vector[1] * scale)
    return vector

def rotate_point(point, angle, origin=(0, 0)):
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return (qx, qy)

def blit_centered(screen, image, position):
    rect = image.get_rect(center=position)
    screen.blit(image, rect)

def load_image(path, colorkey=None):
    image = pygame.image.load(path)
    if colorkey is not None:
        image.set_colorkey(colorkey)
    return image

def draw_text_centered(screen, text, position, font_size=36, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    rendered_text = font.render(text, True, color)
    rect = rendered_text.get_rect(center=position)
    screen.blit(rendered_text, rect)

def get_fps(clock):
    return clock.get_fps()

def limit_fps(clock, fps):
    clock.tick(fps)

def is_key_pressed(key):
    keys = pygame.key.get_pressed()
    return keys[key]

def is_mouse_button_pressed(button):
    buttons = pygame.mouse.get_pressed()
    return buttons[button]

def get_mouse_position():
    return pygame.mouse.get_pos()

def set_mouse_position(position):
    pygame.mouse.set_pos(position)

def hide_mouse_cursor():
    pygame.mouse.set_visible(False)

def show_mouse_cursor():   
    pygame.mouse.set_visible(True)

def capture_screenshot(screen, filename="screenshot.png"):
    pygame.image.save(screen, filename)

def get_screen_size(screen):
    return screen.get_size()

def toggle_fullscreen(screen):
    pygame.display.toggle_fullscreen()

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 

def blend_colors(color1, color2, t):
    r = int(color1[0] + (color2[0] - color1[0]) * t)
    g = int(color1[1] + (color2[1] - color1[1]) * t)
    b = int(color1[2] + (color2[2] - color1[2]) * t)
    return (r, g, b)

def get_angle_between_points(point1, point2):
    return math.atan2(point2[1] - point1[1], point2[0] - point1[0])

def rotate_surface(surface, angle):
    return pygame.transform.rotate(surface, angle)

def scale_surface(surface, scale):
    size = surface.get_size()
    new_size = (int(size[0] * scale), int(size[1] * scale))
    return pygame.transform.scale(surface, new_size)

def flip_surface(surface, flip_x, flip_y):
    return pygame.transform.flip(surface, flip_x, flip_y)

def create_text_surface(text, font_size=36, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    return font.render(text, True, color)

def draw_rect(screen, color, rect, width=0):
    pygame.draw.rect(screen, color, rect, width)

def draw_circle(screen, color, position, radius, width=0):
    pygame.draw.circle(screen, color, position, radius, width)

def draw_line(screen, color, start_pos, end_pos, width=1):
    pygame.draw.line(screen, color, start_pos, end_pos, width)

def draw_polygon(screen, color, points, width=0):
    pygame.draw.polygon(screen, color, points, width)

def get_text_size(text, font_size=36):
    font = pygame.font.Font(None, font_size)
    return font.size(text)

def wrap_text(text, font_size, max_width):  
    font = pygame.font.Font(None, font_size)
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        test_line = current_line + word + ' '
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '
    lines.append(current_line)
    return lines