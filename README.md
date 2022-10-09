# Pinewood ECTO-1

A simple circuit for lights and sound for an ECTO-1 Pinewood racer

First, the full build log is [here on Imgur](https://imgur.com/a/gDuQvSt).

Background: In January of 2019 I entered a “Back to the Future” inspired DeLorean for a Pinewood Derby race among the adults from our local Girl Scout troops. It had a balsa body and super-small LED’s to light up the exterior. By the time the race was done I already knew what movie vehicle I wanted for the 2020 race: ECTO-1. I set out to do another balsa-carved model but ended up getting my first 3D printer mid-year and knew exactly what I needed to do. My intent was to find a suitable STL model for printing, and modify it for use with the Pinewood Derby kit which meant fitting it over the block so as to keep the axle positions and meet the rule requirements. In essence, I built a shell for my block of wood which meets all measurement and weight requirements while providing me a very recognizable shape with all the expected details in lights, fins, and accessories.

My work began with the following [STL from Thingiverse](https://www.thingiverse.com/thing:2980759), which I then imported the model into Blender for modification. This is where my learning curve made a steep climb, but I figured out how to subtract a perfect cubic block of material from within the body of the vehicle to allow everything to fit together. That meant ensuring the wheel wells had enough clearance and (unfortunately) cutting away some portions of the body to make things fit since I was dealing with rigid requirements for vehicle rules. The final model was exported as an STL and sliced in Cura after scaling approximately 174%.

What movie car would be complete without lights AND sound? For this work I knew that I wanted both some lights for the top of the car as well as the distinctive whine of the siren. For that, I started with some standard sound effects (http:// hprops.com/sounds) and looked at the necessary hardware. I ended up buying the wrong type of board which didn’t support audio, and found that I also needed an amplifier to really get a loud enough output. That led me to the ItsyBitsy M0 Express and I2S 3watt amp breakout boards. Using the CircuitPython (more my speed with coding) I created a simple playback loop which would wait for a button press to restart the audio clip. While the audio played, I then used PWM to cycle 2 sets of LED’s up and down in brightness. This gave my lights a nice look as they pulse back and forth and matches the playback of whatever audio clip I load.

Here is the bill of materials for the electronics:

* [ItsyBitsy M0 Express](https://www.adafruit.com/product/3727) (Supports Audio Playback)
* [JST-PH 2-pin SMT Right-Angle Connector](https://www.adafruit.com/product/1769)
* [Mini Metal Speaker w/ Wires 8ohm 0.5W](https://www.adafruit.com/product/1890)
* [I2S 3W Class D Amplifier Breakout](https://www.adafruit.com/product/3006)
* [Micro-Lipo Charger with MicroUSB](https://www.adafruit.com/product/190)
* [4 Lithium Ion Battery 3.7V 500mAh](https://www.adafruit.com/product/1578)
* 4x Medium Blue LED’s
* Multi-Color Hook-up Wire

This guide, along with the [documentation for the I2S board](https://learn.adafruit.com/circuitpython-essentials/circuitpython-audio-out), provides everything you need to know about the code.

Max Weight: 5oz (141.7g)

Max Size: Length: 7” (177.8mm) Width: 2.75” (69.85mm) Height: 3” (76.2mm)

Pinewood Block Reference Dimensions:

* 45mm Wide (69.85mm max)
* 32mm Tall (76.2mm max)
* 177.8mm total length (7”)
* 112.5mm between Axles (outer edge) 109.5mm between Axles (inner edge) 1.5mm Axle Slots
* 22.7mm to Axle 42.7mm to Axle

[ECTO-1 Model](https://www.thingiverse.com/thing:2980759) as scaled in Cura:

* X: 68.0016 mm (174.91%)
* Y: 176.9973 mm (173.46%)
* Z: 56.0442 mm (173.46%)

Decals:

* License Plates: 3mm x 9mm
* Logo Max: 20mm wide, 14mm high
