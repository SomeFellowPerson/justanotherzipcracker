import os
import zipfile as zf
import argparse
import shutil
from time import sleep
from pynput.keyboard import Key, Listener
from time import time
from datetime import timedelta

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--wordlist", type=str)
parser.add_argument("-z", "--zip", type=str)
arguments = parser.parse_args()


class zipthings():
    
    def doExtract(self, password):
        try:
            self.thezip.extractall(path="contents", pwd=password)
            return password.decode("utf-8")
        except:
            return None
        

    def doBruteForce(self, thezip, wordlist):
        self.thezip = thezip
        lines = open(wordlist, "r", encoding="latin-1").readlines()
        print("Line-list created. Starting to bruteforce.")
        self.starttime = time()
        self.count = 0
        self.length = len(lines)
        for i in lines:
            passw = i.strip("\n").encode("utf-8")
            passresponse = self.doExtract(passw)
            self.count += 1
            if passresponse:
                print(f"Password is: {passresponse}")
                break
            
    def pressedEnter(self, key):
        if str(key) == "'s'":
            print(self.theStats())

    def theStats(self):
        thepercent = round((self.count/self.length)*100, 3)
        secondspassed = time() - self.starttime
        timeremaining = round((((secondspassed)/thepercent)*100)-secondspassed)
        triespersecond = round(self.count/secondspassed)
        statsstring = f"\n{self.count}/{self.length} tries | {thepercent}% completed | {triespersecond}tps (Tries per second)\n{str(timedelta(seconds=timeremaining))} remaining\n\n\n"
        return statsstring
            
        
        


if __name__ == "__main__":
    z = zipthings()
    if arguments.wordlist == None or arguments.zip == None:
        print("Please specify a worldlist/zip file")
        exit()
    Listener(on_press=z.pressedEnter).start()
    thezip = zf.ZipFile(arguments.zip)
    z.doBruteForce(thezip, arguments.wordlist)
    shutil.rmtree("contents")


