class MusicPlayer:

    def __init__(self, tracks):
        self.tracks = tracks

    def take_photo(self):
        print("WOW PLAYER WITH CAMERA!")

    def play_track(self):
        print("PLAY", self.tracks[0])

    def pause_track(self):
        print("Pause")


class Camera:

    def __init__(self, matrix, lense, storage):
        self.matrix = matrix
        self.lense = lense
        self.storage = storage


    def take_photo(self):
        print("Cheese!")

    def record_video(self):
        print("Start ... Stop")


class Phone:

    def __init__(self, sim_card, battery):
        self.sim_card = sim_card
        self.battery = battery

    def call(self, number):
        print(f"Calling {number}")

    def send_message(self, number, message):
        print(f"Send '{message}' to {number}")


class SmartPhone(MusicPlayer, Phone, Camera):
    ...



ipod = MusicPlayer([1, 2, 34, 4, 5])
ipod.play_track()
ipod.pause_track()


nicon = Camera("Matrix 2", "glass", "sd-card")
nicon.take_photo()
nicon.record_video()


nokia = Phone("JEANS", "30000mAh")
nokia.call(32112312)
nokia.send_message( 31232312, "Hello")


xiaomi_super_extra_3000 = SmartPhone("VODAPHONE")


xiaomi_super_extra_3000.play_track()
xiaomi_super_extra_3000.pause_track()
xiaomi_super_extra_3000.take_photo()
xiaomi_super_extra_3000.record_video()
xiaomi_super_extra_3000.call(532432904324)
xiaomi_super_extra_3000.send_message(432432432, "kdnsjdnawjdn")



