import es
import random
import os

first_blood = False

#======================================================================================
#	Random Firstblood Sounds
#======================================================================================
#	Start of Config
#======================================================================================

# Firstblood Sounds
#=================================================
# Make sure slashs are pointing / that way...
folder = 'sound/rock/quake'
# Syntax of list ( ['admin/join.mp3','admin/join1.mp3']
connect_sounds = ['rock/quake/firstblood1.mp3','rock/quake/firstblood2.mp3','rock/quake/firstblood3.mp3','rock/quake/firstblood4.mp3','rock/quake/firstblood5.mp3']

# Download
#=================================================
# Makes script download disable if you want to use mani
enable_download = 1

#======================================================================================
#	End of Config
#======================================================================================
#	Do not touch anything down here!
#======================================================================================

# Addon Information
info = es.AddonInfo()
info.name = "Random Firstblood Sounds"
info.version = "1.0"
info.author = "HeaDHunteR"
info.description = "This scriptaddon adds random sounds at the first kill of each round (firstbloood) just edit the sounds above for your preference"
info.basename = "randomfirsblood_sounds"

headhunter_randomfirstbloodsounds_ver     = info.version

sound_folder =  str(es.ServerVar('eventscripts_gamedir')).replace('\\', '/') + '/' + folder

def load():
    if str(es.ServerVar("eventscripts_currentmap")) != "": 
        downloads()

    public = es.ServerVar('headhunter_randomfirstbloodsounds', info.version, info.name)
    public.makepublic()

def es_map_start(ev): 
    downloads()

def downloads():
    if os.path.exists(sound_folder):
        for dlfile in os.listdir(sound_folder):
            es.stringtable('downloadables', sound_folder + dlfile)
    else:
        es.dbgmsg(0, "Error: %s doesn't exist" % sound_folder)

def round_start(event_var):
   global first_blood
   first_blood = False

def player_death(event_var):
   sound = random.choice(connect_sounds)
   global first_blood
   if first_blood:
      return
   es.emitsound('player', event_var['userid'], sound, 1.0, 0.0)
   first_blood = True
 