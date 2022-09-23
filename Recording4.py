"""
-------------------------------
Welcome to the recording series
-------------------------------
This program records a seies of .WAV files and stores their names in a .txt file
Make sure wave_files_log.txt file exists in this directory

"""

import sounddevice as sd
from scipy.io.wavfile import write
import os
from Tab4 import printTab, tabMaker


### Store wav files in new folder ###
main_path = os.getcwd()
wave_file_path = main_path + "/Wave_Files"


fs = 44100  # Sample rate in Hz
duration = 1  # Length of recording in seconds

session_name = input("Name the recording session (no extension) ")
i = 0 # iterates for each recording




while True:
    
    
    ### Display tabs ###
    print("~"*60)
    print("Here is your tab: ", "\n")
    tab = tabMaker(method = "random")
    printTab(tab)
    
    
    ### User input to start recording ###
    user_input = input("Start recording? (y/n) ")
    if user_input != "y":
        print("Program terminated")
        break
    


    ### Recording happens ###
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  
    
    
    ### Create a file name ###
    file_name = session_name + "_" + str(i) + ".wav"
    i += 1
    
    
    os.chdir(wave_file_path)            # Move to wav file folder
    write(file_name, fs, myrecording)   # Save as WAV file 
    
    
    os.chdir(main_path)                 # Move back to main folder
    
    with open("wave_files_log.txt", "a") as wave_files_log: # Record WAV file creation
        wave_files_log.write(file_name + "," +  str(tab) + "\n")



    print(file_name, "has been created!")
    
    
    
    
    
wave_files_log.close()










