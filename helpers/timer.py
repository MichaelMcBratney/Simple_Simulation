from threading import Timer


class CustomTimer:
    def __init__(self, interval, function, *args):
        self.timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.is_active = False

    def run(self):  # when this function is called, it calls back the start function, thereby creating a loop
        self.is_active = False
        self.start()
        self.function(*self.args)

    def start(self):
        if not self.is_active:
            self.timer = Timer(self.interval, self.run)
            self.timer.start()  # this line calls the run function after the given interval
            self.is_active = True

    def stop(self):  # this is used to stop the timer
        self.timer.cancel()
        self.is_active = False
