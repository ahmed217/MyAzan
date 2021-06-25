import vlc
import time
import os, random 

class AzanPlayer:
  def __init__(self):
    self.instance = vlc.Instance('--aout=alsa')
    self.p = self.instance.media_player_new()
    vlc.libvlc_audio_set_volume(self.p, 100)  # volume 0..100
 
  def play(self, dir = './mp3/other/'):

    file = self.getFile(dir)
    self.m = self.instance.media_new(os.path.abspath(dir + file))
    self.p.set_media(self.m)
    self.p.play()
    print('Now playing ', dir + file) 
    time.sleep(10 * 60)

  def getFile(self, dir):
    return random.choice(os.listdir(dir))
    
if __name__ == '__main__':
  a = AzanPlayer()
  a.play('./mp3/fajr/') 
