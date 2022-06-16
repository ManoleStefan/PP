import abc

class BoomboxFacade:
    def __init__(self):
        self.boombox = Boombox()

    def Play(self):
        if self.boombox.mode.GetMode() == "On tape mode":
            if self.boombox.tape != None:
                self.boombox.tape.Play()
                self.boombox.mode = OnTapeMode()
            else:
                print("Please Insert Tape")
        else:
            print("Radio Started")

    def Stop(self):
        if self.boombox.mode.GetMode() == "On tape mode":
            if self.boombox.tape != None:
                self.boombox.tape.Stop()
            else:
                print("No Tape Inserted")
        else:
            print("Radio Stopped")

    def FastForward(self):
        if self.boombox.tape != None:
            self.boombox.tape.FastForward()
        else:
            print("No Tape Inserted")

    def Rewind(self):
        if self.boombox.tape != None:
            self.boombox.tape.Rewind()
        else:
            print("No Tape Inserted")

    def InsertTape(self, tape):
        self.boombox.InsertTape(tape)

    def RemoveTape(self):
        self.boombox.RemoveTape()

    def ShowBattery(self):
        print(str(self.boombox.GetBattery()) + "% left")

    def ShowStatus(self):
        print("Current status: " + self.boombox.GetStatus())

    def VolumeUp(self):
        self.boombox.volumeManager.VolumeUp()

    def VolumeDown(self):
        self.boombox.volumeManager.VolumeDown()

    def ShowVolume(self):
        print("Volume: " + str(self.boombox.volumeManager.GetVolume()))

    def Record(self):
        if self.boombox.tape != None:
            self.boombox.recordingManager.Record()
        else:
            print("Please Insert Tape To Record On")


    def StopRecording(self):
        if self.boombox.tape != None:
            self.boombox.recordingManager.StopRecording()
        else:
            print("No Tape Inserted")

    def Radio(self):
        self.boombox.mode = OnRadioMode()

    def ListenTape(self):
        if self.boombox.tape != None:
            self.boombox.mode = OnTapeMode()
        else:
            print("Please Insert Tape")

class Boombox:
    def __init__(self):
        self.volumeManager = VolumeManager()
        self.recordingManager = RecordingManager()
        self.battery = 100
        self.tape = None
        self.mode = OnRadioMode()

    def InsertTape(self, tape):
        self.tape = tape

    def RemoveTape(self):
        self.tape = None
        self.mode = OnRadioMode()

    def GetBattery(self) -> int:
        return self.battery

    def GetStatus(self) -> str:
        return self.mode.GetMode() + " Recording: " + str(self.recordingManager.GetRecordingStatus())



class VolumeManager:
    def __init__(self):
        self.volume = 50

    def VolumeUp(self):
        print("Volume Up")
        self.volume = self.volume + 1
        if self.volume > 100:
            self.volume = 100

    def VolumeDown(self):
        print("Volume Down")
        self.volume = self.volume - 1
        if self.volume < 0:
            self.volume = 0

    def GetVolume(self) -> int:
        return self.volume


class RecordingManager:
    def __init__(self):
        self.isRecording = False

    def Record(self):
        print("Start Recording")
        self.isRecording = True

    def StopRecording(self):
        print("Stop Recording")
        self.isRecording = False

    def GetRecordingStatus(self) -> bool:
        return self.isRecording

class ITape(metaclass=abc.ABCMeta):
    def Play(self):
        pass
    def Stop(self):
        pass
    def FastForward(self):
        pass
    def Rewind(self):
        pass

class RockMusicTape(ITape):
    def __init__(self, band):
        self.band = band

    def Play(self):
        print("Play tape " + self.band)

    def Stop(self):
        print("Stop tape " + self.band)

    def FastForward(self):
        print("Fast Forward Tape")

    def Rewind(self):
        print("Rewind")

class IMode(metaclass=abc.ABCMeta):
    def GetMode(self) -> str:
        pass

class OnRadioMode(IMode):
    def __init__(self):
        self.modeName = "On radio mode"

    def GetMode(self) -> str:
        return self.modeName

class OnTapeMode(IMode):
    def __init__(self):
         self.modeName = "On tape mode"

    def GetMode(self) -> str:
        return self.modeName

if __name__ == '__main__':
    tape1 = RockMusicTape("Metallica")
    tape2 = RockMusicTape("Guns'n Roses")
    tape3 = RockMusicTape("Empty tape")

    boombox = BoomboxFacade()

    boombox.InsertTape(tape1)
    boombox.ListenTape()

    boombox.Play()
    boombox.FastForward()
    boombox.Stop()

    boombox.RemoveTape()
    boombox.InsertTape(tape3)
    boombox.Radio()
    boombox.Play()

    boombox.Record()
    boombox.StopRecording()

    boombox.Stop()
    boombox.RemoveTape()

    boombox.InsertTape(tape2)
    boombox.ListenTape()
    boombox.Play()
    boombox.ShowStatus()

    for i in range(0, 5):
        boombox.VolumeUp()

    boombox.ShowVolume()
    boombox.ShowBattery()

    boombox.Stop()
    boombox.RemoveTape()
