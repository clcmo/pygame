from models.enemy import Enemy

def create_level3():
    return [
        Enemy(100, 100, "zone1"),
        Enemy(300, 200, "zone2"),
        Enemy(500, 300, "zone3"),
        Enemy(600, 450, "zone4")
    ]
