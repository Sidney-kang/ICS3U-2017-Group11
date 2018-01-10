# Created by: Shuvaethy Neill
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the credits scene

from scene import *
import sound
import ui

from settings_scene import *

class CreditsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2 
        self.scale_size = 0.4
        
        if SettingsScene.SoundEffectsOn == True:
           sound.set_volume(50)
        elif SettingsScene.SoundEffectsOn == False:
           sound.set_volume(0)
        
        if SettingsScene.MusicOn == True:
           SettingsScene.MainMenuMusic.play()
        elif SettingsScene.MusicOn == False:
           SettingsScene.MainMenuMusic.pause()
        
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
                                                       
        credits_title_position = Vector2()
        credits_title_position.y = self.center_of_screen_y + 270
        credits_title_position.x = self.center_of_screen_x                      
        self.credits_title = SpriteNode('./assets/sprites/credits_title.PNG',
                                        parent = self, 
                                        position = credits_title_position,
                                        scale = 0.45)   
                                       
        home_button_position = Vector2()
        home_button_position.y = self.size_of_screen_y - 70
        home_button_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 100                   
        self.home_button = SpriteNode('./assets/sprites/home_button.PNG',
                                      parent = self, 
                                      position = home_button_position,
                                      scale = 0.25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    
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
        
        if self.home_button.frame.contains_point(touch.location):
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
