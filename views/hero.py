def draw_hero(screen, hero):
    screen.blit(f"hero_{hero.direction}{hero.sprite_index}", (hero.rect.x, hero.rect.y))
