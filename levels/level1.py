from models.enemy import Enemy

def create_level1():
    return [
        Enemy(200, 200, "zone1"),
        Enemy(400, 300, "zone2")
    ]
