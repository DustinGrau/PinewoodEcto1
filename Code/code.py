import audioio
import audiobusio
import board
import digitalio
import pulseio
import time

# Configure a switch on pin D2
button = digitalio.DigitalInOut(board.D2)
button.switch_to_input(pull=digitalio.Pull.UP)

# Configure the blue LED's using PWM
blue1 = pulseio.PWMOut(board.D10, frequency=5000, duty_cycle=0)
blue2 = pulseio.PWMOut(board.D11, frequency=5000, duty_cycle=0)

# Configure our sound file to be played.
wave_file = open("ecto1_loop.wav", "rb")
wave = audioio.WaveFile(wave_file)

# ItsyBitsy M0 Express - I2S Output to DAC/Amp
audio = audiobusio.I2SOut(board.D1, board.D0, board.D9)

def flash_blue(x):
    # PWM LED up and down
    step = int(2 * 65535 / 100)
    if x < 50:
        # Count up until 50%
        blue1.duty_cycle = int(x * step)
        blue2.duty_cycle = 65535 - int(x * step)
    else:
        # Count down until 100%
        blue1.duty_cycle = 65535 - int((x - 50) * step)
        blue2.duty_cycle = int((x - 50) * step)

while True:
    print("Sound/Light Start")
    audio.play(wave)

    while audio.playing:
        for i in range(100):
            flash_blue(i)
            time.sleep(0.004)

    print("Waiting for button press...")
    while button.value:
        blue1.duty_cycle = 0
        blue2.duty_cycle = 0