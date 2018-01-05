# Created by: Sidney Kang
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the settings.

from scene import *
import ui

character_gender = './assets/sprites/boy_thief.PNG'

class SettingsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size_of_screen_x/2
        self.center_of_screen_y = self.size_of_screen_y/2 
        # self.scale_size = 0.45
        
        self.touched_once = False
        
        # add blue sky background 
        self.background = SpriteNode('./assets/sprites/main_menu_background.PNG',
        	                           position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
        
        # add bush for background                                                           
        bush_position = Vector2()
        bush_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 100
        bush_position.x = self.size_of_screen_x - 100                           
        self.bush = SpriteNode('./assets/sprites/bush.PNG',
                               parent = self, 
                               position = bush_position,
                               scale = 0.45)       
       
        # add bush for background                                
        bush_2_position = Vector2()
        bush_2_position.y = (self.size_of_screen_y - (2 * (self.center_of_screen_y))) + 100
        bush_2_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 100                               
        self.bush_2 = SpriteNode('./assets/sprites/bush.PNG',
                                 parent = self, 
                                 position = bush_2_position,
                                 scale = 0.45)     
        
        # Creates home button                                                              
        back_arrow_button_position = Vector2()
        back_arrow_button_position.y = self.size_of_screen_y - 90
        back_arrow_button_position.x = (self.size_of_screen_x - (2 * (self.center_of_screen_x))) + 80                   
        self.back_arrow_button = SpriteNode('./assets/sprites/back_arrow_button.PNG',
                                            parent = self, 
                                            position = back_arrow_button_position,
                                            scale = 0.25)            
                                       
        music_button_position = Vector2()
        music_button_position.y = self.size_of_screen_y - 300
        music_button_position.x = self.center_of_screen_x - 360                
        self.music_button = SpriteNode('./assets/sprites/volume_button.PNG',
                                       parent = self, 
                                       position = music_button_position,
                                       scale = 0.15)         
                                       
        no_music_button_position = Vector2()
        no_music_button_position.y = self.size_of_screen_y - 300
        no_music_button_position.x = self.center_of_screen_x - 150                
        self.no_music_button = SpriteNode('./assets/sprites/no_volume_button.PNG',
                                          parent = self, 
                                          position = no_music_button_position,
                                          scale = 0.15)    
                                       
        sound_effects_button_position = Vector2()
        sound_effects_button_position.y = self.center_of_screen_y - 150
        sound_effects_button_position.x = self.center_of_screen_x - 360                  
        self.sound_effects_button = SpriteNode('./assets/sprites/volume_button.PNG',
                                               parent = self, 
                                               position = sound_effects_button_position,
                                               scale = 0.15)                  
                                       
        no_sound_effects_button_position = Vector2()
        no_sound_effects_button_position.y = self.center_of_screen_y - 150
        no_sound_effects_button_position.x = self.center_of_screen_x - 150                  
        self.no_sound_effects_button = SpriteNode('./assets/sprites/no_volume_button.PNG',
                                                  parent = self, 
                                                  position = no_sound_effects_button_position,
                                                  scale = 0.15)                    
                                       
        boy_button_position = Vector2()
        boy_button_position.y = self.size_of_screen_y - 310
        boy_button_position.x = self.size_of_screen_x - 155             
        self.boy_button = SpriteNode('./assets/sprites/boy_button.PNG',
                                     parent = self, 
                                     position = boy_button_position,
                                     scale = 0.3)   
                                       
        girl_button_position = Vector2()
        girl_button_position.y = self.size_of_screen_y - 310
        girl_button_position.x = self.center_of_screen_x + 145              
        self.girl_button = SpriteNode('./assets/sprites/girl_button.PNG',
                                      parent = self, 
                                      position = girl_button_position,
                                      scale = 0.3)    
                                                                          
        settings_title_position = Vector2()
        settings_title_position.y = self.center_of_screen_y + 270
        settings_title_position.x = self.center_of_screen_x                      
        self.settings_title = SpriteNode('./assets/sprites/settings_title.PNG',
                                         parent = self, 
                                         position = settings_title_position,
                                         scale = 0.45)  
                                       
        music_label_position = Vector2()   
        music_label_position.y = self.size_of_screen_y - 200
        music_label_position.x = self.center_of_screen_x - 360                                                 
        self.music_label = LabelNode(text = 'Music',
                                     font = ('Helvetica', 45),
                                     color = 'black',
                                     parent = self,
                                     position = music_label_position)    
                                                               
        sound_effects_label_position = Vector2()   
        sound_effects_label_position.y = self.center_of_screen_y - 50
        sound_effects_label_position.x = self.center_of_screen_x - 285                                              
        self.sound_effects = LabelNode(text = 'Sound Effects',
                                       font = ('Helvetica', 45),
                                       color = 'black',
                                       parent = self,
                                       position = sound_effects_label_position)      
                                    
                                                                                      
        character_gender_label_position = Vector2()   
        character_gender_label_position.y = self.size_of_screen_y - 200
        character_gender_label_position.x = self.size_of_screen_x - 260                                                
        self.character_gender = LabelNode(text = 'Choose Character',
                                          font = ('Helvetica', 45),
                                          parent = self,
                                          color = 'black',
                                          position = character_gender_label_position)                                                                                                                                                   
        
        boy_label_position = Vector2()   
        boy_label_position.y = self.size_of_screen_y - 415
        boy_label_position.x = self.size_of_screen_x - 155                                            
        self.boy = LabelNode(text = 'Boy',
                             font = ('Helvetica', 35),
                             parent = self,
                             color = 'black',
                             position = boy_label_position) 
                                          
        girl_label_position = Vector2()   
        girl_label_position.y = self.size_of_screen_y - 415
        girl_label_position.x = self.center_of_screen_x + 145                                           
        self.girl = LabelNode(text = 'Girl',
                              font = ('Helvetica', 35),
                              parent = self,
                              color = 'black',
                              position = girl_label_position)                                  
                                                                                      
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
        
        if self.back_arrow_button.frame.contains_point(touch.location):
           self.dismiss_modal_scene()
           
        if self.girl_button.frame.contains_point(touch.location) and self.touched_once == True:  
           self.robber.remove_from_parent()  
           character_gender = './assets/sprites/girl_thief.PNG'
           robber_position = Vector2()
           robber_position.y = self.center_of_screen_y - 150
           robber_position.x = self.center_of_screen_x + 260              
           self.robber = SpriteNode(character_gender,
                                 parent = self, 
                                 position = robber_position,
                                 scale = 0.15) 
        elif self.girl_button.frame.contains_point(touch.location) and not self.touched_once == True:      
           character_gender = './assets/sprites/girl_thief.PNG'
           self.touched_once = True
           robber_position = Vector2()
           robber_position.y = self.center_of_screen_y - 150
           robber_position.x = self.center_of_screen_x + 260              
           self.robber = SpriteNode(character_gender,
                                 parent = self, 
                                 position = robber_position,
                                 scale = 0.15)  
        if self.boy_button.frame.contains_point(touch.location) and self.touched_once == True:  
           self.robber.remove_from_parent()  
           character_gender = './assets/sprites/boy_thief.PNG'
           robber_position = Vector2()
           robber_position.y = self.center_of_screen_y - 150
           robber_position.x = self.center_of_screen_x + 260              
           self.robber = SpriteNode(character_gender,
                                 parent = self, 
                                 position = robber_position,
                                 scale = 0.135)                          
        elif self.boy_button.frame.contains_point(touch.location) and not self.touched_once == True:           
           character_gender = './assets/sprites/boy_thief.PNG' 
           self.touched_once = True           
           robber_position = Vector2()
           robber_position.y = self.center_of_screen_y - 150
           robber_position.x = self.center_of_screen_x + 260                
           self.robber = SpriteNode(character_gender,
                                 parent = self, 
                                 position = robber_position,
                                 scale = 0.135)  
    
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
