'''
--------------------------------------------------------------
DUAL SERVO CONTROL USING PYTHON (pyFirmata) AND ARDUINO

SETUP INSTRUCTIONS:

1. Install Python libraries:
   - pyFirmata: pip install pyfirmata
   - tkinter: included in most Python installations

2. Connect your Arduino board to your PC using USB.

3. Open Arduino IDE.
   - Go to File → Examples → Firmata → StandardFirmata.
   - Upload the StandardFirmata sketch to your Arduino board.
   - This sketch must stay running on your Arduino for Python control.

4. Wire your continuous rotation servos:
   - Connect control signal wires to digital PWM pins (e.g., pin 8 for servo 1, pin 9 for servo 2)
   - Connect servo power supply (VCC/GND) appropriately

5. Edit Python script:
   - Set the correct COM port for your Arduino in the 'ArduinoNano' line (e.g., 'COM3')
   - Adjust the servo pins in the script if needed (servo1_pin, servo2_pin)

6. Run the Python script on your computer.
   - The GUI should open.
   - Use sliders or entry fields to set servo speeds and directions.

7. Your Arduino will respond in real time to the commands sent from Python.

NOTES:
- This workflow does NOT use your usual Arduino C++ code/sketch—you must upload StandardFirmata!
- Disconnect any servo power when uploading StandardFirmata to avoid current spikes.
- If you want to return to regular Arduino code, re-upload your original sketch to the board.
--------------------------------------------------------------
'''

# from pyfirmata import ArduinoNano, SERVO
# import tkinter as tk
# from tkinter import messagebox
# from time import sleep

# board = ArduinoNano('COM3')
# servo1_pin = 8  # Example pin for Servo 1
# servo2_pin = 9  # Example pin for Servo 2
# board.digital[servo1_pin].mode = SERVO
# board.digital[servo2_pin].mode = SERVO

# def set_servo_speed(pin, angle):
#     board.digital[pin].write(angle)

# def CCW():
#     speed_1 = int(rotationSpeed1.get())
#     speed_2 = int(rotationSpeed2.get())
#     # For CW/CCW, continuous servos use 0 for one direction and 180 for opposite direction
#     set_servo_speed(servo1_pin, 180 - speed_1*36) # Max CCW
#     set_servo_speed(servo2_pin, 180 - speed_2*36) # Max CCW
#     sleep(0.1)

# def CW():
#     speed_1 = int(rotationSpeed1.get())
#     speed_2 = int(rotationSpeed2.get())
#     set_servo_speed(servo1_pin, speed_1*36) # Max CW
#     set_servo_speed(servo2_pin, speed_2*36) # Max CW
#     sleep(0.1)

# def aboutMsg():
#     messagebox.showinfo("About", "Logic Don't Care Software\nDual Servo Control Ver 1.0\nNov 2025")

# def quitApp():
#     board.exit()
#     win.destroy()

# win = tk.Tk()
# win.title("Dual Continuous Servo Control")
# win.minsize(320,180)

# tk.Label(win, text="Servo 1 Speed (1-5)").grid(column=1, row=1)
# rotationSpeed1 = tk.Entry(win, bd=6, width=6)
# rotationSpeed1.grid(column=2, row=1)
# tk.Label(win, text="Servo 2 Speed (1-5)").grid(column=3, row=1)
# rotationSpeed2 = tk.Entry(win, bd=6, width=6)
# rotationSpeed2.grid(column=4, row=1)

# tk.Label(win, text="Counter Clock").grid(column=1, row=2)
# CCWBtn = tk.Button(win, text="Rotate CCW", command=CCW)
# CCWBtn.grid(column=2, row=2)

# tk.Label(win, text="Clock").grid(column=3, row=2)
# CWBtn = tk.Button(win, text="Rotate CW", command=CW)
# CWBtn.grid(column=4, row=2)

# aboutBtn = tk.Button(win, bg='yellow', text="About", command=aboutMsg)
# aboutBtn.grid(column=1, row=3)
# quitBtn = tk.Button(win, bg='red', text="QUIT", command=quitApp)
# quitBtn.grid(column=4, row=3)

# win.mainloop()
