from tkinter import *
import serial

bounceCounter = 0


def init_window(self):
    # size of the window
    self.geometry("400x300")

    # changing the title of our master widget
    self.title("GUI")


def initComPort():
    serialObj.port = "/dev/ttyS3"
    serialObj.baudrate = 9600
    serialObj.open()


def checkSerialPort(dataframe):
    if serialObj.isOpen() and serialObj.in_waiting:
        recentPacket = serialObj.readline()

        if recentPacket != None:
            global bounceCounter
            bounceCounter += 1
            text = Label(dataframe, text=str(bounceCounter),
                         font=('Calibri', '13'), bg='white')
            text.pack()

        if bounceCounter >= 10:
            resetBounceCounter()


def resetBounceCounter():
    global bounceCounter
    bounceCounter = 0


win = Tk()
init_window(win)

# ports = serial.tools.list_ports.comports()
serialObj = serial.Serial()

initComPort()


while True:
    win.update()
    checkSerialPort(win)
