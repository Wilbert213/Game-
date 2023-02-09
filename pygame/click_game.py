blob=Actor('blob_normal')
blob. pos= 100, 50

WIDTH= 500
HEIGHT= blob.height + 20


def draw():
     screen.fill(( 255, 0, 0))
     blob.draw()



def update():
    blob.left =blob.left + 2
    if blob.left> WIDTH:
        blob.right = 0




def on_mouse_down(pos):
    if blob.collidepoint(pos):
        print("wow!")
        sounds.bloop.play
    else:
        print("missed me!")


