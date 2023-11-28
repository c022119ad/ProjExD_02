import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900

delta = {
pg.K_UP:(0,-5),
pg.K_DOWN:(0,+5),
pg.K_LEFT:(-5,0),
pg.K_RIGHT:(5,0)
}  # 練習3 移動キーの作成


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()  # 練習3 こうかとんSurfaceのrectを抽出
    bm_img = pg.Surface((20,20))  # 練習1透明のSurfaceを生成
    pg.draw.circle(bm_img,(255,0,0),(10,10),10)  # 練習1赤い半径の円をdraw
    bm_img.set_colorkey((0,0,0))
    bm_rct = bm_img.get_rect()
    kk_rct.center = 900,400
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
        key_lst = pg.key.get_pressed()
        summove =[0,0]
        for k,tpl in delta.items():
            if key_lst[k]:  # 矢印キーが押されたら合計移動量を入れる
                summove[0] += tpl[0]
                summove[1] += tpl[1]
        
        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(summove[0],summove[1])
        screen.blit(kk_img, kk_rct)
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