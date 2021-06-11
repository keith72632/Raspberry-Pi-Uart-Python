#port /dev/serial0
#in /boot/config.txt, if enable_uart = 0 mini uart. if enable_uart = 1 PL011 is primary uart
#on host. cat /dev/ttyUSB0. putty and screen don't work well

import time 
import serial
import sys

ser = serial.Serial("/dev/ttyS0", baudrate = 9600, parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)


def uart_init():
    sys.stdout = open('logs.txt', 'w')
    counter = 0
    try:
        while 1:
            ser.write(b'Write counter: %d \n'%(counter))
            print('Count: %d\r\n'%(counter))
            time.sleep(1)
            counter += 1
    except KeyboardInterrupt:
        ser.write(b'Keyboard Interrupt. Program closed\n')
        print("KeyboardInterrupt")
        sys.stdout.write('Keyboard Interrupt')
        sys.stdout.close()

if __name__ == "__main__":
    uart_init()
