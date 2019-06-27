import machine, network, ubinascii, ujson, urequests, utime
from pyb import Pin

WiFi = network.WLAN()
pin1 = Pin('Y4', Pin.IN)
pin2 = Pin('Y3', Pin.IN)

mac = ubinascii.hexlify(network.WLAN().config("mac"),":").decode()
#MAC address: 48:4a:30:01:6d:50 Pyboard New
#MAC address: 48:4a:30:01:6c:70 Pyboard
print("MAC address: " + mac)
def connect():
     EN1 = machine.Pin("W23", machine.Pin.OUT, value=1)  # set power high for USB power (500mA now allowed)
     if not WiFi.isconnected():
          print ("Connecting ..")
          WiFi.active(True)
          #WiFi.scan()
          WiFi.connect("Network","Password")
          WiFi.connect("Tufts_Wireless","")
          i=0
          while i < 50 and not WiFi.isconnected():
               utime.sleep_ms(200)
               i=i+1
          if WiFi.isconnected():
               print ("Connection succeeded")
          else:
               print ("Connection failed")

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
        
def gaugevalue(turningval):
	Tag = "tachovalue"
	Type = "DOUBLE"
	Key = "Q6g3YI_v6cdfkAHHoV8RFSzG-3ANPXGhhV0MfbIrm-"
	urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
	urlTag = urlBase + Tag
	urlValue = urlBase + Tag + "/values/current"
	headers = {"Accept":"application/json","x-ni-api-key":Key}
	angle = str(turningval)
	propName={"type":Type,"path":angle}
	propValue = {"value":{"type":Type,"value":angle}}
	print(urequests.put(urlTag,headers=headers,json=propName).text)
	print(urequests.put(urlValue,headers=headers,json=propValue).text)
	
def led1(turnonval):
	if turnonval > 100:
		Tag = "led1"
		Type = "BOOLEAN"
		Key = "Q6g3YI_v6cdfkAHHoV8RFSzG-3ANPXGhhV0MfbIrm-"
		urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
		urlTag = urlBase + Tag
		urlValue = urlBase + Tag + "/values/current"
		headers = {"Accept":"application/json","x-ni-api-key":Key}
		angle = str(True)
		propName={"type":Type,"path":angle}
		propValue = {"value":{"type":Type,"value":angle}}
		print(urequests.put(urlTag,headers=headers,json=propName).text)
		print(urequests.put(urlValue,headers=headers,json=propValue).text)
	else:
		Tag = "led1"
		Type = "BOOLEAN"
		Key = "Q6g3YI_v6cdfkAHHoV8RFSzG-3ANPXGhhV0MfbIrm-"
		urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
		urlTag = urlBase + Tag
		urlValue = urlBase + Tag + "/values/current"
		headers = {"Accept":"application/json","x-ni-api-key":Key}
		angle = str(False)
		propName={"type":Type,"path":angle}
		propValue = {"value":{"type":Type,"value":angle}}
		print(urequests.put(urlTag,headers=headers,json=propName).text)
		print(urequests.put(urlValue,headers=headers,json=propValue).text)

def led2(turnonval2):
	if turnonval2 > 200:
		Tag = "led2"
		Type = "BOOLEAN"
		Key = "Q6g3YI_v6cdfkAHHoV8RFSzG-3ANPXGhhV0MfbIrm-"
		urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
		urlTag = urlBase + Tag
		urlValue = urlBase + Tag + "/values/current"
		headers = {"Accept":"application/json","x-ni-api-key":Key}
		angle = str(True)
		propName={"type":Type,"path":angle}
		propValue = {"value":{"type":Type,"value":angle}}
		print(urequests.put(urlTag,headers=headers,json=propName).text)
		print(urequests.put(urlValue,headers=headers,json=propValue).text)
	else:
		Tag = "led2"
		Type = "BOOLEAN"
		Key = "Q6g3YI_v6cdfkAHHoV8RFSzG-3ANPXGhhV0MfbIrm-"
		urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
		urlTag = urlBase + Tag
		urlValue = urlBase + Tag + "/values/current"
		headers = {"Accept":"application/json","x-ni-api-key":Key}
		angle = str(False)
		propName={"type":Type,"path":angle}
		propValue = {"value":{"type":Type,"value":angle}}
		print(urequests.put(urlTag,headers=headers,json=propName).text)
		print(urequests.put(urlValue,headers=headers,json=propValue).text)

def led3(turnonval3):
	if turnonval3 > 300:
		Tag = "led3"
		Type = "BOOLEAN"
		Key = "Q6g3YI_v6cdfkAHHoV8RFSzG-3ANPXGhhV0MfbIrm-"
		urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
		urlTag = urlBase + Tag
		urlValue = urlBase + Tag + "/values/current"
		headers = {"Accept":"application/json","x-ni-api-key":Key}
		angle = str(True)
		propName={"type":Type,"path":angle}
		propValue = {"value":{"type":Type,"value":angle}}
		print(urequests.put(urlTag,headers=headers,json=propName).text)
		print(urequests.put(urlValue,headers=headers,json=propValue).text)
	else:
		Tag = "led3"
		Type = "BOOLEAN"
		Key = "Q6g3YI_v6cdfkAHHoV8RFSzG-3ANPXGhhV0MfbIrm-"
		urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
		urlTag = urlBase + Tag
		urlValue = urlBase + Tag + "/values/current"
		headers = {"Accept":"application/json","x-ni-api-key":Key}
		angle = str(False)
		propName={"type":Type,"path":angle}
		propValue = {"value":{"type":Type,"value":angle}}
		print(urequests.put(urlTag,headers=headers,json=propName).text)
		print(urequests.put(urlValue,headers=headers,json=propValue).text)

def main():
     connect()
     e = Encoder(pin1,pin2,False,0.5)
     e.reset()
     while True:
          angle = e.position
          led1(angle)
          led2(angle)
          led3(angle)
          gaugevalue(angle)
          utime.sleep(1)
if __name__ == '__main__':
     main()
