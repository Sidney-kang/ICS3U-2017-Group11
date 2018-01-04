# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from levels_scene import *
from settings_scene import *
from credits_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2 
        self.scale_size = 0.4
        
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
                                     
        start_button_position = Vector2()
        start_button_position.y = self.center_of_screen_y - 100 
        start_button_position.x = self.center_of_screen_x 
        self.start_button = SpriteNode('./assets/sprites/start_button.PNG',
                                       parent = self,
                                       position = start_button_position,
                                       scale = 0.3)        
                                       
        settings_button_position = Vector2()
        settings_button_position.y = self.center_of_screen_y - 200
        settings_button_position.x = self.center_of_screen_x 
        self.settings_button = SpriteNode('./assets/sprites/settings_button.PNG',
                                          parent = self,
                                          position = settings_button_position,
                                          scale = 0.3)      
                                          
        credits_button_position = Vector2()
        credits_button_position.y = self.center_of_screen_y - 300
        credits_button_position.x = self.center_of_screen_x 
        self.credits_button = SpriteNode('./assets/sprites/credits_button.PNG',
                                          parent = self,
                                          position = credits_button_position,
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
        pass
        
        if self.settings_button.frame.contains_point(touch.location):
             self.present_modal_scene(SettingsScene())
        if self.credits_button.frame.contains_point(touch.location):
             self.present_modal_scene(CreditsScene())
        if self.start_button.frame.contains_point(touch.location):
             self.present_modal_scene(LevelsScene())
    
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
