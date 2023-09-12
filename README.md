# Online Operated LED Screen

## Operating an LED 16 x 2 Screen using a Raspberry Pi Pico W

This project is a small, easy to set up, dive into the Pico W's capabilities. It does that by hosting an web page with an input field which, once submitted, uploads it to the LED Screen (16x2)

This code is written in MicroPython and is ment to be used in the Thonny IDE

For the LED Screen API I have to give credit to https://github.com/T-622/RPI-PICO-I2C-LCD for the code

The set up should take at most 30 minutes, then you can experiment with it yourself, hope you will have fun!

![Raspberry-Pi-Pico-with-I2C-LCD-connection-diagram](https://github.com/TudorFerecus/Online-Operated-LED-Screen/assets/89069348/049763a3-e41d-4924-8e63-562550b22880)

## What do I need for it?

 Hardware wise, you will need:

* Raspberry Pi Pico W (it has to be the W series because it's the only one that has WI-FI)
* LED Screen 16x2 with I2C Interface
B to Micro USB cable
* 4 Jumper cables (I used female-female, but you should use which one works for you and your pin types)

## Step by step guilde

* Download Thonny
* Connect LED display to Pico Pi W as showed in the photo above (if you want to change the pins, consult the "Alternative Pin Layout" to make it work)
* Connect the Pico to the Computer (the IDE should recognise it)
* Add the files to the Pico using the Thonny File Manager (left side of the page)
* Add the SSID and Password in this fields, in constants.py:
  
  ``` python
  ssid = 'YOUR_SSID_HERE'
  wlan_password = 'YOUR_PASSWORD_HERE'

  ```
* Run the "main_LED_remote.py" file in Thonny
* If errors appear press stop and run the file again, if there are still errors, plug and unplug the Pico and try again
* Look in the console, there you should see the Link (consisting of the Pico's IP adress), paste it in your browser
* To see the text on your LED Screen type something in the input and press the button
* That's all :)

## Alternative Pin Layout

If, for any reason, you want to connect other GPIO pins to the LED Screen's I2C, you can do this in a simple way, but you need to do 2 extra steps
* First, change the I2C_SDA_PIN value from the "constants.py" file to the GPIO pin you connected to the SDA pin from the I2C and do the same for the I2C_SCL_PIN
* Then, run the "scan.py" file and copy the output from the console, that is the I2C's addres you will convert in the next step
* After that, go to https://www.rapidtables.com/convert/number/decimal-to-hex.html (or any other decimal to hex website) and paste the addres you got from the previous step
* Finally, paste the website's output to the I2C_ADDR in the "constants.py" file
* You should be all set, DO NOT FORGET, this step is not necessary if you do not change the pins



by Tudor Ferecus, cheers!
