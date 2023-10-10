# Engineering3 
# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

##  Hello_CircuitPython

### Description & Code
This asignment was to make a led flash a rainbow. i did this by wiring the led to the arduino then did the code. I-+ lost my code, but this is similar to it. 
```C
void setup()  { 
 
} 
 
void loop()  {
 
 
  for(int b = 0 ; b <= 255; b=b+5) 
  { 
      for(int g = 0 ; g <= 255; g=g+5) 
    { 
      for(int r= 0 ; r <= 255; r=r+5) 
       { 
        analogWrite(9, b);         
        analogWrite(10, g);         
        analogWrite(11, r);    
        delay(10);
 
      } 
    }
  }
 
}
```
credit goes to [seeeddoc.github.io](https://seeeddoc.github.io/Arduino_Sidekick_Basic_Kit/)

### Evidence

### Wiring


<img src="https://seeeddoc.github.io/Arduino_Sidekick_Basic_Kit/img/Arduino_Sidekick_RGB_LED_Display.jpg"  style="width:500px;">


image credit goes to [https://seeeddoc.github.io(/Arduino_Sidekick_Basic_Kit/)
### Reflection
This asignment wasn't even hard i just had to look up how to wire a led. Cause i always wire first then do my code. 






## CircuitPython_LCD

### Description & Code

```python
Code goes here
import board
import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# turn on lcd power switch pin
lcdPower = digitalio.DigitalInOut(board.D8)
lcdPower.direction = digitalio.Direction.INPUT
lcdPower.pull = digitalio.Pull.DOWN

# Keep the I2C protocol from running until the LCD has been turned on
# You need to flip the switch on the breadboard to do this.
while lcdPower.value is False:
    print("still sleeping")
    time.sleep(0.1)

# Time to start up the LCD!
time.sleep(1)
print(lcdPower.value)
print("running")

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)


# Loop forever.
while True:
```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring


### Reflection


## circuitphython_servo

### Description & Code
This asignment was to get 2 buttons and when u press one button it goes to 180 and when u press the other one it goes to 0.
I got this working by getting the buttons working then add the code. 


```python
Code goes here
 Create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

#button 1 turns to 180
btn = DigitalInOut(board.D11)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

#button 2 turns to 0
btn2 = DigitalInOut(board.D6)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

while True:
    # if button 1 is pressed then it will turn to 180
    if btn.value:
        my_servo.angle = 180
        time.sleep(0.02 )
        print("BTN1 is pressed") 
        # if button 2 is pressed it will turn to 0
    if btn2.value:
        my_servo.angle = 0
        time.sleep(0.05)
        print("BTN2 is pressed")


```

### Evidence

### Wiring
![buttonServoWiring](https://github.com/Mgray881/ENG3/assets/143528424/6c9d90a5-d094-45cc-bd45-f1122d33e2f1)



### Reflection
This asignment was hard but once i asked my classmate she told me what to do and it got easier. i used goggle to look up "how to wire a button." and i used adafruit to get the code.


## Circuirtphython Distance Sensor

### Description & Code
This asignment was to measure the distance to an object using HC-SR04. Also we had to use a neopixel to turn red when objects is less than 5cm, and when its green it turn to 35cm.
```python
Code goes here
import time
import board
from rainbowio import colorwheel
import neopixel
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D13, echo_pin=board.D12)
print("starting")
cm = 0

NUMPIXELS = 1  # Update this to match the number of LEDs.
BRIGHTNESS = 0.2  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL  # This is the default pin on the 5x5 NeoPixel Grid BFF.

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

while True:
    try:
        cm = sonar.distance
        print(cm)
        if cm < 5:
            pixels.fill(RED) 
        elif cm > 35:
            pixels.fill(GREEN)
        else:
            pixels.fill(BLUE)
        pixels.show()
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

```
code helped from alexis and adafruit website

### Evidence

### Wiring
![ultrasonic-sensor-hc-sr04/](https://howtomechatronics.com/wp-content/uploads/2022/02/HC-SR04-Ultrasonic-Sensor-Arduino-Connection-Wiring-1024x580.png?ezimgfmt=ng:webp/ngcb2)

image credit goes to [howtomechatronics.com](https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/)


### Reflection
this assigment was easy i just loooked up how to wire a hc-sr04 circuit phython and it showed me how to wire it and gave me a code. And my friend Alexis helpled me get the code for the neopxel and she helped me make sure everything was good.


## Motor control

### Description & Code Snippets
this asignment was to wire up a 6v battery pack to the metro with a motor, we also had to write a phython code to make the motor speed up and slow down. 
  

```python
Code goes here
import time
import board
from analogio import AnalogIn
import pwmio
pin = AnalogIn(board.A1)
motor = pwmio.PWMOut(board.D5)
while True: 

    print(pin.value)
    time.sleep(0.1)
    motor.duty_cycle = pin.value
```


**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring

<img src = "images/motorcontrol.jpg" width="500" >

### Reflection
this assignment was easy, the wiring was kinda hard because it was alot to wire. but the code was easy i thought it was gonna have to be long beeing that we used a lot of matrials such as batterty pack, the motor, the Potentiometer and the transistor.


## CircuitPhython Photointerrupters 

### Description & Code Snippets
this asignment was to Wire up your photointerrupter and have it keep track of how many times it has been interrupted.
```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring

### Reflection



## NextAssignment

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](:http//guides.github.com/features/mastering-markdown/)
### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**


## the hanger

### Assignment Description
we had to create a hanger on onshape. 
### Evidence


### Part Link 

https://cvilleschools.onshape.com/documents/2e8dfbcded09e66a270bbb18/w/b9bc7ad52ff04cab243d2807/e/5ca39b632d2663b1e46d01f0

### Reflection
this assignment was easy all i had to was look at the picture. I did get stuck doing some of the dimentions but alexis and mr. dierof helpled me. once i made one side of the hanger the other side was easy cause all i had to do was use the mirror tool.


## the swing arm

### Assignment Description
for this asignment we had to look at different pictures of the swing arm and make it.

### Evidence


### Part Link 
https://cvilleschools.onshape.com/documents/c9d45026a84cfd0c3c2bb8d7/w/be2364a1204e00b5b7cff7b4/e/716cf72a171e4ce0c0e34ed9

### Reflection
this asignment was hard. gudrun helped me do everything she showed me how to make the different parts, but of course i knew how to extrude and use the tools.



## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence

Take several cropped screenshots of your Onshape document from different angles. Try to capture all important aspects of the design. Turn off overlays that obscure the parts, such as planes or mate connectors. Your images should have captions, so the reader knows what they are looking at!  

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!




