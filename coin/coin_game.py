WIDTH= 400
HEIGHT= 400

score= 20

game_over = False
Skull= Actor("skull")
Skull.pos = 100, 100

Coin = Actor("coin")
coin.pos= 200 , 200

def draw():
screen.fill("green")
fox.draw()
coin.draw()
screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

def place_coin():
pass
def time_up():
pass
def update():
pass

coin.x = randint(20, (WIDTH - 20))
coin.y = randint(20, (HEIGHT - 20))
def update():
pass



