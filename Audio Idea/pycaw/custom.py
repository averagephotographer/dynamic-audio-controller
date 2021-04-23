from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume, AudioSession
from time import sleep

spotify = 'Spotify.exe'
chrome = 'chrome.exe'
twitch = 'TwitchUI.exe'
discord = 'Discord.exe'
explorer = 'explorer.exe'


def getSessions():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        sessionList.append(session.Process.name())
        print(sessionList)


def main():
    # find the highest priority program, make all the other programs lower their volume
    highest = sessionList[0]
    for i in range(len(sessionList)):
        try:
            if priority(sessionList[i]) < priority(highest):
                highest = sessionList[i]
        except:
            pass

    for i in (sessionList):
        # print("i: {}, highest: {}".format(i, highest))
        if priority(i) > priority(highest):
            change(i, 0.05)
        else:
            change(i, 1)
            test(i)


def change(program, amount):
    # this code turns the master volume of whatever appication down to 30% of whatever the master volume is
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    if session.Process and session.Process.name() == program:
        volume.SetMasterVolume(amount, None)


def test(program):
    test = session._ctl.QueryInterface(IAudioEndpointVolume)
    if session.Process and session.Process.name() == program:
        print(test.GetVolumeRange())


def priority(name):
    # priority default is 10, highest priority is 1
    if name == chrome or name == discord:
        return 1
    if name == spotify or name == twitch or name == explorer:
        return 2
    else:
        return 3


# while(True):
sessionList = []
getSessions()
if spotify in sessionList:
    main()
    # sleep(5)
