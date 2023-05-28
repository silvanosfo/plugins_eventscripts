import es
import random
import os

#======================================================================================
#	Random Knife Sounds
#======================================================================================
#	Start of Config
#======================================================================================

# Knife Sounds
#=================================================
# Make sure slashs are pointing / that way...
folder = 'sound/rock/quake'
# Syntax of list ( ['admin/join.mp3','admin/join1.mp3']
connect_sounds = ['rock/quake/facada1.mp3','rock/quake/facada2.mp3','rock/quake/facada3.mp3','rock/quake/facada4.mp3','rock/quake/facada5.mp3']

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
info.name = "Random Knife Sounds"
info.version = "1.0"
info.author = "HeaDHunteR"
info.description = "This scriptaddon adds random sounds when somebody is killed with a knife, just edit the sounds above for your preference"
info.basename = "randomknife_sounds"

headhunter_randomknifesounds_ver     = info.version


sound_folder =  str(es.ServerVar('eventscripts_gamedir')).replace('\\', '/') + '/' + folder


def load():
    if str(es.ServerVar("eventscripts_currentmap")) != "": 
        downloads()

    public = es.ServerVar('headhunter_randomknifesounds', info.version, info.name)
    public.makepublic()

def es_map_start(ev):
    downloads()

def downloads():
    if os.path.exists(sound_folder):
        for dlfile in os.listdir(sound_folder):
            es.stringtable('downloadables', sound_folder + dlfile)
    else:
        es.dbgmsg(0, "Error: %s doesn't exist" % sound_folder)
		
def player_death(ev):
	sound = random.choice(connect_sounds)
	if ev['weapon'] == 'knife':
            es.emitsound('player', ev['userid'], sound, 1.0, 0.0)