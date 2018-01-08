# Created by:Sidney Kang
# Created on: Jan 2018
# Created for: ICS3U
# This scene shows the losing scene.

from scene import *
import sound
import ui

from main_menu_scene import *
from settings_scene import *

class LoseScene(Scene):
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

        # show lose scene background 
        background_position = Vector2()
        background_position.y = self.center_of_screen_y + 100
        background_position.x = self.center_of_screen_x  
        # for boy robber
        if SettingsScene.GenderType == './assets/sprites/boy_thief.PNG':                                   
           self.background = SpriteNode('./assets/sprites/lose_scene_background.PNG',
                                        parent = self, 
                                        position = background_position,
                                        size = self.size/1.2) 
        # for girl robber                                
        else:
           self.background = SpriteNode('./assets/sprites/lose_scene_background_female.PNG',
                                        parent = self, 
                                        position = background_position,
                                        size = self.size/1.2)                             

        home_button_position = Vector2()
        home_button_position.y = self.size_of_screen_y - 70
        home_button_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 100                   
        self.home_button = SpriteNode('./assets/sprites/home_button.PNG',
                                      parent = self, 
                                      position = home_button_position,
                                      scale = 0.25)        

        # This shows 'YOU LOSE' label                             
        lose_label_position = Vector2()   
        lose_label_position.y = self.center_of_screen_y - 275
        lose_label_position.x = self.center_of_screen_x                                           
        self.lose = LabelNode(text = 'YOU LOSE',
                              font = ('Marker Felt', 150),
                              parent = self,
                              color = '#ffffff',
                              position = lose_label_position)                                                                                                                    

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
        pass
        
        # This transitions to main menu scene 
        if self.home_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')
           self.present_modal_scene(MainMenuScene())      
    
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
