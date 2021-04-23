"""
Mutes the volume of all processes, but unmutes chrome.exe process.
"""
from pycaw.pycaw import AudioUtilities

# priorities
spotify = "Spotify.exe"
chrome = "chrome.exe"
twitch = "TwitchUI.exe"
discord = "Discord.exe"
explorer = "explorer.exe"
zoom = "Zoom.exe"

priority = {
    chrome: 0,
    discord: 0,
    spotify: 1,
    twitch: 1,
    explorer: 1
}


def lower(program):
    for session in sessions:
        # print(session.Process)
        volume = session.SimpleAudioVolume
        print(session.Process.name())
        if session.Process and session.Process.name() == program:
            volume.SetMasterVolume(.3, None)
            break


def isRunning(program):
    for session in sessions:
        if session.Process and session.Process.name() == program:
            return True


# def priority(name):
#     if name == chrome or name == discord:
#         return 0
#     if name == spotify or name == twitch or name == explorer:
#         return 1
#     else:
#         return 2


if __name__ == "__main__":
    sessions = AudioUtilities.GetAllSessions()
    # get highest
    highest = ""
    for session in sessions:
        if priority[session.Process.name()] < priority[highest]:
            highest = session.Process.name()
            # print(highest)

    print("final: {}".format(highest))

    # if isRunning(chrome):
    #     lower(spotify)
