
class PlayerButton:
    def __init__(self):
        pass
    def play(self):
        print("La la la....")

class RecordButton:
    def __init__(self):
        pass

    def record(self):
        print("Recording...")

class FastForwardButton:
    def __init__(self):
        pass

    def ff(self):
        print("Fast Forward...")

class RewindButton:
    def __init__(self):
        pass

    def rewind(self):
        print("Rewind..")

class RadioButton:
    def __init__(self):
        pass

    def radioPlay(self):
        print("Radio plays...")

class VolumeButton:
    def __init__(self):
        pass

    def changeVolume(self):
        print("Volume changed..")

class Battery:
    def __init__(self):
        pass

    def batteryStatus(self):
        print("Battery status...")

class BoomBox:
    def __init__(self):
        self.player = PlayerButton()
        self.recorder = RecordButton()
        self.fastforward = FastForwardButton()
        self.rewinder = RewindButton()
        self.radio = RadioButton()
        self.volume = VolumeButton()
        self.battery = Battery()

    def play(self):
        self.player.play()

    def record(self):
        self.recorder.record()

    def fastForward(self):
        self.fastforward.ff()

    def rewind(self):
        self.rewinder.rewind()

    def radioPlay(self):
        self.radio.radioPlay()

    def changeVolume(self):
        self.volume.changeVolume()

    def batteryStatus(self):
        self.battery.batteryStatus()

if __name__ == '__main__':
    bb = BoomBox()

    bb.batteryStatus()
    bb.play()
    bb.rewind()
    bb.record()
    bb.batteryStatus()
    bb.changeVolume()