from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class TaskResolver:
    statusButtonGreen = (0, 255, 0)  # use R value
    statusButtonYellow = (255, 240, 1)  # use R value
    statusButtonRed = (255, 0, 0)  # use either G or B value

    def click(self, x, y):
        win32api.SetCursorPos((x, y))
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def clickAndHold(self, pos, duration):
        win32api.SetCursorPos(pos)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(duration)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def writeSlow(self, string):
        for i in string:
            keyboard.press_and_release(i)
            sleep(0.02)

    def imageToText(self, region):
        img = pyautogui.screenshot(region=region)
        img.save(r"screen/tmp.png")
        result = pytesseract.image_to_string(img)
        sleep(0.01)
        return result

    @classmethod
    def dragTo(cls, fromX, fromY, toX, toY):
        win32api.SetCursorPos((fromX, fromY))
        sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.1)
        pyautogui.moveTo(toX, toY, 0.2)
        sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    # simply click on kettle button
    def resolveKettle(self):
        mainPanelKettleLocation = (1240, 619)
        # color of kettle button on main panel
        kettleStatus = pyautogui.pixel(mainPanelKettleLocation[0], mainPanelKettleLocation[1])[0]

        if kettleStatus in [168, 161]:  # if its Yellow or red
            kettleButtonLocation = (1865, 191)
            TaskResolver.click(self, kettleButtonLocation[0], kettleButtonLocation[1])

    # relatively low priority task: expensive to check, better to wait
    def resolveLitButtonTask(self):
        litButton = (0, 211, 255)  # get R value

        buttonsPerRow = 19
        numberOfRows = 3
        rowYValues = [830, 860, 889]
        buttonOffset = 33
        for i in range(numberOfRows):
            currentX = 680
            for _ in range(buttonsPerRow):
                if pyautogui.pixel(currentX, rowYValues[i])[1] == litButton[1]:  # check G value
                    sleep(0.01)
                    TaskResolver.click(self, currentX, rowYValues[i])
                currentX += buttonOffset

    def resolveCenterButtonTask(self):
        rightButton = (605, 740)
        leftButton = (532, 740)
        upButton = (564, 720)
        downButton = (566, 760)

    def resolveColleaguesTask(self):
        faceColor = (0, 151, 32)
        facePosition1 = (424, 660)
        facePosition2 = (410, 628)
        facePosition3 = (421, 632)
        if (pyautogui.pixel(facePosition1[0], facePosition1[1])[1] == faceColor[1]) or \
                (pyautogui.pixel(facePosition2[0], facePosition2[1])[1] == faceColor[1]) or \
                (pyautogui.pixel(facePosition3[0], facePosition3[1])[1] == faceColor[1]):
            buttonPosition = (427, 755)
            TaskResolver.click(self, buttonPosition[0], buttonPosition[1])

    def resolveMagnetTask(self):
        pass

    def resolveCalculatorTask(self):
        pass

    def resolveCircleColorTask(self):
        pass

    def resolveMeterBalanceTask(self):
        region = (1407, 912, 107, 42)

        meter = self.imageToText(region)
        print(meter)

        pass

    def resolveNuclearWasteTask(self):
        pass

    def resolveNumberSliderTask(self):
        pass

    def resolvePluggingTask(self):
        pass

    def resolveReduceMeterTask(self):
        meterBarColor = (20, 44, 29)
        meterBarLocation = (331, 857)
        if pyautogui.pixel(meterBarLocation[0], meterBarLocation[1])[0] == meterBarColor[0]:
            buttonLocation = (300, 881)
            TaskResolver.click(self, buttonLocation[0], buttonLocation[1])

    def resolveShapeTask(self):
        pass

    def resolveTypingTask(self):
        region = (1310, 900, 300, 40)
        stringToType = self.imageToText(region)
        stringToType = stringToType.lower()
        self.writeSlow(stringToType)

    def resolveLeftRightTask(self):
        meterColor = (20, 44, 29)
        rightColumnPos = (76, 855)
        leftColumnPos = (28, 855)
        if pyautogui.pixel(rightColumnPos[0], rightColumnPos[1])[0] == meterColor[0]:
            keyboard.send("right")
        if pyautogui.pixel(leftColumnPos[0], leftColumnPos[1])[0] == meterColor[0]:
            keyboard.send("left")

    def resolveIQTask(self):
        iqLeftBlockLocation = (401, 623)
        iqRightBlockLocation = (454, 623)
        xShapeLocation = (458, 703)
        oShapeLocation = (400, 706)
        squareLocation = (400, 752)
        triangleLocation = (456, 755)

        squareColor = (3, 7, 120)
        xColor = (0, 125, 103)
        oColor = (179, 125, 44)
        triangleColor = (127, 67, 125)

        if pyautogui.pixel(iqLeftBlockLocation[0], iqLeftBlockLocation[1])[2] == squareColor[2]:
            TaskResolver.dragTo(iqLeftBlockLocation[0], iqLeftBlockLocation[1], squareLocation[0],
                                squareLocation[1])

        if pyautogui.pixel(iqLeftBlockLocation[0], iqLeftBlockLocation[1])[2] == xColor[2]:
            TaskResolver.dragTo(iqLeftBlockLocation[0], iqLeftBlockLocation[1], xShapeLocation[0],
                                xShapeLocation[1])

        if pyautogui.pixel(iqLeftBlockLocation[0], iqLeftBlockLocation[1])[2] == oColor[2]:
            TaskResolver.dragTo(iqLeftBlockLocation[0], iqLeftBlockLocation[1], oShapeLocation[0],
                                oShapeLocation[1])

        if pyautogui.pixel(iqLeftBlockLocation[0], iqLeftBlockLocation[1])[2] == triangleColor[2]:
            TaskResolver.dragTo(iqLeftBlockLocation[0], iqLeftBlockLocation[1], triangleLocation[0],
                                triangleLocation[1])

        if pyautogui.pixel(iqRightBlockLocation[0], iqRightBlockLocation[1])[2] == squareColor[2]:
            TaskResolver.dragTo(iqRightBlockLocation[0], iqRightBlockLocation[1], squareLocation[0],
                                squareLocation[1])

        if pyautogui.pixel(iqRightBlockLocation[0], iqRightBlockLocation[1])[2] == xColor[2]:
            TaskResolver.dragTo(iqRightBlockLocation[0], iqRightBlockLocation[1], xShapeLocation[0],
                                xShapeLocation[1])

        if pyautogui.pixel(iqRightBlockLocation[0], iqRightBlockLocation[1])[2] == oColor[2]:
            TaskResolver.dragTo(iqRightBlockLocation[0], iqRightBlockLocation[1], oShapeLocation[0],
                                oShapeLocation[1])

        if pyautogui.pixel(iqRightBlockLocation[0], iqRightBlockLocation[1])[2] == triangleColor[2]:
            TaskResolver.dragTo(iqRightBlockLocation[0], iqRightBlockLocation[1], triangleLocation[0],
                                triangleLocation[1])

    def resolveBalanceNumberTask(self):
        pass

    def resolveBugFinderTask(self):
        pass

    def resolveFrequencyTask(self):
        pass

    def resolveFlippingSwitchesTask(self):
        topRowIndicatorColor = (0, 41, 80)  # this color means the switch is off
        topRowIndicatorYPos = 584
        topRowIndicatorXPos = [1325, 1352, 1378, 1403, 1432, 1457, 1486, 1511, 1540, 1565]
        # bottomRowIndicatorPositions = [(1333,690), (1378,690), (1422,690)] #around 45 offset

        bottomRowIndicatorColor = (0, 25, 56)  # this color means the switch is off
        bottomRowIndicatorPos = [1333, 690]
        bottomRowIndicatorOffset = 45

        numberOfBottomSwitches = 6

        # for _ in range(numberOfTopSwitches):
        #     print(pyautogui.pixel(topRowIndicatorPos[0], topRowIndicatorPos[1]))
        #     if pyautogui.pixel(topRowIndicatorPos[0], topRowIndicatorPos[1])[1] == topRowIndicatorColor[1]:
        #         sleep(0.01)
        #         self.click(topRowIndicatorPos[0], topRowIndicatorPos[1])
        #     topRowIndicatorPos[0] += topRowIndicatorOffset
        # print('----------')

        for topRowIndicatorXPo in topRowIndicatorXPos:
            if (
                    pyautogui.pixel(topRowIndicatorXPo, topRowIndicatorYPos)[1]
                    == topRowIndicatorColor[1]
            ):
                sleep(0.01)
                self.click(topRowIndicatorXPo, topRowIndicatorYPos)

        for _ in range(numberOfBottomSwitches):
            if pyautogui.pixel(bottomRowIndicatorPos[0], bottomRowIndicatorPos[1])[1] == bottomRowIndicatorColor[1]:
                sleep(0.01)
                self.click(bottomRowIndicatorPos[0], bottomRowIndicatorPos[1])
            bottomRowIndicatorPos[0] += bottomRowIndicatorOffset

    def resolveRedGreenLightTask(self):
        middleRightTopStatus = (1603, 565)  # statusLocation
        if pyautogui.pixel(middleRightTopStatus[0], middleRightTopStatus[1])[0] == self.statusButtonYellow[0]:
            lightPosition = [(1346, 603), (1414, 603), (1476, 603), (1543, 603)]
            switchButtonPosition = [(1346, 657), (1414, 657), (1476, 657), (1543, 657)]

            for i in range(len(lightPosition)):
                self.click(lightPosition[i][0], lightPosition[i][1])  # open lid
                sleep(0.01)
                lightColor = pyautogui.pixel(lightPosition[i][0], lightPosition[i][1])[0]
                print(lightColor)
                if 240 < lightColor < 256:  # check color, if red then press switch
                    self.click(switchButtonPosition[i][0], switchButtonPosition[i][1])
                    sleep(0.01)

    def resolveRemoveParticleTask(self):
        topLeftStatus = (91, 346)
        if pyautogui.pixel(topLeftStatus[0], topLeftStatus[1])[0] == self.statusButtonYellow[0]:
            buttonLocation = (192, 384)
            sliderLocation = (121, 355)
            sliderEndLocation = (271, 351)
            self.clickAndHold(buttonLocation, 1.5)
            self.dragTo(sliderLocation[0], sliderLocation[1], sliderEndLocation[0], sliderEndLocation[1])

    def resolveSwitchColorTask(self):
        statusCyan = (0, 210, 181)
        statusPurple = (231, 122, 226)
        statusYellow = (255, 199, 0)
        statusBlue = (27, 134, 218)

        buttonBlue = (3, 71, 120)
        buttonPurple = (127, 67, 125)
        buttonCyan = (0, 125, 103)
        buttonYellow = (179, 125, 44)

        colorClickMap = {
            (buttonBlue, statusCyan): 2,  # blue -> cyan
            (buttonBlue, statusPurple): 3,  # blue -> purple
            (buttonBlue, statusYellow): 1,  # blue -> yellow

            (buttonPurple, statusBlue): 1,  # purple -> blue
            (buttonPurple, statusCyan): 3,  # purple -> cyan
            (buttonPurple, statusYellow): 2,  # purple -> yellow

            (buttonCyan, statusPurple): 1,  # cyan -> purple
            (buttonCyan, statusBlue): 2,  # cyan -> blue
            (buttonCyan, statusYellow): 3,  # cyan -> yellow

            (buttonYellow, statusCyan): 1,  # yellow -> cyan
            (buttonYellow, statusPurple): 2,  # yellow -> purple
            (buttonYellow, statusBlue): 3  # yellow -> blue

        }
        buttonPositions = [(1844, 532), (1844, 578), (1844, 613), (1844, 655), (1844, 707), (1844, 746)]
        statusPositions = [(1887, 536), (1887, 579), (1887, 622), (1887, 663), (1887, 705), (1887, 747)]

        for i in range(len(statusPositions)):
            currentButtonColor = pyautogui.pixel(buttonPositions[i][0], buttonPositions[i][1])
            currentStatusColor = pyautogui.pixel(statusPositions[i][0], statusPositions[i][1])

            if (currentButtonColor, currentStatusColor) in colorClickMap:
                clickTimes = colorClickMap[(currentButtonColor, currentStatusColor)]
                for _ in range(clickTimes):
                    self.click(buttonPositions[i][0], buttonPositions[i][1])

    def resolveSymbolRemovalTask(self):
        isRemainingSymbol = True
        region = (1819, 504, 90, 180)

        circleButton = (1886, 751)
        squareButton = (1885, 709)
        triangleButton = (1842, 752)
        xButton = (1845, 711)
        while isRemainingSymbol:
            isRemainingSymbol = False
            if pyautogui.locateOnScreen('symbols/circle.png', region=region, grayscale=True,
                                        confidence=0.7) is not None:
                self.click(circleButton[0], circleButton[1])
                isRemainingSymbol = True
            # if pyautogui.locateOnScreen('symbols/square.png', region=region, grayscale=True, confidence=0.7) != None:
            #     self.click(squareButton[0], squareButton[1])
            #     isRemainingSymbol = True
            if pyautogui.locateOnScreen('symbols/triangle.png', region=region, grayscale=True,
                                        confidence=0.7) is not None:
                self.click(triangleButton[0], triangleButton[1])
                isRemainingSymbol = True
            if pyautogui.locateOnScreen('symbols/x.png', region=region, grayscale=True, confidence=0.7) is not None:
                self.click(xButton[0], xButton[1])
                isRemainingSymbol = True

    def resolveEquationTask(self):
        region = (1647, 529, 150, 26)
        equation = self.imageToText(region)
        print(equation)
        variable = equation[len(equation) - 1]
        number = equation[:-1]
        answer = 0
        if variable == 'C':
            answer = int(number) * 2
        elif variable == 'L':
            answer = int(number) - 1
        elif variable == 'R':
            answer = (int(number) * 2) + 1
        keyboard.press('ctrl')
        print(answer)
        self.writeSlow(str(answer))
        sleep(0.01)
        keyboard.release('ctrl')

