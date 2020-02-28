import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()   #初始化背景设置
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))     #创建1200*800的显示窗口
    pygame.display.set_caption("Alien Invasion")    #标题

    #创建一艘飞船
    ship=Ship(screen)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():    #访问pygame检测到的事件
            if event.type==pygame.QUIT:
                sys.exit()      #退出游戏
        
        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        #让最近绘制的屏幕可见
        pygame.display.flip()

#初始化游戏并开始主循环    
run_game()