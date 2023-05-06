from PyQt5 import QtWidgets, QtGui, QtCore, uic

from asrInterface import Ui_MainWindow
import sys
import win32api
import speech_recognition as sr

class SpeechRecognitionThread(QtCore.QThread):
    command_received = QtCore.pyqtSignal(str)

    def __init__(self):
        super(SpeechRecognitionThread, self).__init__()
        self.recognizer = sr.Recognizer()
        # 设置能量阈值为300
        self.recognizer.energy_threshold = 300

        # 设置动态能量阈值的平均值为50
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.dynamic_energy_adjustment_ratio = 1.5

        self.microphone = sr.Microphone()

    def run(self):
        while True:
            command = self.recognize_speech_from_mic()
            if command["transcription"]:
                self.command_received.emit(command["transcription"])    #发送信号
    def recognize_speech_from_mic(self):
        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(self.recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(self.microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")

        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            response["transcription"] = self.recognizer.recognize_google(audio)

           # response["transcription"] = self.recognizer.recognize_sphinx(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response





class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Add any other pushButton connections here
        self.recognition_thread = SpeechRecognitionThread()
        self.recognition_thread.command_received.connect(self.on_command_received)  #这个子线程的信号连接到on_command_received函数
        self.recognition_thread.finished.connect(self.recognition_thread.deleteLater)


    def show(self):
        super(myWindow, self).show()
        self.recognition_thread.start()

    def on_command_received(self, command):
        if command.lower() == "play music":
            self.playMusic()
            self.ui.textBrowser.append(">> I heared you say "+command)
        elif command.lower() == "open notepad":
            self.openTextFile()
            self.ui.textBrowser.append(">> I heared you say "+command)
        else:
            self.ui.textBrowser.append(">> I heared you say "+command+". I'm sorry I don't understand your instructions.")




    def playMusic(self):
        win32api.ShellExecute(0, 'open', 'C:\\Users\\dell\\Desktop\\text-music.mp3', '','',1)

    def openTextFile(self):
            win32api.ShellExecute(0, 'open', 'notepad.exe', '','',1)

app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())

