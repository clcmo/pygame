def draw_enemies(screen, enemies):
    for enemy in enemies:
        if enemy.alive:
            screen.blit(f"enemy{enemy.sprite_index}", (enemy.rect.x, enemy.rect.y))
