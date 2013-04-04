#! /usr/bin/python
#
# COPYRIGHT: Gayner Technical Services Pty Ltd 2011
# 
# LICENCE: 
#	THIS FILE IS SUBJECT TO THE TERMS AND CONDITIONS DEFINED IN THE FILE
#	'LICENCE', WHICH IS PART OF THIS SOURCE CODE PACKAGE
#

import socket
import subprocess
import threading

AUDIO_HEADER = "\x52\x49\x46\x46\x24\x20\x00\x00\x57\x41\x56\x45\x66\x6d\x74\x20\x10\x00\x00\x00\x01\x00\x01\x00\x44\xac\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00\x64\x61\x74\x61\x00\x00\x00\x00"

class AudioConnection(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        self.__run = True

        self.sock = None
        self.process = None

        # Read config file
        self.streamserver = "rtmp://stream.benchmarkmonitoring.com.au/live"
        self.streamname = "test"

        self.start()

    def connectBarnOwl(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(5.0)
            self.sock.connect((socket.gethostbyname(socket.gethostname()), 8080))
            self.sock.send("AUD:<EOF>")
        except:
            self.sock = None
            

    def startEncoder(self):
        self.process = subprocess.Popen(["ffmpeg.exe", "-re" ,"-i", "-", "-ab", "128k", "-ar", "44100", "-ac", "1", "-f", "flv", self.streamserver + "/" + self.streamname], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def run(self):

        while self.__run:

            # Connect to barnowl
            if self.sock == None:
                self.connectBarnOwl()

            # Start encoder subprocess
            if self.process == None or self.process.poll() != None:
                self.startEncoder()
                self.process.stdin.write(AUDIO_HEADER)

            # Read audio frame restart connection if faulty
            try:
                audio = self.readAudioFrame()
            except:
                self.sock.close()
                self.sock = None
                continue

            # Write to subprocess
            try:
                self.process.stdin.write(audio)
            except:
                pass

    def readAudioFrame(self):
        r = ""
        audio = ""
        trash1 = self.sock.recv(4)
        
        while True:
            b = self.sock.recv(1)
            if len(b) == 0:
                raise IOError
            r += b
                    
            if r.endswith("<EOF>"):
                audio += r[:-5]
                break
        
        return audio

    def die(self):
        self.__run = False
        self.join()


