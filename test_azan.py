import vlc
import time

instance = vlc.Instance('--aout=alsa')
p = instance.media_player_new()
m = instance.media_new('/home/pi/MyAzan/azan1.mp3') 
p.set_media(m)
p.play() 
#p.pause() 
#vlc.libvlc_audio_set_volume(p, 80)  # volume 0..100
time.sleep(100)
