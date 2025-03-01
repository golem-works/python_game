import pygame
import random
import time


# pygameを初期化
pygame.init()

#スクリーンを初期化
screen = pygame.display.set_mode()
#スクリーンのサイズを設定
screen_width = screen.get_width()
screen_height = screen.get_height()

pygame.display.set_caption("キャッチゲーム")

# 背景を設定 
background_color = (220, 255, 220)

#イメージ
mole_image = pygame.image.load("model.png")
mole_width = mole_image.get_width()
mole_height = mole_image.get_height()

#キャラスピードの設定
mole_speed = screen_height / 800

#キャラの出現率
mole_spawn_rate = 30

#game time
play_secs = 30

#score
score = 0

#font
font = pygame.font.Font(None,48)

#スプライトグループ
moles = pygame.sprite.Group()

#クロックを設定
clock = pygame.time.Clock()
clock.tick(60)

#game用の値
running = True
start_time=time.time()


#game loop
while running:
    #イベントを取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #背景を描画
    screen.fill(background_color)

    #キャラを生成
    if random.randint(1, mole_spawn_rate) == 1:
        mole = pygame.sprite.Sprite()
        mole.image = mole_image
        mole.rect = mole.image.get_rect()
        mole.rect.x = random.randint(0, screen_width - mole_width)
        mole.rect.y = 0
        moles.add(mole)

    #キャラを描画
    for mole in moles:
        mole.rect.y += mole_speed
        screen.blit(mole.image, mole.rect)
        if mole.rect.y > screen_height:
            moles.remove(mole)
            score -= 1

    #スコアを描画
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    #残り時間を描画
    elapsed_time = time.time() - start_time
    remaining_time = max(play_secs - elapsed_time, 0)
    time_text = font.render(f"Time: {remaining_time:.1f}", True, (0, 0, 0))
    screen.blit(time_text, (10, 10 + score_text.get_height()))

    #ゲームオーバー
    if remaining_time == 0:
        running = False

    #マウスのクリックを取得
    if pygame.mouse.get_pressed()[0]:
        click_pos = pygame.mouse.get_pos()
        for mole in moles:
            if mole.rect.collidepoint(click_pos):
                moles.remove(mole)
                score += 1

    #画面を更新
    pygame.display.flip()
