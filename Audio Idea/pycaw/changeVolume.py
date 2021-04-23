from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


def main():
    # this code turns the master volume of whatever appication down to 30% of whatever the master volume is
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        print(session.Process.name())
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Spotify.exe":
            print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(1, None)


def priority():
    # priority default is 0, highest priority is 1
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        name = session.Process.name()
        if name == "chrome.exe":
            return 1
        if name == "Spotify.exe":
            return 2
        else:
            return 0


if __name__ == "__main__":
    main()
