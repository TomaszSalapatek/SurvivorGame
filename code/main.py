from settings import *
from player import Player
import pygame
from sprites import *
from random import randint,choice
from pytmx.util_pygame import load_pygame
from groups import AllSprites

class Game:
    def __init__(self):

        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivors")
        self.clock = pygame.time.Clock()
        self.running = True
        

        #groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        #music
        self.bullet_sound = pygame.mixer.Sound(join('audio','shoot.wav'))
        self.game_sound = pygame.mixer.Sound(join('audio','music.wav'))
        self.impact_sound = pygame.mixer.Sound(join('audio','impact.ogg'))
        self.impact_sound.set_volume(0.2)
        self.game_sound.set_volume(0.2)
        self.bullet_sound.set_volume(0.3)
        self.game_sound.play(loops = -1)
        

        #Events
        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event,500)
        self.spawn_position = []

        #gun timer
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_cooldown = 100

        
        self.load_images()
        self.setup()

    def load_images(self):
        self.bullet_surf = pygame.image.load(join('images','gun','bullet.png')).convert_alpha()

        folders = list(walk(join('images','enemies')))[0][1]
        self.enemy_frames = {}
        for folder in folders:
            for folder_path,_, file_names in walk(join('images','enemies',folder)):
                self.enemy_frames[folder] = []
                for file_name in sorted(file_names,key = lambda name: int(name.split('.')[0])):
                    full_path = join(folder_path,file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    self.enemy_frames[folder].append(surf)
        
    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.bullet_sound.play()
            pos = self.gun.rect.center + self.gun.player_direction * 50
            Bullet(self.bullet_surf,pos,self.gun.player_direction,(self.all_sprites,self.bullet_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def gun_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.gun_cooldown:
                self.can_shoot  = True
    def setup(self):
        map = load_pygame(join('data','maps','world.tmx'))

        for x,y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x*TILE_SIZE,y*TILE_SIZE),image,self.all_sprites) #tam liczy sie po kratkach, musimyprzemnozyc razy piksele
    
        for obj in map.get_layer_by_name('Objects'):
             CollisionSprite((obj.x,obj.y),obj.image,(self.all_sprites,self.collision_sprites))
        
        for obj in map.get_layer_by_name('Collisions'):
             CollisionSprite((obj.x,obj.y),pygame.Surface((obj.width,obj.height)),self.collision_sprites)

        
        for obj in map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player((obj.x,obj.y),self.all_sprites,self.collision_sprites)
                self.gun = Gun(self.player,self.all_sprites)
            else:
                self.spawn_position.append((obj.x,obj.y))

    def bullet_collision(self):
        if self.bullet_sprites:
            for bullet in self.bullet_sprites:
                collided_sprites = pygame.sprite.spritecollide(bullet,self.enemy_sprites,False,pygame.sprite.collide_mask)
                if collided_sprites:
                    bullet.kill()
                    for sprite in collided_sprites:
                        sprite.destroy()
                self.impact_sound.play()
                    
    def player_collision(self):
        if pygame.sprite.spritecollide(self.player,self.enemy_sprites,False,pygame.sprite.collide_mask):
            self.running = False
        
    def run(self):
        while self.running:

            dt = self.clock.tick()/1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    exit()
                if event.type == self.enemy_event:
                    Enemy(choice(self.spawn_position),choice(list(self.enemy_frames.values())),(self.all_sprites,self.enemy_sprites),self.player,self.collision_sprites)
        
            

            #update
            self.gun_timer()
            self.input()
            self.all_sprites.update(dt)
            self.bullet_collision()
            self.player_collision()
            

            #draw section
            self.display_surface.fill((0,0,0)) 
            self.all_sprites.draw(self.player.rect.center)
            #keys = pygame.key.get_pressed()
        
            
            pygame.display.update()
            


if __name__ == '__main__': #if file is ok
    game = Game()
    game.run()


    