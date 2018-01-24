# Created by: Sidney Kang
# Created on: Jan 2018
# Created for: ICS3U
# This scene shows the levels scene.

from scene import *
import ui

from main_game_scene import *
import config

class LevelsScene(Scene):
    
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2 

        # This allows sound effects to play or to not play 
        # based on whether the play sound effects or no sound effects was pressed (in settings scene)  
        if config.sound_effects_on == True:
           sound.set_volume(50)
        elif config.sound_effects_on == False:
           sound.set_volume(0)

        # This plays or does not play music 
        # based on whether the music or no music button was pressed (in settings scene)  
        if config.music_on == True:
           config.main_menu_music.play()
        elif config.music_on == False:
           config.main_menu_music.pause()
        
        # add blue sky background 
        self.background = SpriteNode('./assets/sprites/main_menu_background.PNG',
        	                           position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)

        # add bush on right (for backgound)                                                         
        bush_position = Vector2()
        bush_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 100
        bush_position.x = self.size_of_screen_x - 100                           
        self.bush = SpriteNode('./assets/sprites/bush.PNG',
                               parent = self, 
                               position = bush_position,
                               scale = 0.45)       
        
        # add bush on left (for background)                                                          
        bush_2_position = Vector2()
        bush_2_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 100
        bush_2_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 100                               
        self.bush_2 = SpriteNode('./assets/sprites/bush.PNG',
                                 parent = self, 
                                 position = bush_2_position,
                                 scale = 0.45)     

        # This shows home button
        home_button_position = Vector2()
        home_button_position.y = self.size_of_screen_y - 70
        home_button_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 100                   
        self.home_button = SpriteNode('./assets/sprites/home_button.PNG',
                                      parent = self, 
                                      position = home_button_position,
                                      scale = 0.25)                                                                                                                                                                               
        
        # This shows levels label
        levels_title_position = Vector2()
        levels_title_position.y = self.center_of_screen_y + 270
        levels_title_position.x = self.center_of_screen_x                      
        self.levels_title = SpriteNode('./assets/sprites/levels_title.PNG',
                                       parent = self, 
                                       position = levels_title_position,
                                       scale = 0.45)                              

        # This shows level 1 button 
        level_1_button_position = Vector2()
        level_1_button_position.y = self.center_of_screen_y 
        level_1_button_position.x = self.center_of_screen_x - 350                            
        self.level_1_button = SpriteNode('./assets/sprites/level_1_button.PNG',
                                  parent = self, 
                                  position = level_1_button_position,
                                  scale = 0.4)

        # This shows level 2 button 
        level_2_button_position = Vector2()
        level_2_button_position.y = self.center_of_screen_y 
        level_2_button_position.x = self.center_of_screen_x                             
        self.level_2_button = SpriteNode('./assets/sprites/level_2_button.PNG',
                                  parent = self, 
                                  position = level_2_button_position,
                                  scale = 0.4) 

        # This shows level 3 button 
        level_3_button_position = Vector2()
        level_3_button_position.y = self.center_of_screen_y 
        level_3_button_position.x = self.center_of_screen_x + 350                            
        self.level_3_button = SpriteNode('./assets/sprites/level_3_button.PNG',
                                  parent = self, 
                                  position = level_3_button_position,
                                  scale = 0.4)                               

    def update(self):
        # this method is called, hopefully, 60 times a second
         
         # This transitions to main menu scene
         if config.game_over == True:
            self.dismiss_modal_scene()  
         
         # This transitions to main menu scene                      
         if config.home_menu_pressed == True:
            config.home_menu_pressed = False
            self.dismiss_modal_scene()
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # This transitions to main menu scene
        if self.home_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')
           self.dismiss_modal_scene()
        
        # This transitions to level 1 of game
        if self.level_1_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')
           config.main_menu_music.stop()
           config.game_won = False
           config.level_difficulty = 3
           self.present_modal_scene(MainGameScene()) 
        # This transitions to level 2 of game   
        elif self.level_2_button.frame.contains_point(touch.location): 
           sound.play_effect('8ve:8ve-tap-mellow')
           config.main_menu_music.stop()
           config.game_won = False
           config.level_difficulty = 4
           self.present_modal_scene(MainGameScene())
        # This transitions to level 3 of game
        elif self.level_3_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')
           config.main_menu_music.stop()
           config.game_won = False
           config.level_difficulty = 5
           self.present_modal_scene(MainGameScene())
    
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
