

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *



#PyToggle(animation_curve=QEasingCurve.OutBounce)
class PyToggle(QCheckBox):
    def __init__(
            self,
            width = 70,
            button_height = 28,
            bg_color = "#777",
            circle_color = "#000",
            active_color = "#00BCff",

            #Change animations here
            animation_curve = QEasingCurve.OutBounce 
            # change the Bouncing of Round Ball
    ):
        QCheckBox.__init__(self)

        
        #set Detail Paramenter
        self.setFixedSize(width, button_height)
        self.setCursor(Qt.PointingHandCursor)

        #Color
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        # Create Animation
        self._circle_position = 3
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(animation_curve)

        #Duration of Button Transition
        self.animation.setDuration(800)


        # Connect state Changed
        self.stateChanged.connect(self.start_transition)

        # Uncomment to use images on toggle button 
        # self.day = QPixmap(":/icons/images/icons/sun.png")
        # self.night = QPixmap(":/icons/images/icons/moon.png")

    #Create new Set and Get value
    @Property(float)
    def cirle_postion(self): #get
        return self._circle_position
    @cirle_postion.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()


    def start_transition(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - 26)
        else:
            self.animation.setEndValue(3)

        #Start animation
        self.animation.start()

    


    #Set Nes Hit Area
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
       rect = QRect(0, 0, self.width(), self.height())
       painter = QPainter(self)
       painter.setRenderHint(QPainter.Antialiasing)
       if not self.isChecked():
           
           #SET Background for night mode here
           painter.setBrush(QImage("night_sky.jpg"))
           painter.setPen(Qt.NoPen)
           painter.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)
           painter.setBrush(QColor("#F4F6F0"))
           painter.drawEllipse(self._circle_position, 3, 22, 22)
       else:

           #SET Background for Day mode here
           painter.setBrush(QImage("day_sky.jpg"))
           painter.setPen(Qt.NoPen)
           painter.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)
           painter.setBrush(QColor("#FDB813"))
           painter.drawEllipse(self._circle_position, 3, 22, 22)







