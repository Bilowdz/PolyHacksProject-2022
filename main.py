from datetime import datetime
from playsound import playsound


# hello mme poutri, I hope you are doing well. Today, we will code an alarm clock that will make you want to kill
# yourself faster than you can turn it off.

def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 23:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"


while True:
    alarm_time = input("Enter time in 'HH:MM:SS' format: ")

    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]

while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec <= current_sec:
                print("Wake Up!")
                # playsound('/laugh.wav')
                break
