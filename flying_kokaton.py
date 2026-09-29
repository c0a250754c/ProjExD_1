import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習８
    kk_img = pg.image.load("fig/3.png") #練習３
    kk_img = pg.transform.flip(kk_img, True, False) #練習5
    kk_rct = kk_img.get_rect ()
    kk_rct.center = 300,200
    tmr = 0
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_list = pg.key.get_pressed()
        sum_mv = [-1,0]
        if key_list[pg.K_UP]:
            sum_mv[1] -= 1 
        if key_list[pg.K_DOWN]:
            sum_mv[1] += 1
        if key_list[pg.K_LEFT]:
            sum_mv[0] -= 1  
        if key_list[pg.K_RIGHT]:
            sum_mv[0] += 2   
        kk_rct.move_ip((sum_mv))

            
             
        x = tmr%3200 #練習５
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0]) #練習７
        screen.blit(bg_img2, [-x+3200, 0]) #練習９
        screen.blit(kk_img, kk_rct)#練習4,10
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()