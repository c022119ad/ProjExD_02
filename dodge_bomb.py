import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bm_img = pg.Surface((20,20))  # 練習1透明のSurfaceを生成
    pg.draw.circle(bm_img,(255,0,0),(10,10),10)  # 練習1赤い半径の円をdraw
    bm_img.set_colorkey((0,0,0))
    bm_rct = bm_img.get_rect()
    bm_rct.centerx = random.randint(0,WIDTH)
    bm_rct.centery = random.randint(0,HEIGHT)
    vx = 5
    vy = 5
    clock = pg.time.Clock()
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bm_rct.move_ip(vx,vy)  # 練習2 爆弾を動かす
        screen.blit(bm_img,bm_rct)
        
        pg.display.update()
        tmr += 1
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()