import cv2
import aproximater
import os
import time
import threading
import moviepy.editor
import playsound


vid = "/home/almor/Documents/Python Course with Notes/CLanime/testvod.mp4"
video = cv2.VideoCapture(vid)
fps = video.get(cv2.CAP_PROP_FPS)
framecnt = video.get(cv2.CAP_PROP_FRAME_COUNT)
runtime =  framecnt
def getframe(n):
    video.set(cv2.CAP_PROP_POS_FRAMES, n)
    ret, frame = video.read()
    name = f"/home/almor/Documents/Python Course with Notes/CLanime/.vidcache/.{n}.png"
    cv2.imwrite(name, frame)
def goreshti():
    playsound.playsound('audio.mp3')
slept = 1/fps


input_file = moviepy.editor.VideoFileClip('/home/almor/Documents/Python Course with Notes/CLanime/testvod.mp4')
audio = input_file.audio
audio.write_audiofile("audio.mp3")


thread1 = threading.Thread(target=goreshti)

thread1.start()
c= 1
while (c < framecnt):
    tnow = float(time.perf_counter())

    term = os.get_terminal_size()
    termH = term[1]
    termW = term[0]

    getframe(c)

    imgnm = f"/home/almor/Documents/Python Course with Notes/CLanime/.vidcache/.{c}.png"
    if c>1:
        imgnamaewa = f"/home/almor/Documents/Python Course with Notes/CLanime/.vidcache/.{c-1}.png"
        os.remove(imgnamaewa)

    image = cv2.imread(imgnm)
    h, w = image.shape[:2]


    cnt = 0

    if(h>termH):
        r = aproximater.aproximat(h/termH)
    else:
        r = aproximater.aproximat(termH/h)

    actr = aproximater.aproximat((r+1)/2)
    for i in range(0,w,actr):
        cnt += 1

    dif = aproximater.aproximat((termW-cnt)/2)
    apac = " "*dif
    
    p = ""

    
    for i in range(0,h,r+1):

        
        p+=apac
        for j in range(0,w,r+1):

            (B, G, R) = image[i, j]
            p += (f"\033[38;2;{R};{G};{B}m██\033[0m")

        p+= "\n"

    # print("\033c")
    os.system('clear')
    print(p)
    c+=1
    
    tlol = float(time.perf_counter())
    tfinal = tlol-tnow

    if slept > tfinal:
        time.sleep(slept-tfinal)
    else:
        time.sleep(tfinal-slept)

os.remove("audio.mp3")
os.remove(imgnm)
