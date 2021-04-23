"""
Mutes the volume of all processes, but unmutes chrome.exe process.
"""
from pycaw.pycaw import AudioUtilities
from time import sleep

# priorities
spotify = "Spotify.exe"
chrome = "chrome.exe"
twitch = "TwitchUI.exe"
discord = "Discord.exe"
explorer = "explorer.exe"
zoom = "Zoom.exe"


def change(program, vol):
    for session in sessions:
        # print(session.Process)
        volume = session.SimpleAudioVolume
        # print(session.Process.name())
        if session.Process and session.Process.name() == program:
            volume.SetMasterVolume(vol, None)
            break


def isRunning(program):
    for session in sessions:
        if session.Process and session.Process.name() == program:
            return True


def priority(name):
    if name == chrome or name == discord:
        return 0
    if name == spotify or name == twitch or name == explorer:
        return 1
    else:
        return 1


if __name__ == "__main__":
    while(True):
        sessions = AudioUtilities.GetAllSessions()
        # get highest
        highest = ""
        for session in sessions:
            if priority(session.Process.name()) < priority(highest):
                highest = session.Process.name()
                # print(highest)

        print("final: {}".format(highest))

        # set highest priority to full volume, set lower priorities to 0.3
        for session in sessions:
            if priority(session.Process.name()) > priority(highest):
                change(session.Process.name(), 0.1)
            else:
                change(session.Process.name(), 1)
    sleep(500)

    # use dictionary?
    # if isRunning(chrome):
    #     lower(spotify)
