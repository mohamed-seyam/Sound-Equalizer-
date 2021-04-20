# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\EQ.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.widgets.MatplotlibWidget import MatplotlibWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 952)
        MainWindow.setMinimumSize(QtCore.QSize(1022, 952))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\assets/MainIcon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 1, 1, 1)
        self.spectrogram_before = MatplotlibWidget()
        self.spectrogram_before.setMinimumSize(QtCore.QSize(470, 227))
        self.spectrogram_before.setMaximumSize(QtCore.QSize(946, 228))
        self.spectrogram_before.setObjectName("spectrogram_before")
        self.gridLayout.addWidget(self.spectrogram_before, 3, 0, 1, 1)
        self.spectrogram_after = MatplotlibWidget()
        self.spectrogram_after.setMinimumSize(QtCore.QSize(470, 227))
        self.spectrogram_after.setMaximumSize(QtCore.QSize(946, 228))
        self.spectrogram_after.setObjectName("spectrogram_after")
        self.gridLayout.addWidget(self.spectrogram_after, 3, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.controlers_before = QtWidgets.QHBoxLayout()
        self.controlers_before.setObjectName("controlers_before")
        self.jump_back_btn_before = QtWidgets.QPushButton(self.centralwidget)
        self.jump_back_btn_before.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\assets/fast-backward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jump_back_btn_before.setIcon(icon)
        self.jump_back_btn_before.setObjectName("jump_back_btn_before")
        self.controlers_before.addWidget(self.jump_back_btn_before)
        self.play_btn_before = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn_before.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\assets/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_btn_before.setIcon(icon1)
        self.play_btn_before.setObjectName("play_btn_before")
        self.controlers_before.addWidget(self.play_btn_before)
        self.pause_btn_before = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn_before.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\assets/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_btn_before.setIcon(icon2)
        self.pause_btn_before.setObjectName("pause_btn_before")
        self.controlers_before.addWidget(self.pause_btn_before)
        self.stop_btn_before = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn_before.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\assets/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_btn_before.setIcon(icon3)
        self.stop_btn_before.setObjectName("stop_btn_before")
        self.controlers_before.addWidget(self.stop_btn_before)
        self.jump_forward_btn_before = QtWidgets.QPushButton(self.centralwidget)
        self.jump_forward_btn_before.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\assets/fast-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.jump_forward_btn_before.setIcon(icon4)
        self.jump_forward_btn_before.setObjectName("jump_forward_btn_before")
        self.controlers_before.addWidget(self.jump_forward_btn_before)
        self.zoom_in_btn_before = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in_btn_before.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\assets/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in_btn_before.setIcon(icon5)
        self.zoom_in_btn_before.setObjectName("zoom_in_btn_before")
        self.controlers_before.addWidget(self.zoom_in_btn_before)
        self.zoom_out_btn_before = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out_btn_before.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\assets/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out_btn_before.setIcon(icon6)
        self.zoom_out_btn_before.setObjectName("zoom_out_btn_before")
        self.controlers_before.addWidget(self.zoom_out_btn_before)
        self.verticalLayout_4.addLayout(self.controlers_before)
        self.gridLayout.addLayout(self.verticalLayout_4, 5, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)
        self.time_before = QtWidgets.QHBoxLayout()
        self.time_before.setObjectName("time_before")
        self.current_time_before = QtWidgets.QLabel(self.centralwidget)
        self.current_time_before.setMinimumSize(QtCore.QSize(80, 0))
        self.current_time_before.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.current_time_before.setObjectName("current_time_before")
        self.time_before.addWidget(self.current_time_before)
        self.time_seeker_before = QtWidgets.QSlider(self.centralwidget)
        self.time_seeker_before.setOrientation(QtCore.Qt.Horizontal)
        self.time_seeker_before.setObjectName("time_seeker_before")
        self.time_before.addWidget(self.time_seeker_before)
        self.total_time_before = QtWidgets.QLabel(self.centralwidget)
        self.total_time_before.setMinimumSize(QtCore.QSize(80, 0))
        self.total_time_before.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.total_time_before.setObjectName("total_time_before")
        self.time_before.addWidget(self.total_time_before)
        self.playback_speed_before = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.playback_speed_before.setFont(font)
        self.playback_speed_before.setObjectName("playback_speed_before")
        self.playback_speed_before.addItem("")
        self.playback_speed_before.addItem("")
        self.playback_speed_before.addItem("")
        self.playback_speed_before.addItem("")
        self.playback_speed_before.addItem("")
        self.playback_speed_before.addItem("")
        self.time_before.addWidget(self.playback_speed_before)
        self.gridLayout.addLayout(self.time_before, 4, 0, 1, 1)
        self.time_after = QtWidgets.QHBoxLayout()
        self.time_after.setObjectName("time_after")
        self.current_time_after = QtWidgets.QLabel(self.centralwidget)
        self.current_time_after.setMinimumSize(QtCore.QSize(80, 0))
        self.current_time_after.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.current_time_after.setObjectName("current_time_after")
        self.time_after.addWidget(self.current_time_after)
        self.time_seeker_after = QtWidgets.QSlider(self.centralwidget)
        self.time_seeker_after.setOrientation(QtCore.Qt.Horizontal)
        self.time_seeker_after.setObjectName("time_seeker_after")
        self.time_after.addWidget(self.time_seeker_after)
        self.total_time_after = QtWidgets.QLabel(self.centralwidget)
        self.total_time_after.setMinimumSize(QtCore.QSize(80, 0))
        self.total_time_after.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.total_time_after.setObjectName("total_time_after")
        self.time_after.addWidget(self.total_time_after)
        self.playback_speed_after = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.playback_speed_after.setFont(font)
        self.playback_speed_after.setObjectName("playback_speed_after")
        self.playback_speed_after.addItem("")
        self.playback_speed_after.addItem("")
        self.playback_speed_after.addItem("")
        self.playback_speed_after.addItem("")
        self.playback_speed_after.addItem("")
        self.playback_speed_after.addItem("")
        self.time_after.addWidget(self.playback_speed_after)
        self.gridLayout.addLayout(self.time_after, 4, 1, 1, 1)
        self.graph_after = PlotWidget(self.centralwidget)
        self.graph_after.setMinimumSize(QtCore.QSize(470, 227))
        self.graph_after.setObjectName("graph_after")
        self.gridLayout.addWidget(self.graph_after, 1, 1, 1, 1)
        self.graph_before = PlotWidget(self.centralwidget)
        self.graph_before.setMinimumSize(QtCore.QSize(470, 227))
        self.graph_before.setObjectName("graph_before")
        self.gridLayout.addWidget(self.graph_before, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.controlers_after = QtWidgets.QHBoxLayout()
        self.controlers_after.setObjectName("controlers_after")
        self.jump_back_btn_after = QtWidgets.QPushButton(self.centralwidget)
        self.jump_back_btn_after.setText("")
        self.jump_back_btn_after.setIcon(icon)
        self.jump_back_btn_after.setObjectName("jump_back_btn_after")
        self.controlers_after.addWidget(self.jump_back_btn_after)
        self.play_btn_after = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn_after.setText("")
        self.play_btn_after.setIcon(icon1)
        self.play_btn_after.setObjectName("play_btn_after")
        self.controlers_after.addWidget(self.play_btn_after)
        self.pause_btn_after = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn_after.setText("")
        self.pause_btn_after.setIcon(icon2)
        self.pause_btn_after.setObjectName("pause_btn_after")
        self.controlers_after.addWidget(self.pause_btn_after)
        self.stop_btn_after = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn_after.setText("")
        self.stop_btn_after.setIcon(icon3)
        self.stop_btn_after.setObjectName("stop_btn_after")
        self.controlers_after.addWidget(self.stop_btn_after)
        self.jump_forward_btn_after = QtWidgets.QPushButton(self.centralwidget)
        self.jump_forward_btn_after.setText("")
        self.jump_forward_btn_after.setIcon(icon4)
        self.jump_forward_btn_after.setObjectName("jump_forward_btn_after")
        self.controlers_after.addWidget(self.jump_forward_btn_after)
        self.zoom_in_btn_after = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in_btn_after.setText("")
        self.zoom_in_btn_after.setIcon(icon5)
        self.zoom_in_btn_after.setObjectName("zoom_in_btn_after")
        self.controlers_after.addWidget(self.zoom_in_btn_after)
        self.zoom_out_btn_after = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out_btn_after.setText("")
        self.zoom_out_btn_after.setIcon(icon6)
        self.zoom_out_btn_after.setObjectName("zoom_out_btn_after")
        self.controlers_after.addWidget(self.zoom_out_btn_after)
        self.verticalLayout_3.addLayout(self.controlers_after)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.max_freq_content_label = QtWidgets.QLabel(self.centralwidget)
        self.max_freq_content_label.setObjectName("max_freq_content_label")
        self.verticalLayout_14.addWidget(self.max_freq_content_label)
        self.max_freq_content = QtWidgets.QSlider(self.centralwidget)
        self.max_freq_content.setMaximum(11)
        self.max_freq_content.setProperty("value", 11)
        self.max_freq_content.setOrientation(QtCore.Qt.Vertical)
        self.max_freq_content.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.max_freq_content.setObjectName("max_freq_content")
        self.verticalLayout_14.addWidget(self.max_freq_content)
        self.max_freq_content_lab = QtWidgets.QLabel(self.centralwidget)
        self.max_freq_content_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.max_freq_content_lab.setObjectName("max_freq_content_lab")
        self.verticalLayout_14.addWidget(self.max_freq_content_lab)
        self.gridLayout.addLayout(self.verticalLayout_14, 1, 2, 1, 1)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.min_freq_content_label = QtWidgets.QLabel(self.centralwidget)
        self.min_freq_content_label.setObjectName("min_freq_content_label")
        self.verticalLayout_15.addWidget(self.min_freq_content_label)
        self.min_freq_content = QtWidgets.QSlider(self.centralwidget)
        self.min_freq_content.setMaximum(11)
        self.min_freq_content.setOrientation(QtCore.Qt.Vertical)
        self.min_freq_content.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.min_freq_content.setObjectName("min_freq_content")
        self.verticalLayout_15.addWidget(self.min_freq_content)
        self.min_freq_content_lab = QtWidgets.QLabel(self.centralwidget)
        self.min_freq_content_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.min_freq_content_lab.setObjectName("min_freq_content_lab")
        self.verticalLayout_15.addWidget(self.min_freq_content_lab)
        self.gridLayout.addLayout(self.verticalLayout_15, 3, 2, 1, 1)
        self.verticalLayout_16.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.band_1 = QtWidgets.QSlider(self.centralwidget)
        self.band_1.setMaximum(8)
        self.band_1.setPageStep(1)
        self.band_1.setProperty("value", 4)
        self.band_1.setOrientation(QtCore.Qt.Vertical)
        self.band_1.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.band_1.setObjectName("band_1")
        self.verticalLayout.addWidget(self.band_1)
        self.band_1_label = QtWidgets.QLabel(self.centralwidget)
        self.band_1_label.setObjectName("band_1_label")
        self.verticalLayout.addWidget(self.band_1_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.band_2 = QtWidgets.QSlider(self.centralwidget)
        self.band_2.setMaximum(8)
        self.band_2.setPageStep(1)
        self.band_2.setProperty("value", 4)
        self.band_2.setOrientation(QtCore.Qt.Vertical)
        self.band_2.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.band_2.setObjectName("band_2")
        self.verticalLayout_2.addWidget(self.band_2)
        self.band_2_label = QtWidgets.QLabel(self.centralwidget)
        self.band_2_label.setObjectName("band_2_label")
        self.verticalLayout_2.addWidget(self.band_2_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.band_3 = QtWidgets.QSlider(self.centralwidget)
        self.band_3.setMaximum(8)
        self.band_3.setPageStep(1)
        self.band_3.setProperty("value", 4)
        self.band_3.setOrientation(QtCore.Qt.Vertical)
        self.band_3.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.band_3.setObjectName("band_3")
        self.verticalLayout_5.addWidget(self.band_3)
        self.band_3_label = QtWidgets.QLabel(self.centralwidget)
        self.band_3_label.setObjectName("band_3_label")
        self.verticalLayout_5.addWidget(self.band_3_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.band_4 = QtWidgets.QSlider(self.centralwidget)
        self.band_4.setAutoFillBackground(False)
        self.band_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.band_4.setMaximum(8)
        self.band_4.setPageStep(1)
        self.band_4.setProperty("value", 4)
        self.band_4.setOrientation(QtCore.Qt.Vertical)
        self.band_4.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.band_4.setObjectName("band_4")
        self.verticalLayout_6.addWidget(self.band_4)
        self.band_4_label = QtWidgets.QLabel(self.centralwidget)
        self.band_4_label.setObjectName("band_4_label")
        self.verticalLayout_6.addWidget(self.band_4_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.band_5 = QtWidgets.QSlider(self.centralwidget)
        self.band_5.setMaximum(8)
        self.band_5.setPageStep(1)
        self.band_5.setProperty("value", 4)
        self.band_5.setOrientation(QtCore.Qt.Vertical)
        self.band_5.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.band_5.setObjectName("band_5")
        self.verticalLayout_7.addWidget(self.band_5)
        self.band_5_label = QtWidgets.QLabel(self.centralwidget)
        self.band_5_label.setObjectName("band_5_label")
        self.verticalLayout_7.addWidget(self.band_5_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.band_6 = QtWidgets.QSlider(self.centralwidget)
        self.band_6.setMaximum(8)
        self.band_6.setPageStep(1)
        self.band_6.setProperty("value", 4)
        self.band_6.setOrientation(QtCore.Qt.Vertical)
        self.band_6.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.band_6.setObjectName("band_6")
        self.verticalLayout_8.addWidget(self.band_6)
        self.band_6_label = QtWidgets.QLabel(self.centralwidget)
        self.band_6_label.setObjectName("band_6_label")
        self.verticalLayout_8.addWidget(self.band_6_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.band_7 = QtWidgets.QSlider(self.centralwidget)
        self.band_7.setMaximum(8)
        self.band_7.setPageStep(1)
        self.band_7.setProperty("value", 4)
        self.band_7.setOrientation(QtCore.Qt.Vertical)
        self.band_7.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.band_7.setObjectName("band_7")
        self.verticalLayout_9.addWidget(self.band_7)
        self.band_7_label = QtWidgets.QLabel(self.centralwidget)
        self.band_7_label.setObjectName("band_7_label")
        self.verticalLayout_9.addWidget(self.band_7_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.band_8 = QtWidgets.QSlider(self.centralwidget)
        self.band_8.setMaximum(8)
        self.band_8.setPageStep(1)
        self.band_8.setProperty("value", 4)
        self.band_8.setOrientation(QtCore.Qt.Vertical)
        self.band_8.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.band_8.setObjectName("band_8")
        self.verticalLayout_10.addWidget(self.band_8)
        self.band_8_label = QtWidgets.QLabel(self.centralwidget)
        self.band_8_label.setObjectName("band_8_label")
        self.verticalLayout_10.addWidget(self.band_8_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9)
        self.band_9 = QtWidgets.QSlider(self.centralwidget)
        self.band_9.setMaximum(8)
        self.band_9.setPageStep(1)
        self.band_9.setProperty("value", 4)
        self.band_9.setOrientation(QtCore.Qt.Vertical)
        self.band_9.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.band_9.setObjectName("band_9")
        self.verticalLayout_11.addWidget(self.band_9)
        self.band_9_label = QtWidgets.QLabel(self.centralwidget)
        self.band_9_label.setObjectName("band_9_label")
        self.verticalLayout_11.addWidget(self.band_9_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_12.addWidget(self.label_10)
        self.band_10 = QtWidgets.QSlider(self.centralwidget)
        self.band_10.setMaximum(8)
        self.band_10.setPageStep(1)
        self.band_10.setProperty("value", 4)
        self.band_10.setOrientation(QtCore.Qt.Vertical)
        self.band_10.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.band_10.setObjectName("band_10")
        self.verticalLayout_12.addWidget(self.band_10)
        self.band_10_label = QtWidgets.QLabel(self.centralwidget)
        self.band_10_label.setObjectName("band_10_label")
        self.verticalLayout_12.addWidget(self.band_10_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_16.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.palettes_box = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.palettes_box.setFont(font)
        self.palettes_box.setObjectName("palettes_box")
        self.palettes_box.addItem("")
        self.palettes_box.addItem("")
        self.palettes_box.addItem("")
        self.palettes_box.addItem("")
        self.palettes_box.addItem("")
        self.verticalLayout_13.addWidget(self.palettes_box)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_13.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_16.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.playback_speed_before.setCurrentIndex(2)
        self.playback_speed_after.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SBME - Sound Equalizer"))
        self.label_11.setText(_translate("MainWindow", "Original Plot"))
        self.label_24.setText(_translate("MainWindow", "Equalized Spectrogram"))
        self.label_13.setText(_translate("MainWindow", "Original Spectrogram"))
        self.label_12.setText(_translate("MainWindow", "Equalized Plot"))
        self.current_time_before.setText(_translate("MainWindow", "0:00"))
        self.total_time_before.setText(_translate("MainWindow", "0:00"))
        self.playback_speed_before.setItemText(0, _translate("MainWindow", "x0.5"))
        self.playback_speed_before.setItemText(1, _translate("MainWindow", "x0.75"))
        self.playback_speed_before.setItemText(2, _translate("MainWindow", "x1.0"))
        self.playback_speed_before.setItemText(3, _translate("MainWindow", "x1.25"))
        self.playback_speed_before.setItemText(4, _translate("MainWindow", "x1.5"))
        self.playback_speed_before.setItemText(5, _translate("MainWindow", "x2.0"))
        self.current_time_after.setText(_translate("MainWindow", "0:00"))
        self.total_time_after.setText(_translate("MainWindow", "0:00"))
        self.playback_speed_after.setItemText(0, _translate("MainWindow", "x0.5"))
        self.playback_speed_after.setItemText(1, _translate("MainWindow", "x0.75"))
        self.playback_speed_after.setItemText(2, _translate("MainWindow", "x1.0"))
        self.playback_speed_after.setItemText(3, _translate("MainWindow", "x1.25"))
        self.playback_speed_after.setItemText(4, _translate("MainWindow", "x1.5"))
        self.playback_speed_after.setItemText(5, _translate("MainWindow", "x2.0"))
        self.max_freq_content_label.setText(_translate("MainWindow", "MAX"))
        self.max_freq_content_lab.setText(_translate("MainWindow", "16384"))
        self.min_freq_content_label.setText(_translate("MainWindow", "MIN"))
        self.min_freq_content_lab.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "2.2K"))
        self.band_1_label.setText(_translate("MainWindow", "1dB"))
        self.label_2.setText(_translate("MainWindow", "4.4K"))
        self.band_2_label.setText(_translate("MainWindow", "1dB"))
        self.label_3.setText(_translate("MainWindow", "6.6K"))
        self.band_3_label.setText(_translate("MainWindow", "1dB"))
        self.label_4.setText(_translate("MainWindow", "8.8K"))
        self.band_4_label.setText(_translate("MainWindow", "1dB"))
        self.label_5.setText(_translate("MainWindow", "11K"))
        self.band_5_label.setText(_translate("MainWindow", "1dB"))
        self.label_6.setText(_translate("MainWindow", "13.2K"))
        self.band_6_label.setText(_translate("MainWindow", "1dB"))
        self.label_7.setText(_translate("MainWindow", "15.4K"))
        self.band_7_label.setText(_translate("MainWindow", "1dB"))
        self.label_8.setText(_translate("MainWindow", "17.6K"))
        self.band_8_label.setText(_translate("MainWindow", "1dB"))
        self.label_9.setText(_translate("MainWindow", "19.8K"))
        self.band_9_label.setText(_translate("MainWindow", "1dB"))
        self.label_10.setText(_translate("MainWindow", "22K"))
        self.band_10_label.setText(_translate("MainWindow", "1dB"))
        self.palettes_box.setItemText(0, _translate("MainWindow", "twilight"))
        self.palettes_box.setItemText(1, _translate("MainWindow", "Blues"))
        self.palettes_box.setItemText(2, _translate("MainWindow", "Greys"))
        self.palettes_box.setItemText(3, _translate("MainWindow", "ocean"))
        self.palettes_box.setItemText(4, _translate("MainWindow", "nipy_spectral"))
        self.pushButton.setText(_translate("MainWindow", "Print PDF"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())