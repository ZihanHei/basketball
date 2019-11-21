#game file
from gamelib import*

#variable#
game2=Game(800,600,"Basketball")

bk=Image("bk.jpg",game2)
bk.resizeTo(800,600)

kobe=Image("kobe.png",game2)
kobe.resizeBy(-50)
kobe.setSpeed(10,60)

michael=Image("michael.png",game2)
michael.resizeBy(-50)
michael.setSpeed(8,60)


ball=Image("basketball.png",game2)
ball.resizeBy(-95)

#essential game loop
while not game2.over:
    game2.processInput()

    bk.draw()
    kobe.move(True)
    michael.move(True)
    ball.moveTo(mouse.x,mouse.y)
    game2.update(30)

game2.quit()
