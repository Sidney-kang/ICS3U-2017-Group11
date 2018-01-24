# Created by:Shuvaethy Neill
# Created on: Jan 2018
# Created for: ICS3U
# This scene shows the winning scene.

from scene import *
import sound
import ui

import config
from transition_scene import *

class WinScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene

        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2 

        # add background color
        self.black = SpriteNode(position = self.size / 2, 
                                color = ('black'), 
                                parent = self, 
                                size = self.size)
                                
        background_position = Vector2()
        background_position.y = self.center_of_screen_y + 100
        background_position.x = self.center_of_screen_x                                  
        # add lose scene background 
        if config.gender_type == './assets/sprites/boy_thief.PNG':                                                                 
           self.background = SpriteNode('./assets/sprites/win_scene_background.PNG',
                                        parent = self, 
                                        position = background_position,
                                        size = self.size/1.1)  
        # lose scene for girl robber                                
        else:
           self.background = SpriteNode('./assets/sprites/win_scene_background_female.PNG',
                                        parent = self, 
                                        position = background_position,
                                        size = self.size/1.1)
        
        # This shows 'YOU WIN' label
        win_label_position = Vector2()   
        win_label_position.y = self.center_of_screen_y - 275
        win_label_position.x = self.center_of_screen_x                                           
        self.win = LabelNode(text = 'YOU WIN',
                             font = ('Marker Felt', 150),
                             parent = self,
                             color = '#ffffff',
                             position = win_label_position)    

        # This shows next button                                           
        next_arrow_button_position = Vector2()
        next_arrow_button_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 100
        next_arrow_button_position.x = self.size_of_screen_x - 80                    
        self.next_arrow_button = SpriteNode('./assets/sprites/next_arrow_button.PNG',
                                            parent = self, 
                                            position = next_arrow_button_position,
                                            scale = 0.25)                                                                                                                    

    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # This transitions to main game scene           
        if config.game_over == True or config.game_won == True:
           self.dismiss_modal_scene()          
           
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # This transitions to transition scene
        if self.next_arrow_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')    
           self.present_modal_scene(TransitionScene())                      

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
