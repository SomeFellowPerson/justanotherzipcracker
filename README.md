# justanotherzipcracker
A python script to crack zip passwords. It works by iterating through wordlists, therefore you can use tools like "crunch" to generate those


justanotherzipcracker is a CLI tool (No GUI!)  
The Syntax goes as follows:  
*************************************************************  
python crack_zip.py -w <wordlist-of-choice> -z <zip-to-crack>  
*************************************************************  
You can display the progress of the cracking process by pressing "s" on the keyboard  
  
In the repository I have added an example zip file which I used to confirm the functionality of the script.
Since github won't allow me to upload any files bigger than 25MB here is a worldist I generated with crunch  
that suits the zip's password pattern: https://mega.nz/file/QPoDkaxB#CERLFPgIgC5D1b-dd6SlKRVY7L4J_blTO5KT5iBcNRo  
The wordlist contains every 1 to 4 character long combination from the alphabet (up- and lowercase) plus all digits from 0-9.    
If you want to you can try it out for yourself, the correct password should be found at around 42%-43%.  
Crunch command for wordlist: Crunch command: crunch 1 4 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -o passes.txt
  
  

