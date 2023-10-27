# rat-lab

This is a repository of some experiments with how Windows Defender detects Command and Control. I plan on testing using Websockets, Discord, and IRC for C2.

# Discord RAT

Very simple remote access toolkit that uses discord for command and control. I have found that this makes detection more difficult because traffic to discord is not unusual.

Libraries for making discord bots can very easily be used for making RATs. In my example I used discord.py, but go might be a better option because you could use [gobfuscate](https://github.com/unixpickle/gobfuscate).

I made an exe file using pyinstaller, but other languages have better compilation options.

# Findings

## Heuristic Detection 
* Connecting to unknown server at boot can trigger detection
* Establishing persistance in shell:startup can trigger detection
* Establishing persistance in registry does not trigger detection
* Unencrypted C2 is more likely to trigger detection than encrypted C2 

## Signature Based Detection
* Flipped bit in .exe stops it
* Does not detect similar behaviors between executables with static analysis