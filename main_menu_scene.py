# Created by: Shuvaethy Neill
# Created on: Jan 2018
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import sound
import ui

import config
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

        # add bush on right (for background)                                                        
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

        # This shows game logo                                                          
        game_logo_position = Vector2()
        game_logo_position.y = self.center_of_screen_y + 50
        game_logo_position.x = self.center_of_screen_x + 100                          
        self.game_logo = SpriteNode('./assets/sprites/game_logo.PNG',
                                    parent = self, 
                                    position = game_logo_position,
                                    scale = 0.45)                                

        # This shows start button                                                          
        start_button_position = Vector2()
        start_button_position.y = self.center_of_screen_y - 130
        start_button_position.x = self.center_of_screen_x - 60
        self.start_button = SpriteNode('./assets/sprites/start_button.PNG',
                                       parent = self,
                                       position = start_button_position,
                                       scale = 0.23)        

        # This shows settings button                                                                
        settings_button_position = Vector2()
        settings_button_position.y = self.center_of_screen_y - 200
        settings_button_position.x = self.center_of_screen_x - 60
        self.settings_button = SpriteNode('./assets/sprites/settings_button.PNG',
                                          parent = self,
                                          position = settings_button_position,
                                          scale = 0.23)      

        # This shows credits button                                                                  
        credits_button_position = Vector2()
        credits_button_position.y = self.center_of_screen_y - 270
        credits_button_position.x = self.center_of_screen_x - 60
        self.credits_button = SpriteNode('./assets/sprites/credits_button.PNG',
                                         parent = self,
                                         position = credits_button_position,
                                         scale = 0.23)
                                                                                                                                                                   
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

        # This transitions to settings scene
        if self.settings_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')
           self.present_modal_scene(SettingsScene())
        # This transitions to credits scene   
        if self.credits_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')
           self.present_modal_scene(CreditsScene())
        # This transitions to levels scene  
        if self.start_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-tap-mellow')
           config.game_over = False
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
