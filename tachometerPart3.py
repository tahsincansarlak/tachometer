import machine, network, ubinascii, ujson, urequests, utime
from pyb import Pin

pin1 = Pin('Y4', Pin.IN)
pin2 = Pin('Y3', Pin.IN)
runPin = Pin('X3',Pin.OUT)
class Encoder(object):
    def __init__(self, pin_x, pin_y, reverse, scale):
        self.reverse = reverse
        self.scale = scale
        self.forward = True
        self.pin_x = pin_x
        self.pin_y = pin_y
        self._pos = 0
        self.x_interrupt = pyb.ExtInt(pin_x, pyb.ExtInt.IRQ_RISING_FALLING, pyb.Pin.PULL_NONE, self.x_callback)
        self.y_interrupt = pyb.ExtInt(pin_y, pyb.ExtInt.IRQ_RISING_FALLING, pyb.Pin.PULL_NONE, self.y_callback)

    def x_callback(self, line):
        self.forward = self.pin_x.value() ^ self.pin_y.value() ^ self.reverse
        self._pos += 1 if self.forward else -1

    def y_callback(self, line):
        self.forward = self.pin_x.value() ^ self.pin_y.value() ^ self.reverse ^ 1
        self._pos += 1 if self.forward else -1

    @property
    def position(self):
        return self._pos*self.scale

    def reset(self):
        self._pos = 0

def trinket(motorvalue):
     if motorvalue > 150:
          runPin(255) 
def main():
     print("started")
     e = Encoder(pin1,pin2,False,0.5)
     print("here")
     e.reset()
     print("Getting close")
     while True:
          angle = e.position
          print("angle")
          print(angle)
          trinket(angle)
          utime.sleep(1)
          
if __name__ == '__main__':
     main()