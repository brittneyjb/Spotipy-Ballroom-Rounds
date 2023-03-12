# Spotipy-Ballroom-Rounds

### Disclaimer:
This is a script created by Brittney Bush in her freetime. This is not created with best practices in mind it was simply a "can I do this" manner.  
Please submit any pull requests here and I will review.  
Before submitting any merge requests, please remove your personal user_id and laptop(device_id).  
This script has currently only been run on my machine and using a spotify premium account.  

### To Use:
In lines 8 & 9, you will need to add your personal Spotify user id and laptop(device id).   
The user id is listed as "username" in your account overview.  
The laptop(device id) can be easily surpassed by changing line 9 to: `laptop = sp.devices()['devices'][0]['id']`

### First Run:
Ensure Spotify is open on your computer.  
During the first run of the code, Spotify will prompt asking for the required permissions for the script to function.  
Click "Authorize" or "Allow" (I can't remember which). You will be redirected to the Google homepage.  
Copy the url you were redirected to and paste in the terminal, then click enter to continue.  
Continue to follow the prompts and enjoy.  

### Spotipy Documentation:
https://spotipy.readthedocs.io/en/2.22.1/#  
Examples: https://github.com/spotipy-dev/spotipy-examples
