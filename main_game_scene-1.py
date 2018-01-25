# Created by: Sidney Kang
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import sound
import ui

import config
from lose_scene import *
from win_scene import *
from numpy import random

class MainGameScene(Scene):        
    
    def setup(self):
        # this method is called, when user moves to this scene              
        
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2         
        
        self.down_button_down = False
        self.left_button_down = False
        self.up_button_down = False
        self.right_button_down = False 
        self.distance_between_hearts = 0       
        self.table_view_button_down = True
        self.robber_move_speed = 20.0
        self.police_attack_speed = 15.0
        self.police_attack_rate = 2
        self.number_coins_collected = 0
        self.stop_missiles = False
        self.heart_removed = False        
        self.missiles = []
        self.bushes = []
        self.coins = []
        self.hearts = []                
        self.character_gender = config.gender_type               
        
        # This allows sound effects to play or to not play 
        # based on whether the play sound effects or no sound effects was pressed (in settings scene)  
        if config.sound_effects_on == True:
           sound.set_volume(50)
        elif config.sound_effects_on == False:
           sound.set_volume(0)
        
        # This plays or does not play music 
        # based on whether the music or no music button was pressed (in settings scene)        
        if config.music_on == True:
           config.main_game_music.number_of_loops = -1
           config.main_game_music.play()
        elif config.music_on == False:
           config.main_game_music.pause()        
        
        # add grassy background 
        self.background = SpriteNode('./assets/sprites/main_game_background.PNG',
        	                           position = self.size / 2, 
                                     parent = self, 
                                     size = self.size) 
        
        # This show table view button                                                     
        table_view_button_position = Vector2()
        table_view_button_position.y = self.size_of_screen_y - 90
        table_view_button_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 80                   
        self.table_view_button = SpriteNode('./assets/sprites/table_view_button.PNG',
                                            parent = self, 
                                            position = table_view_button_position,
                                            scale = 0.25)    
        
        # This shows the bushes and coins                                                                                                                                                                                                                                                                         
        self.create_bush_and_coins()                    
                                                                                                                   
        # Creates robber sprite                                                           
        self.robber_position = Vector2()
        self.robber_position.y = self.center_of_screen_y - 250
        self.robber_position.x = self.size_of_screen_x - 170            
        self.robber = SpriteNode(self.character_gender,
                                 parent = self, 
                                 position = self.robber_position,
                                 scale = 0.11)                                
               
        # Creates down button                                                   
        down_button_position = Vector2()
        down_button_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 65
        down_button_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 135                   
        self.down_button = SpriteNode('./assets/sprites/down_button.PNG',
                                      parent = self, 
                                      position = down_button_position,
                                      alpha = 0.7,
                                      scale = 0.15)         
        # Creates left button                                  
        left_button_position = Vector2()
        left_button_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 150
        left_button_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 70                   
        self.left_button = SpriteNode('./assets/sprites/left_button.PNG',
                                      parent = self, 
                                      position = left_button_position,
                                      alpha = 0.7,
                                      scale = 0.15)         
        # Creates up button                                    
        up_button_position = Vector2()
        up_button_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 233
        up_button_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 135                   
        self.up_button = SpriteNode('./assets/sprites/up_button.PNG',
                                    parent = self, 
                                    position = up_button_position,
                                    alpha = 0.7,
                                    scale = 0.15) 
        # Creates right button                                  
        right_button_position = Vector2()
        right_button_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 150
        right_button_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 200                   
        self.right_button = SpriteNode('./assets/sprites/right_button.PNG',
                                       parent = self, 
                                       position = right_button_position,
                                       alpha = 0.7,
                                       scale = 0.15)                                                                                          
        
        # This creates the coin counter
        coin_count_position = Vector2()   
        coin_count_position.y = self.size_of_screen_y - 55
        coin_count_position.x = self.center_of_screen_x + 350                                              
        self.coin_count = LabelNode(text = 'Coins:' + '      ' + str(self.number_coins_collected) + '/' + str(config.level_difficulty),
                                    font = ('Marker Felt', 45),
                                    color = 'black',
                                    parent = self,
                                    position = coin_count_position)     
                                    
        
        # This creates a small coin sprite beside coin counter (for aesthetic)              
        coin_count_sprite_position = Vector2()
        coin_count_sprite_position.y = self.size_of_screen_y - 55
        coin_count_sprite_position.x = self.center_of_screen_x + 370                                                             
        self.coin_count_sprite = SpriteNode('plf:HudCoin',
                                            parent = self, 
                                            position = coin_count_sprite_position,
                                            scale = 1.3)                                                             
        
        # This shows 'Life: ' label                                                  
        life_span_position = Vector2()   
        life_span_position.y = self.size_of_screen_y - 55
        life_span_position.x = self.center_of_screen_x - 270                                                  
        self.life_span = LabelNode(text = 'Life: ',
                                   font = ('Marker Felt', 45),
                                   color = 'black',
                                   parent = self,
                                   position = life_span_position)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                       
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # This loads a new game scene for corresponding level
        if config.ran_once == True: 
           if config.restart_game == True and config.game_won == True:
              self.setup()             
              config.ran_once = False
        
        # This transitions to levels scene                         
        if config.game_over == True or config.game_won == True and config.level_difficulty > 5 or config.game_won == True and config.no_button_pressed == True:
           self.dismiss_modal_scene()   
            
        # Every update it randomly check if new missiles should be created
        missile_create_chance = random.randint(1,30)
        if missile_create_chance <= self.police_attack_rate and self.stop_missiles == False:
           self.create_new_missile()            
           sound.play_effect('arcade:Explosion_7')   
           self.heart_removed = False               
        
        # This allows missiles to be removed once they reach bottom of screen      
        for missile in self.missiles:
            if missile.position.y < self.size_of_screen_y - (2 * (self.center_of_screen_y)) + 40:
               missile.remove_from_parent()
               self.missiles.remove(missile)   
        
        # Moves robber if button pressed        
        if self.down_button_down == True :
           self.robber.run_action(Action.move_by(0.0, -1*self.robber_move_speed, 0.1))
        if self.left_button_down == True :
           self.robber.run_action(Action.move_by(-1*self.robber_move_speed, 0.0, 0.1))
        if self.up_button_down == True :
           self.robber.run_action(Action.move_by(0.0, self.robber_move_speed, 0.1))
        if self.right_button_down == True :
           self.robber.run_action(Action.move_by(self.robber_move_speed, 0.0, 0.1))    
               
        # This checks if robber was hit by missile, if so 1 heart is removed from lifespan.
        #  When robber has no more hearts main_game_scene transitions to lose_scene      
        if len(self.missiles) > 0 and len(self.hearts) > 1:
           for missile in self.missiles:
               for heart in self.hearts:
                   if missile.frame.intersects(self.robber.frame) and self.heart_removed == False: 
                      sound.play_effect('arcade:Hit_2')
                      heart.remove_from_parent()
                      self.hearts.remove(heart)                    
                      missile.remove_from_parent()
                      self.missiles.remove(missile)
                      self.heart_removed = True 
        elif len(self.missiles) > 0 and len(self.hearts) == 1:  
             for missile in self.missiles:
                 for heart in self.hearts:
                     if missile.frame.intersects(self.robber.frame) and self.heart_removed == False:  
                        sound.play_effect('arcade:Hit_2')
                        heart.remove_from_parent()
                        self.hearts.remove(heart)  
                        missile.remove_from_parent()
                        self.missiles.remove(missile) 
                        self.robber.remove_from_parent()      
                        config.main_game_music.stop()  
                        self.stop_missiles = True
                        self.present_modal_scene(LoseScene())     
        else:           
           pass         	            
        
        # This checks if missile hit a bush, if so it removes missile from screen    
        if len(self.missiles) > 0 and len(self.bushes) > 0:
           for missile in self.missiles:
               for bush in self.bushes:
                   if missile.frame.intersects(bush.frame):
                      missile.remove_from_parent()
                      self.missiles.remove(missile)
                   else:
                      pass                
        
        # This checks if robber collected a coin, if so 1 point is added to coin counter.
        #  When coin counter is full main_game_scene transitions to win_scene  
        if len(self.coins) > 1:
           for collected_coin in self.coins:
                if collected_coin.frame.intersects(self.robber.frame):
                   sound.play_effect('arcade:Coin_5')
                   collected_coin.remove_from_parent()               
                   self.coins.remove(collected_coin)  
                   self.number_coins_collected = self.number_coins_collected + 1
                   self.coin_count.text = 'Coins:' + '      ' + str(self.number_coins_collected) + '/' + str(config.level_difficulty)
        elif len(self.coins) == 1:
           for collected_coin in self.coins:
               if collected_coin.frame.intersects(self.robber.frame):
                  sound.play_effect('arcade:Coin_5')
                  collected_coin.remove_from_parent()               
                  self.coins.remove(collected_coin)
                  self.number_coins_collected = self.number_coins_collected + 1
                  self.coin_count.text = 'Coins:' + '      ' + str(self.number_coins_collected) + '/' + str(config.level_difficulty)
                  config.main_game_music.stop() 
                  config.game_won = False
                  self.stop_missiles = True
                  self.present_modal_scene(WinScene())   
        else:
           pass                    
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # Checks if up, down, left, or right button was pressed
        if self.left_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')            
           self.left_button_down = True
           # This changes the direction the robber is facing (left)
           self.character_turned_left()                                                                                                                  
        if self.right_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')            
           self.right_button_down = True 
           # This changes the direction the robber is facing (right)
           self.character_turned_right()                                                                                                                                 
        if self.down_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')
           self.down_button_down = True                            
        if self.up_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')
           self.up_button_down = True                  
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
              
        # If finger is removed then no matter what, robber should not move
        self.left_button_down = False
        self.right_button_down = False
        self.up_button_down = False
        self.down_button_down = False

        # This shows a list of buttons for user to change scenes from main game
        #  game is paused in background
        if self.table_view_button.frame.contains_point(touch.location) and self.table_view_button_down == True:
           sound.play_effect('8ve:8ve-tap-mellow')                                  
           self.multi_menu_scene()  
           self.stop_missiles = True          
           self.table_view_button_down = False
        
        # This gets rid of blurry background and all buttons so user can return to game         
        if self.table_view_button_down == False:
           # This returns back to game
           if self.back_arrow_button.frame.contains_point(touch.location):	             
              sound.play_effect('8ve:8ve-tap-mellow')    
              self.loading_background .remove_from_parent()
              self.back_arrow_button.remove_from_parent()
              self.home_button_game_scene.remove_from_parent()
              self.levels_button.remove_from_parent() 
              self.stop_missiles = False
              self.table_view_button_down = True
           # This transitions to main_menu_scene       
           elif self.home_button_game_scene.frame.contains_point(touch.location): 
              config.main_game_music.stop()   
              sound.play_effect('8ve:8ve-tap-mellow')       
              config.home_menu_pressed = True
              self.dismiss_modal_scene()
           # This transitions to levels_scene      
           elif self.levels_button.frame.contains_point(touch.location):	
              config.main_game_music.stop() 
              sound.play_effect('8ve:8ve-tap-mellow')    
              self.dismiss_modal_scene()   
   
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background            
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass            
                                       
    def create_new_missile(self):
        # This creates a missile sprite   
                   
        missile_start_position = Vector2()
        missile_start_position.x = random.randint(100,
                                        self.size_of_screen_x - 100)
        missile_start_position.y = self.size_of_screen_y + 100
        
        missile_end_position = Vector2()
        missile_end_position.x = missile_start_position.x
        missile_end_position.y = self.size_of_screen_y - (2 * (self.center_of_screen_y))                              
        
        self.missile = SpriteNode('./assets/sprites/missile.png',
                                  position = missile_start_position,
                                  parent = self) 
        
        self.missiles.append(self.missile)
                                        
        # Make missiles move downwards
        missileMoveAction = Action.move_to(missile_end_position.x, 
                                           missile_end_position.y,
                                           self.police_attack_speed,
                                           TIMING_SINODIAL)              
                                       
        self.missiles[len(self.missiles)-1].run_action(missileMoveAction)
        
    def create_bush(self): 
        # This creates a bush sprite 
        
        self.bush_position = Vector2()
        self.bush_position.y = random.randint((self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 200,
                                        self.size_of_screen_y - 200)
        self.bush_position.x = random.randint((self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 100,
                                        self.size_of_screen_x - 185)    
                                                            
        self.bush = SpriteNode('./assets/sprites/bush.PNG',
                               parent = self, 
                               position = self.bush_position,
                               scale = 0.2)  
                               
        self.bushes.append(self.bush)                   
    
    def create_coin(self): 
        # This creates a coin sprite
        
        self.coin_position = Vector2()
        self.coin_position.y = self.bush_position.y - 130
        self.coin_position.x = self.bush_position.x 
                                                            
        self.coin = SpriteNode('plf:HudCoin',
                               parent = self, 
                               position = self.coin_position,
                               scale = 1.3)  
        self.coins.append(self.coin)  
        
    def create_heart(self): 
        # This creates a heart sprite 
        
        self.heart_position = Vector2()
        self.heart_position.y = self.size_of_screen_y - 55
        self.heart_position.x = (self.center_of_screen_x - 200) + self.distance_between_hearts 
                                                            
        self.heart = SpriteNode('plf:HudHeart_full',
                                parent = self, 
                                position = self.heart_position,
                                scale = 1.2)  
        self.hearts.append(self.heart)                                                                                                                                    
        
    def multi_menu_scene(self):  
        # This creates a list of buttons 
        #  and background that make game scene look darker
    	  
    	  # This created 'blurry' black	background
        self.loading_background = SpriteNode(position = self.size / 2, 
                                             color = ('black'), 
                                             parent = self, 
                                             size = self.size)
        self.loading_background.alpha = 0.6
        
        # This creates back button so user can return to game
        back_arrow_button_position = Vector2()
        back_arrow_button_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 100
        back_arrow_button_position.x =  (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 80                    
        self.back_arrow_button = SpriteNode('./assets/sprites/back_arrow_button.PNG',
                                            parent = self, 
                                            position = back_arrow_button_position,
                                            scale = 0.6) 
                                          
        # This shows home button                           
        home_button_game_scene_position = Vector2()
        home_button_game_scene_position.y = self.center_of_screen_y + 100
        home_button_game_scene_position.x = self.center_of_screen_x                 
        self.home_button_game_scene = SpriteNode('./assets/sprites/home_button_game_scene.PNG',
                                                 parent = self, 
                                                 position = home_button_game_scene_position,
                                                 scale = 0.35)        
                                                                 
        # This shows levels button                               
        levels_button_position = Vector2()
        levels_button_position.y = self.center_of_screen_y - 50
        levels_button_position.x = self.center_of_screen_x                   
        self.levels_button = SpriteNode('./assets/sprites/levels_button.PNG',
                                        parent = self, 
                                        position = levels_button_position,
                                        scale = 0.35)        
                                        
    def character_turned_left(self):	
       # This shows the character facing left
    
        self.robber.remove_from_parent()    
    
        new_robber_position = self.robber.position        
        self.robber = SpriteNode(self.character_gender,
                                 parent = self, 
                                 position = new_robber_position,
                                 scale = 0.11)        
                                 
    def character_turned_right(self):
        # This shows the character facing right
    
        self.robber.remove_from_parent()       
    
        new_robber_position = self.robber.position
        if config.gender_type == './assets/sprites/boy_thief.PNG':    
           self.robber = SpriteNode('./assets/sprites/boy_thief_right.PNG',
                                    parent = self, 
                                    position = new_robber_position,
                                    scale = 0.11)              
        else:
           self.robber = SpriteNode('./assets/sprites/girl_thief_right.PNG',
                                    parent = self, 
                                    position = new_robber_position,
                                    scale = 0.11)               
                                    
    def create_bush_and_coins(self):	
        # This creates bushes and coins
        
        # This creates hearts for lifespan
        for counter in range(0,3):
            self.create_heart() 
            self.distance_between_hearts = self.distance_between_hearts + 60        
            
        # This creates bush and coin sprites in which each bush and coin pair is spaced out proportionately                                                                    
        for counter in range(0,config.level_difficulty):
            self.create_bush()  
            self.create_coin()  
        
        # This makes sure that each bush is not touching one another
        #  if so it recreates a bush with a different location     
        outer_loop_counter = 0
        inner_loop_counter = 0
        while outer_loop_counter < len(self.bushes):
              inner_loop_counter = outer_loop_counter + 1
              while inner_loop_counter < len(self.bushes):              
                     while    self.bushes[outer_loop_counter].frame.intersects(self.bushes[inner_loop_counter].frame) or self.coins[outer_loop_counter].frame.intersects(self.bushes[inner_loop_counter].frame):                         
                          self.bushes[outer_loop_counter].remove_from_parent()
                          self.coins[outer_loop_counter].remove_from_parent()
                          self.bushes.remove(self.bushes[outer_loop_counter])
                          self.coins.remove(self.coins[outer_loop_counter])
                          self.create_bush()
                          self.create_coin()                         
                     inner_loop_counter += 1
              outer_loop_counter += 1                                                                                                                                                                                                                                                                                                    
