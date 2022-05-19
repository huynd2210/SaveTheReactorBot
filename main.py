from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import pytesseract
import cv2

from TaskResolver import TaskResolver

mainPanelGreen = (0, 150, 49)
mainPanelYellow = (168, 148, 0)
mainPanelRed = (161, 0, 0)

# Status Location
rightBottomRightStatus = (1767, 800)
rightBottomLeftStatus = (1651, 933)
rightTopLeftStatus = (1650, 488)
rightTopRightStatus = (1835, 493)

middleBottomStatus = (649, 836)
middleLeftStatus = (531, 570)
middleRightMiddleStatus = (1602, 738)
middleRightBottomStatus = (1324, 886)

LeftRightRightStatus = (384, 570)
LeftRightStatus = (277, 572)
LeftLeftLeftStatus = (27, 571)
LeftLeftStatus = (133, 571)


def takeScreenshot(region):
    iml = pyautogui.screenshot(region=region)
    iml.save(r"C:\Users\This PC\Desktop\tmp\sample.png")


def isTaskPresent(task):
    return (
            pyautogui.locateOnScreen(
                task, region=(640, 640, 640, 160), grayscale=True, confidence=0.8
            )
            is not None
    )


def getTask():
    allTasks = [
        'litButtonTask.png',
        'calculatorTask.png',
        'colleaguesTask.png',
        'magnetTask.png',
        'redGreenLightTask.png',
        'typingTask.png',
        'numberSliderTask.png',
        'nuclearWasteTask.png',
        'pluggingTask.png',
        'shapeTask.png',
        'reduceMeterTask.png',
        'meterBalanceTask.png',
        'circleColorTask.png'
    ]
    return [task for task in allTasks if isTaskPresent(task)]


def play():
    taskResolver = TaskResolver()

    taskResolver.resolveKettle()
    taskResolver.resolveLeftRightTask()
    # taskResolver.resolveLitButtonTask()
    taskResolver.resolveIQTask()
    # taskResolver.resolveReduceMeterTask()
    # taskResolver.resolveColleaguesTask()
    # taskResolver.resolveFlippingSwitchesTask()
    # taskResolver.resolveTypingTask()
    # taskResolver.resolveRedGreenLightTask()
    taskResolver.resolveRemoveParticleTask()
    # taskResolver.resolveSymbolRemovalTask()
    # taskResolver.resolveSwitchColorTask()
    # taskResolver.resolveEquationTask()
    # taskResolver.resolveMeterBalanceTask()

def runBot():
    print("Running program....")
    isStart = False
    while True:
        # press m to start
        if isStart or keyboard.is_pressed('m'):
            isStart = True
            play()
        # press q to quit
        if keyboard.is_pressed('q'):
            break

def runScreenshot(region):
    print("press q to take screenshot")
    while True:
        if keyboard.is_pressed('q'):
            takeScreenshot(region)
            print("Screenshot taken")
            break

if __name__ == '__main__':
    # runScreenshot((1647, 529, 150, 26))
    runBot()


    # start = time.time()
    # pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    # img = cv2.imread("C:\\Users\\This PC\\Desktop\\tmp\\tmp.png")
    # res = pytesseract.image_to_string(img)
    # end = time.time()
    # print(end - start)
    #
    # print(res)


    # while True:
    #     region = (0, 0, 1000, 500)
    #     if (
    #         pyautogui.locateOnScreen(
    #             'symbols/x.png',
    #             region=region,
    #             grayscale=True,
    #             confidence=0.7,
    #         )
    #         is None
    #     ):
    #         print("not there")
    #
    #     else:
    #         print("found it")
    #         break

    # t = TaskResolver
    # t.dragTo(600, 330, 1120, 602)

