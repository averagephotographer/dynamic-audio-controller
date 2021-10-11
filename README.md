# Dynamic Audio Controller

## Idea
This idea came around when I was trying to switch between listening to Spotify and watching YouTube tutorials quickly. I'd go pause one and unpause the other and undo it when I went back to work. This got tedious so I decided to make a script to automate it for me.


## How it works
* Prioritize programs (i.e. Spotify, Chrome, Discord, etc.)
* If a higher priority program is playing audio, lower the volume of the lower priority ones
* Controls Windows Volume Mixer (WVM) depending on what programs are running

## What doesn't work
* script cannot tell if a program is playing audio. It can only tell if it's connected to the WVM
