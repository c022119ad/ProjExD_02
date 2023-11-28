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


def check_bound(rct:pg.Rect) -> tuple[bool,bool]:
    """
    オブジェクトが画面内か画面外を判定して真理値タプルを返す関数
    引数rctは こうかとんor爆弾Surfaceのrect
    戻り値 横方向,縦方向判定結果 画面内ならTrue 画面外ならFalse
    """
    yoko,tate = True,True
    if rct.left <0 or WIDTH <rct.right:
        yoko = False
    if rct.top <0 or HEIGHT < rct.bottom:
        tate = False
    return yoko,tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_imgs = [pg.transform.rotozoom(kk_img,i*45,1.0) for i in range(8)]  #切り替え用に画像をリストを作る
    c = 1
    kk_imgs[2]  = pg.transform.flip(kk_imgs[2],True,False) #左右反転する
    for l in range(3,7):
        
        kk_imgs[l] = pg.transform.rotozoom(kk_imgs[2],c*45,1.0)  #角度調整
        c+=1
    kk_ch_dict = {
    (-5,0): kk_imgs[0],
    (-5,+5): kk_imgs[1],
    (0,5):kk_imgs[2],
    (5,5):kk_imgs[3],
    (5,0):kk_imgs[4],
    (5,-5):kk_imgs[5],
    (0,-5):kk_imgs[6],
    (-5,-5):kk_imgs[7]
    }
    kk_rct = kk_img.get_rect()  # 練習3 こうかとんSurfaceのrectを抽出
    bm_img = pg.Surface((20,20))  # 練習1透明のSurfaceを生成
    pg.draw.circle(bm_img,(255,0,0),(10,10),10)  # 練習1赤い半径の円をdraw
    bm_img.set_colorkey((0,0,0))
    bm_rct = bm_img.get_rect()
    kk_rct.center = 900,400
    bm_rct.centerx = random.randint(0,WIDTH)
    bm_rct.centery = random.randint(0,HEIGHT)
    vx = 0
    vy = 0
    clock = pg.time.Clock()
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bm_rct):
            print("game over")
            return
        
        key_lst = pg.key.get_pressed()
        summove =[0,0]
        for k,tpl in delta.items():
            if key_lst[k]:  # 矢印キーが押されたら合計移動量を入れる
                summove[0] += tpl[0]
                summove[1] += tpl[1]
        
        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(summove[0],summove[1])
        if check_bound(kk_rct) != (True,True):
            kk_rct.move_ip(-summove[0],-summove[1])
        kk_key = tuple(summove)
        if sum(summove) != 0:
            kk_img =kk_ch_dict[kk_key] 
        screen.blit(kk_img, kk_rct)
        #c = 0
        #for k,v in kk_ch_dict.items():
         #   screen.blit(v,(c*100,450))
          #  c+=1
        
        bm_rct.move_ip(vx,vy)  # 練習2 爆弾を動かす
        yoko,tate = check_bound(bm_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        bm_rct.move_ip(vx,vy)
                
        screen.blit(bm_img,bm_rct)
        
        pg.display.update()
        tmr += 1
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()