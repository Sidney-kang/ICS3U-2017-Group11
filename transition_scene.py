# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import sound
import ui

import config

class TransitionScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2 
        self.scale_size = 0.4
        
        if config.sound_effects_on == True:
           sound.set_volume(50)
        elif config.sound_effects_on == False:
           sound.set_volume(0)
        
        if config.music_on == True:
           config.main_menu_music.play()
        elif config.music_on == False:
           config.main_menu_music.pause()
           
        if config.level_difficulty < 5:
           self.text = 'Would you like to go to the next level?' 
        else:
            self.text = 'You completed all the levels! Return to the levels scene?'
            self.no_button.remove_from_parent()
        
        # add blue sky background 
        self.background = SpriteNode('./assets/sprites/main_menu_background.PNG',
        	                           position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
                                     
        bush_position = Vector2()
        bush_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 100
        bush_position.x = self.size_of_screen_x - 100                           
        self.bush = SpriteNode('./assets/sprites/bush.PNG',
                               parent = self, 
                               position = bush_position,
                               scale = 0.45)       
                                       
        bush_2_position = Vector2()
        bush_2_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 100
        bush_2_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 100                               
        self.bush_2 = SpriteNode('./assets/sprites/bush.PNG',
                                 parent = self, 
                                 position = bush_2_position,
                                 scale = 0.45)
                                 
        go_to_next_level_label_position = Vector2()   
        go_to_next_level_label_position.y = self.center_of_screen_y + 100
        go_to_next_level_label_position.x = self.center_of_screen_x                                                 
        self.go_to_next_level_label = LabelNode(text = self.text,
                                     font = ('Marker Felt', 45),
                                     color = 'black',
                                     parent = self,
                                     position = go_to_next_level_label_position)  
                                     
        # This shows music button                                                                  
        yes_button_position = Vector2()
        yes_button_position.y = self.size_of_screen_y - 500
        yes_button_position.x = self.center_of_screen_x - 250                
        self.yes_button = SpriteNode('./assets/sprites/yes_button.PNG',
                                       parent = self, 
                                       position = yes_button_position,
                                       scale = 0.3)         
        
        # This shows no music button                                                                 
        no_button_position = Vector2()
        no_button_position.y = self.size_of_screen_y - 500
        no_button_position.x = self.center_of_screen_x + 250                
        self.no_button = SpriteNode('./assets/sprites/no_button.PNG',
                                          parent = self, 
                                          position = no_button_position,
                                          scale = 0.3)                                  
                                     
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen       
        
        if self.yes_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')
           config.level_difficulty = config.level_difficulty + 1       
           if config.level_difficulty <= 5:    
              if config.ran_once == False:
                 config.ran_once = True  
              config.game_won = True      
              config.restart_game = True
              config.main_menu_music.stop()
              self.dismiss_modal_scene()              
           else:
              config.game_won = True
              self.dismiss_modal_scene()
                 
        if self.no_button.frame.contains_point(touch.location):   
           config.game_won = True
           config.no_button_pressed = True
           config.main_game_music.stop()
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
