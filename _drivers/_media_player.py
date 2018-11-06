import python-vlc

class _media_player():
    
    def __init__(self,command='WBUR'):
        '''
        Handle general media requests to be output from the
        If nothing is heard, WBUR will be put on
        '''

        #find the type of player needed. This is not the right way to do this but it works for now
        if 'WBUR' in command:
            #self._interface=__url_streamer('https://icecast-stream.wbur.org/wbur')
            #no special class is needed because the vlc.MediaPlayer works within structure
            self._interface=vlc.MediaPlayer("https://icecast-stream.wbur.org/wbur")


    def play(self):
        self._interface.play()