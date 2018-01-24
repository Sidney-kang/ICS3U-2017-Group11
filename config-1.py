# Created by: Sidney Kang
# Created on: Jan 2018
# Created for: ICS3U
# This holds all global variables.

import sound

# These are the variables associated with music and sound effects
main_menu_music = sound.Player('assets/sounds/main_menu_music.mp3')
main_game_music = sound.Player('assets/sounds/main_game_music.mp3')
music_on = True
sound_effects_on = True

# These are the variables associated with the main game
gender_type  = './assets/sprites/boy_thief.PNG'
level_difficulty = 0
game_over = False
game_won = False
restart_game = False
home_menu_pressed = False
ran_once = False

# This variable is associated with the transition scene
no_button_pressed = False
