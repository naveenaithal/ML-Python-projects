# import sys
# sys.path.append('C:\PathTo\project\package1')
# import main3

import tkinter as tk
import threading
import socket
from vidstream import *

local_ip_adress=socket.gethostbyname(socket.gethostname())

server=StreamingServer(local_ip_adress,7777)
reciver=AudioReceiver(local_ip_adress,6666)

def start_listing():
    t1=threading.Thread(target=server.start_server)
    t2=threading.Thread(target=reciver.start_server)
    t1.start()
    t2.start()
def start_camara_stream():
    camara_client=CameraClient(text_target_ip.get(1.0,'end-1c'),9999)
    t3=threading.Thread(target=camara_client.start_stream)
    t3.start()

def start_screen_sharing():
    screen_client=ScreenShareClient(text_target_ip.get(1.0,'end-1c'),9999)
    t4=threading.Thread(target=screen_client.start_stream)
    t4.start()

def start_audio_stream():
    audio_sender=AudioSender(text_target_ip.get(1.0,'end-1c'),8888)
    t5=threading.Thread(target=audio_sender.start_stream)
    t5.start()


window=tk.Tk()
window.title("Video streaming")
window.geometry('300x200')

label_target_ip=tk.Label(window,text='Target ip',)
label_target_ip.pack()

text_target_ip=tk.Text(window,height=1)
text_target_ip.pack()

btn_listing=tk.Button(window,text="Start Listing",width=50,command=start_listing)
btn_listing.pack(anchor=tk.CENTER,expand=True)

btn_camara=tk.Button(window,text="Start camara stream",width=50,command=start_camara_stream)
btn_camara.pack(anchor=tk.CENTER,expand=True)

btn_screen=tk.Button(window,text="Start Screen sharing",width=50,command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER,expand=True)

btn_audio=tk.Button(window,text="Start Audio straming",width=50,command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER,expand=True)

window.mainloop()


