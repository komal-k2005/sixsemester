import time
import winsound

def set_alarm(alarm_time, sound_file_path):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            play_sound(sound_file_path)
            break
        time.sleep(1)

def play_sound(sound_file_path):
    winsound.PlaySound(sound_file_path, winsound.SND_FILENAME)

# Example usage:
alarm_time = "08:00:00"  # Set your desired alarm time
sound_file_path = "path/to/your/alarm_sound.wav"  # Provide the path to your sound file
set_alarm(alarm_time, sound_file_path)