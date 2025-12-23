from models.enemy import Enemy

def create_level2():
    return [
        Enemy(150, 150, "zone1"),
        Enemy(350, 250, "zone2"),
        Enemy(500, 400, "zone3")
    ]
