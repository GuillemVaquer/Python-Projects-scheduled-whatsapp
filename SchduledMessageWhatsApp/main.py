import pywhatkit
import datetime



def main():
    path = get_path()
    if path == "c":
        receiver = input("Enter WhatsApp Number of Sender (without Country Code) : ")
        msg, sending_time = get_message()
        pywhatkit.sendwhatmsg(f"+91{receiver}", f"{msg}", sending_time.hour, sending_time.minute)
    else:
        receiver = input("Enter the exact name of the Whatsapp group : ")
        msg, sending_time = get_message()
        pywhatkit.sendwhatmsg_to_group(f"{receiver}", f"{msg}", sending_time.hour, sending_time.minute)
    

def get_path():
    while True:
        try:
            path = input("Are you sending a message to a contact or to a group? (c/g): ")
            if path != ("c" or "g"):
                raise ValueError
        except ValueError:
            print("Please write either 'c' or 'g'.")
        return path

def get_message():
    msg = input("Enter Your Message : ")
    sending_time = input("Enter Time in (HH:MM) 24-hr format : ")
    sending_time = datetime.time.fromisoformat(sending_time)
    return msg, sending_time


if __name__=="__main__":
    main()
