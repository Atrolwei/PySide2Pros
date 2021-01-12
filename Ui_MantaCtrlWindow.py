# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MantaCtrlWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(609, 650)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.status_overview = QVBoxLayout()
        self.status_overview.setObjectName(u"status_overview")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.yaw_label = QLabel(self.centralwidget)
        self.yaw_label.setObjectName(u"yaw_label")

        self.verticalLayout_6.addWidget(self.yaw_label)

        self.roll_label = QLabel(self.centralwidget)
        self.roll_label.setObjectName(u"roll_label")

        self.verticalLayout_6.addWidget(self.roll_label)

        self.pitch_label = QLabel(self.centralwidget)
        self.pitch_label.setObjectName(u"pitch_label")

        self.verticalLayout_6.addWidget(self.pitch_label)

        self.depth_label = QLabel(self.centralwidget)
        self.depth_label.setObjectName(u"depth_label")

        self.verticalLayout_6.addWidget(self.depth_label)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_17)

        self.longitude_label = QLabel(self.centralwidget)
        self.longitude_label.setObjectName(u"longitude_label")

        self.horizontalLayout_2.addWidget(self.longitude_label)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_2.addWidget(self.label_13)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_18)

        self.latitude_label = QLabel(self.centralwidget)
        self.latitude_label.setObjectName(u"latitude_label")

        self.horizontalLayout_3.addWidget(self.latitude_label)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.yaw_desire = QLineEdit(self.centralwidget)
        self.yaw_desire.setObjectName(u"yaw_desire")

        self.horizontalLayout_6.addWidget(self.yaw_desire)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.pitch_desire = QLineEdit(self.centralwidget)
        self.pitch_desire.setObjectName(u"pitch_desire")

        self.horizontalLayout_6.addWidget(self.pitch_desire)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_4.addWidget(self.label_20)

        self.depth_desire = QLineEdit(self.centralwidget)
        self.depth_desire.setObjectName(u"depth_desire")

        self.horizontalLayout_4.addWidget(self.depth_desire)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_4.addWidget(self.label_19)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_16)

        self.ctrl_begin = QLineEdit(self.centralwidget)
        self.ctrl_begin.setObjectName(u"ctrl_begin")

        self.horizontalLayout_4.addWidget(self.ctrl_begin)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame)

        self.button_desire_send = QPushButton(self.centralwidget)
        self.button_desire_send.setObjectName(u"button_desire_send")

        self.horizontalLayout_5.addWidget(self.button_desire_send)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addLayout(self.verticalLayout_9)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.status_overview.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.status_overview, 0, 0, 1, 1)

        self.MFAC_ctrl = QVBoxLayout()
        self.MFAC_ctrl.setObjectName(u"MFAC_ctrl")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_44 = QLabel(self.centralwidget)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_30.addWidget(self.label_44)


        self.MFAC_ctrl.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_45 = QLabel(self.centralwidget)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_29.addWidget(self.label_45)

        self.yaw_pitch_depth = QLineEdit(self.centralwidget)
        self.yaw_pitch_depth.setObjectName(u"yaw_pitch_depth")

        self.horizontalLayout_29.addWidget(self.yaw_pitch_depth)


        self.MFAC_ctrl.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_76 = QLabel(self.centralwidget)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_28.addWidget(self.label_76)

        self.miu = QLineEdit(self.centralwidget)
        self.miu.setObjectName(u"miu")

        self.horizontalLayout_28.addWidget(self.miu)

        self.label_75 = QLabel(self.centralwidget)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_28.addWidget(self.label_75)

        self.yita = QLineEdit(self.centralwidget)
        self.yita.setObjectName(u"yita")

        self.horizontalLayout_28.addWidget(self.yita)

        self.label_46 = QLabel(self.centralwidget)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_28.addWidget(self.label_46)

        self.lamda = QLineEdit(self.centralwidget)
        self.lamda.setObjectName(u"lamda")

        self.horizontalLayout_28.addWidget(self.lamda)


        self.MFAC_ctrl.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_78 = QLabel(self.centralwidget)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_21.addWidget(self.label_78)

        self.fai_init_0 = QLineEdit(self.centralwidget)
        self.fai_init_0.setObjectName(u"fai_init_0")

        self.horizontalLayout_21.addWidget(self.fai_init_0)

        self.label_77 = QLabel(self.centralwidget)
        self.label_77.setObjectName(u"label_77")

        self.horizontalLayout_21.addWidget(self.label_77)

        self.fai_init_1 = QLineEdit(self.centralwidget)
        self.fai_init_1.setObjectName(u"fai_init_1")

        self.horizontalLayout_21.addWidget(self.fai_init_1)

        self.label_79 = QLabel(self.centralwidget)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_21.addWidget(self.label_79)

        self.fai_init_2 = QLineEdit(self.centralwidget)
        self.fai_init_2.setObjectName(u"fai_init_2")

        self.horizontalLayout_21.addWidget(self.fai_init_2)


        self.MFAC_ctrl.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_82 = QLabel(self.centralwidget)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_19.addWidget(self.label_82)

        self.rou_0 = QLineEdit(self.centralwidget)
        self.rou_0.setObjectName(u"rou_0")

        self.horizontalLayout_19.addWidget(self.rou_0)

        self.label_81 = QLabel(self.centralwidget)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_19.addWidget(self.label_81)

        self.rou_1 = QLineEdit(self.centralwidget)
        self.rou_1.setObjectName(u"rou_1")

        self.horizontalLayout_19.addWidget(self.rou_1)

        self.label_80 = QLabel(self.centralwidget)
        self.label_80.setObjectName(u"label_80")

        self.horizontalLayout_19.addWidget(self.label_80)

        self.rou_2 = QLineEdit(self.centralwidget)
        self.rou_2.setObjectName(u"rou_2")

        self.horizontalLayout_19.addWidget(self.rou_2)


        self.MFAC_ctrl.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)

        self.button_MFAC_send = QPushButton(self.centralwidget)
        self.button_MFAC_send.setObjectName(u"button_MFAC_send")

        self.horizontalLayout_20.addWidget(self.button_MFAC_send)


        self.MFAC_ctrl.addLayout(self.horizontalLayout_20)


        self.gridLayout.addLayout(self.MFAC_ctrl, 1, 1, 1, 1)

        self.openloop_ctrl = QVBoxLayout()
        self.openloop_ctrl.setObjectName(u"openloop_ctrl")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_43 = QLabel(self.centralwidget)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_17.addWidget(self.label_43)


        self.openloop_ctrl.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_73 = QLabel(self.centralwidget)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_27.addWidget(self.label_73)

        self.OL_frez_l = QLineEdit(self.centralwidget)
        self.OL_frez_l.setObjectName(u"OL_frez_l")

        self.horizontalLayout_27.addWidget(self.OL_frez_l)

        self.label_72 = QLabel(self.centralwidget)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_27.addWidget(self.label_72)

        self.label_74 = QLabel(self.centralwidget)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_27.addWidget(self.label_74)

        self.OL_frez_r = QLineEdit(self.centralwidget)
        self.OL_frez_r.setObjectName(u"OL_frez_r")

        self.horizontalLayout_27.addWidget(self.OL_frez_r)

        self.label_71 = QLabel(self.centralwidget)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_27.addWidget(self.label_71)


        self.openloop_ctrl.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_70 = QLabel(self.centralwidget)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_26.addWidget(self.label_70)

        self.OL_flap_l = QLineEdit(self.centralwidget)
        self.OL_flap_l.setObjectName(u"OL_flap_l")

        self.horizontalLayout_26.addWidget(self.OL_flap_l)

        self.label_69 = QLabel(self.centralwidget)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_26.addWidget(self.label_69)

        self.label_68 = QLabel(self.centralwidget)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_26.addWidget(self.label_68)

        self.OL_flap_r = QLineEdit(self.centralwidget)
        self.OL_flap_r.setObjectName(u"OL_flap_r")

        self.horizontalLayout_26.addWidget(self.OL_flap_r)

        self.label_67 = QLabel(self.centralwidget)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_26.addWidget(self.label_67)


        self.openloop_ctrl.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_66 = QLabel(self.centralwidget)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_25.addWidget(self.label_66)

        self.OL_twist_l = QLineEdit(self.centralwidget)
        self.OL_twist_l.setObjectName(u"OL_twist_l")

        self.horizontalLayout_25.addWidget(self.OL_twist_l)

        self.label_65 = QLabel(self.centralwidget)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_25.addWidget(self.label_65)

        self.label_64 = QLabel(self.centralwidget)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_25.addWidget(self.label_64)

        self.OL_twist_r = QLineEdit(self.centralwidget)
        self.OL_twist_r.setObjectName(u"OL_twist_r")

        self.horizontalLayout_25.addWidget(self.OL_twist_r)

        self.label_63 = QLabel(self.centralwidget)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_25.addWidget(self.label_63)


        self.openloop_ctrl.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_62 = QLabel(self.centralwidget)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_24.addWidget(self.label_62)

        self.OL_dphi_l = QLineEdit(self.centralwidget)
        self.OL_dphi_l.setObjectName(u"OL_dphi_l")

        self.horizontalLayout_24.addWidget(self.OL_dphi_l)

        self.label_61 = QLabel(self.centralwidget)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_24.addWidget(self.label_61)

        self.label_60 = QLabel(self.centralwidget)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_24.addWidget(self.label_60)

        self.OL_dphi_r = QLineEdit(self.centralwidget)
        self.OL_dphi_r.setObjectName(u"OL_dphi_r")

        self.horizontalLayout_24.addWidget(self.OL_dphi_r)

        self.label_59 = QLabel(self.centralwidget)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_24.addWidget(self.label_59)


        self.openloop_ctrl.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_58 = QLabel(self.centralwidget)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_23.addWidget(self.label_58)

        self.OL_bias_l = QLineEdit(self.centralwidget)
        self.OL_bias_l.setObjectName(u"OL_bias_l")

        self.horizontalLayout_23.addWidget(self.OL_bias_l)

        self.label_57 = QLabel(self.centralwidget)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_23.addWidget(self.label_57)

        self.label_56 = QLabel(self.centralwidget)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_23.addWidget(self.label_56)

        self.OL_bias_r = QLineEdit(self.centralwidget)
        self.OL_bias_r.setObjectName(u"OL_bias_r")

        self.horizontalLayout_23.addWidget(self.OL_bias_r)

        self.label_55 = QLabel(self.centralwidget)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_23.addWidget(self.label_55)


        self.openloop_ctrl.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_86 = QLabel(self.centralwidget)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_31.addWidget(self.label_86)

        self.OL_twistbias_l = QLineEdit(self.centralwidget)
        self.OL_twistbias_l.setObjectName(u"OL_twistbias_l")

        self.horizontalLayout_31.addWidget(self.OL_twistbias_l)

        self.label_85 = QLabel(self.centralwidget)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_31.addWidget(self.label_85)

        self.label_84 = QLabel(self.centralwidget)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_31.addWidget(self.label_84)

        self.OL_twistbias_r = QLineEdit(self.centralwidget)
        self.OL_twistbias_r.setObjectName(u"OL_twistbias_r")

        self.horizontalLayout_31.addWidget(self.OL_twistbias_r)

        self.label_83 = QLabel(self.centralwidget)
        self.label_83.setObjectName(u"label_83")

        self.horizontalLayout_31.addWidget(self.label_83)


        self.openloop_ctrl.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_54 = QLabel(self.centralwidget)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_22.addWidget(self.label_54)

        self.OL_tail_l = QLineEdit(self.centralwidget)
        self.OL_tail_l.setObjectName(u"OL_tail_l")

        self.horizontalLayout_22.addWidget(self.OL_tail_l)

        self.label_53 = QLabel(self.centralwidget)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_22.addWidget(self.label_53)

        self.label_52 = QLabel(self.centralwidget)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_22.addWidget(self.label_52)

        self.OL_tail_r = QLineEdit(self.centralwidget)
        self.OL_tail_r.setObjectName(u"OL_tail_r")

        self.horizontalLayout_22.addWidget(self.OL_tail_r)

        self.label_51 = QLabel(self.centralwidget)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_22.addWidget(self.label_51)


        self.openloop_ctrl.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.button_STOP = QPushButton(self.centralwidget)
        self.button_STOP.setObjectName(u"button_STOP")

        self.horizontalLayout_18.addWidget(self.button_STOP)

        self.button_OL_RUN = QPushButton(self.centralwidget)
        self.button_OL_RUN.setObjectName(u"button_OL_RUN")

        self.horizontalLayout_18.addWidget(self.button_OL_RUN)


        self.openloop_ctrl.addLayout(self.horizontalLayout_18)


        self.gridLayout.addLayout(self.openloop_ctrl, 0, 1, 1, 1)

        self.PID_ctrl = QVBoxLayout()
        self.PID_ctrl.setObjectName(u"PID_ctrl")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_15.addWidget(self.label_21)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_14.addWidget(self.label_26)

        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_14.addWidget(self.label_31)

        self.yaw_kp = QLineEdit(self.centralwidget)
        self.yaw_kp.setObjectName(u"yaw_kp")

        self.horizontalLayout_14.addWidget(self.yaw_kp)

        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_14.addWidget(self.label_28)

        self.yaw_ki = QLineEdit(self.centralwidget)
        self.yaw_ki.setObjectName(u"yaw_ki")

        self.horizontalLayout_14.addWidget(self.yaw_ki)

        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_14.addWidget(self.label_27)

        self.yaw_kd = QLineEdit(self.centralwidget)
        self.yaw_kd.setObjectName(u"yaw_kd")

        self.horizontalLayout_14.addWidget(self.yaw_kd)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_13.addWidget(self.label_25)

        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_13.addWidget(self.label_32)

        self.pitch_kp = QLineEdit(self.centralwidget)
        self.pitch_kp.setObjectName(u"pitch_kp")

        self.horizontalLayout_13.addWidget(self.pitch_kp)

        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_13.addWidget(self.label_29)

        self.pitch_ki = QLineEdit(self.centralwidget)
        self.pitch_ki.setObjectName(u"pitch_ki")

        self.horizontalLayout_13.addWidget(self.pitch_ki)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_13.addWidget(self.label_24)

        self.pitch_kd = QLineEdit(self.centralwidget)
        self.pitch_kd.setObjectName(u"pitch_kd")

        self.horizontalLayout_13.addWidget(self.pitch_kd)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_12.addWidget(self.label_23)

        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_12.addWidget(self.label_33)

        self.depth_kp = QLineEdit(self.centralwidget)
        self.depth_kp.setObjectName(u"depth_kp")

        self.horizontalLayout_12.addWidget(self.depth_kp)

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_12.addWidget(self.label_30)

        self.depth_ki = QLineEdit(self.centralwidget)
        self.depth_ki.setObjectName(u"depth_ki")

        self.horizontalLayout_12.addWidget(self.depth_ki)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_12.addWidget(self.label_22)

        self.depth_kd = QLineEdit(self.centralwidget)
        self.depth_kd.setObjectName(u"depth_kd")

        self.horizontalLayout_12.addWidget(self.depth_kd)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)


        self.PID_ctrl.addLayout(self.verticalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_3)

        self.button_PID_send = QPushButton(self.centralwidget)
        self.button_PID_send.setObjectName(u"button_PID_send")

        self.horizontalLayout_9.addWidget(self.button_PID_send)


        self.PID_ctrl.addLayout(self.horizontalLayout_9)

        self.Base_ctrl = QVBoxLayout()
        self.Base_ctrl.setObjectName(u"Base_ctrl")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_16.addWidget(self.label_34)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_4)


        self.Base_ctrl.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_37 = QLabel(self.centralwidget)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_11.addWidget(self.label_37)

        self.base_l_flap = QLineEdit(self.centralwidget)
        self.base_l_flap.setObjectName(u"base_l_flap")

        self.horizontalLayout_11.addWidget(self.base_l_flap)

        self.label_38 = QLabel(self.centralwidget)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_11.addWidget(self.label_38)

        self.label_36 = QLabel(self.centralwidget)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_11.addWidget(self.label_36)

        self.base_r_flap = QLineEdit(self.centralwidget)
        self.base_r_flap.setObjectName(u"base_r_flap")

        self.horizontalLayout_11.addWidget(self.base_r_flap)

        self.label_35 = QLabel(self.centralwidget)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_11.addWidget(self.label_35)


        self.Base_ctrl.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_41 = QLabel(self.centralwidget)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_10.addWidget(self.label_41)

        self.base_l_roll = QLineEdit(self.centralwidget)
        self.base_l_roll.setObjectName(u"base_l_roll")

        self.horizontalLayout_10.addWidget(self.base_l_roll)

        self.label_42 = QLabel(self.centralwidget)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_10.addWidget(self.label_42)

        self.label_40 = QLabel(self.centralwidget)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_10.addWidget(self.label_40)

        self.base_r_roll = QLineEdit(self.centralwidget)
        self.base_r_roll.setObjectName(u"base_r_roll")

        self.horizontalLayout_10.addWidget(self.base_r_roll)

        self.label_39 = QLabel(self.centralwidget)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_10.addWidget(self.label_39)


        self.Base_ctrl.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_50 = QLabel(self.centralwidget)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_7.addWidget(self.label_50)

        self.base_l_bias = QLineEdit(self.centralwidget)
        self.base_l_bias.setObjectName(u"base_l_bias")

        self.horizontalLayout_7.addWidget(self.base_l_bias)

        self.label_49 = QLabel(self.centralwidget)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_7.addWidget(self.label_49)

        self.label_48 = QLabel(self.centralwidget)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_7.addWidget(self.label_48)

        self.base_r_bias = QLineEdit(self.centralwidget)
        self.base_r_bias.setObjectName(u"base_r_bias")

        self.horizontalLayout_7.addWidget(self.base_r_bias)

        self.label_47 = QLabel(self.centralwidget)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_7.addWidget(self.label_47)


        self.Base_ctrl.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_5)

        self.button_base_send = QPushButton(self.centralwidget)
        self.button_base_send.setObjectName(u"button_base_send")

        self.horizontalLayout_8.addWidget(self.button_base_send)


        self.Base_ctrl.addLayout(self.horizontalLayout_8)


        self.PID_ctrl.addLayout(self.Base_ctrl)


        self.gridLayout.addLayout(self.PID_ctrl, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Manta Controller", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Yaw", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Roll", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"Pitch", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Depth", None))
        self.yaw_label.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.roll_label.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.pitch_label.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.depth_label.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"cm", None))
        self.label_17.setText(QCoreApplication.translate("mainWindow", u"\u7ecf\u5ea6", None))
        self.longitude_label.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_18.setText(QCoreApplication.translate("mainWindow", u"\u7eac\u5ea6", None))
        self.latitude_label.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"\u822a\u5411\u671f\u671b", None))
        self.yaw_desire.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"\u4fef\u4ef0\u671f\u671b", None))
        self.pitch_desire.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_20.setText(QCoreApplication.translate("mainWindow", u"\u6df1\u5ea6\u671f\u671b", None))
        self.depth_desire.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_16.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u59cb\u63a7\u5236", None))
        self.ctrl_begin.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_14.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.button_desire_send.setText(QCoreApplication.translate("mainWindow", u"SEND", None))
        self.label_44.setText(QCoreApplication.translate("mainWindow", u"  MFAC Parameters", None))
        self.label_45.setText(QCoreApplication.translate("mainWindow", u"  0:\u504f\u822a/1:\u4fef\u4ef0/2:\u5b9a\u6df1", None))
        self.yaw_pitch_depth.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_76.setText(QCoreApplication.translate("mainWindow", u"  \u03bc    ", None))
        self.miu.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.label_75.setText(QCoreApplication.translate("mainWindow", u"\u03b7    ", None))
        self.yita.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.label_46.setText(QCoreApplication.translate("mainWindow", u"\u03bb    ", None))
        self.lamda.setText(QCoreApplication.translate("mainWindow", u"0.05", None))
        self.label_78.setText(QCoreApplication.translate("mainWindow", u"  \u03c6ini0", None))
        self.fai_init_0.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.label_77.setText(QCoreApplication.translate("mainWindow", u"\u03c6ini1", None))
        self.fai_init_1.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.label_79.setText(QCoreApplication.translate("mainWindow", u"\u03c6ini2", None))
        self.fai_init_2.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.label_82.setText(QCoreApplication.translate("mainWindow", u"  \u03c10   ", None))
        self.rou_0.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.label_81.setText(QCoreApplication.translate("mainWindow", u"\u03c11   ", None))
        self.rou_1.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.label_80.setText(QCoreApplication.translate("mainWindow", u"\u03c12   ", None))
        self.rou_2.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.button_MFAC_send.setText(QCoreApplication.translate("mainWindow", u"SEND MFAC", None))
        self.label_43.setText(QCoreApplication.translate("mainWindow", u"  Open Loop Parameters", None))
        self.label_73.setText(QCoreApplication.translate("mainWindow", u"  \u5de6\u9891\u7387", None))
        self.OL_frez_l.setText(QCoreApplication.translate("mainWindow", u"0.7", None))
        self.label_72.setText(QCoreApplication.translate("mainWindow", u"Hz", None))
        self.label_74.setText(QCoreApplication.translate("mainWindow", u"\u53f3\u9891\u7387", None))
        self.OL_frez_r.setText(QCoreApplication.translate("mainWindow", u"0.7", None))
        self.label_71.setText(QCoreApplication.translate("mainWindow", u"Hz", None))
        self.label_70.setText(QCoreApplication.translate("mainWindow", u"  \u5de6\u6446\u5e45", None))
        self.OL_flap_l.setText(QCoreApplication.translate("mainWindow", u"15", None))
        self.label_69.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_68.setText(QCoreApplication.translate("mainWindow", u"\u53f3\u6446\u5e45", None))
        self.OL_flap_r.setText(QCoreApplication.translate("mainWindow", u"15", None))
        self.label_67.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_66.setText(QCoreApplication.translate("mainWindow", u"  \u5de6\u626d\u5e45", None))
        self.OL_twist_l.setText(QCoreApplication.translate("mainWindow", u"20", None))
        self.label_65.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_64.setText(QCoreApplication.translate("mainWindow", u"\u53f3\u626d\u5e45", None))
        self.OL_twist_r.setText(QCoreApplication.translate("mainWindow", u"20", None))
        self.label_63.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_62.setText(QCoreApplication.translate("mainWindow", u"  \u5de6\u76f8\u5dee", None))
        self.OL_dphi_l.setText(QCoreApplication.translate("mainWindow", u"90", None))
        self.label_61.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_60.setText(QCoreApplication.translate("mainWindow", u"\u53f3\u76f8\u5dee", None))
        self.OL_dphi_r.setText(QCoreApplication.translate("mainWindow", u"90", None))
        self.label_59.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_58.setText(QCoreApplication.translate("mainWindow", u"  \u5de6\u6446\u504f", None))
        self.OL_bias_l.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_57.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_56.setText(QCoreApplication.translate("mainWindow", u"\u53f3\u6446\u504f", None))
        self.OL_bias_r.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_55.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_86.setText(QCoreApplication.translate("mainWindow", u"  \u5de6\u626d\u504f", None))
        self.OL_twistbias_l.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_85.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_84.setText(QCoreApplication.translate("mainWindow", u"\u53f3\u626d\u504f", None))
        self.OL_twistbias_r.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_83.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_54.setText(QCoreApplication.translate("mainWindow", u"  \u5de6\u5c3e\u9ccd", None))
        self.OL_tail_l.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_53.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_52.setText(QCoreApplication.translate("mainWindow", u"\u53f3\u5c3e\u9ccd", None))
        self.OL_tail_r.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_51.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.button_STOP.setText(QCoreApplication.translate("mainWindow", u"STOP", None))
        self.button_OL_RUN.setText(QCoreApplication.translate("mainWindow", u"RUN", None))
        self.label_21.setText(QCoreApplication.translate("mainWindow", u"PID Parameters", None))
        self.label_26.setText(QCoreApplication.translate("mainWindow", u"Yaw  ", None))
        self.label_31.setText(QCoreApplication.translate("mainWindow", u"Kp", None))
        self.yaw_kp.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_28.setText(QCoreApplication.translate("mainWindow", u"Ki", None))
        self.yaw_ki.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_27.setText(QCoreApplication.translate("mainWindow", u"Kd", None))
        self.yaw_kd.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_25.setText(QCoreApplication.translate("mainWindow", u"Pitch", None))
        self.label_32.setText(QCoreApplication.translate("mainWindow", u"Kp", None))
        self.pitch_kp.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_29.setText(QCoreApplication.translate("mainWindow", u"Ki", None))
        self.pitch_ki.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_24.setText(QCoreApplication.translate("mainWindow", u"Kd", None))
        self.pitch_kd.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_23.setText(QCoreApplication.translate("mainWindow", u"Depth", None))
        self.label_33.setText(QCoreApplication.translate("mainWindow", u"Kp", None))
        self.depth_kp.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_30.setText(QCoreApplication.translate("mainWindow", u"Ki", None))
        self.depth_ki.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_22.setText(QCoreApplication.translate("mainWindow", u"Kd", None))
        self.depth_kd.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.button_PID_send.setText(QCoreApplication.translate("mainWindow", u"SEND PID", None))
        self.label_34.setText(QCoreApplication.translate("mainWindow", u"Base Parameters", None))
        self.label_37.setText(QCoreApplication.translate("mainWindow", u"\u5de6\u80f8\u9ccd\u6446\u5e45\u57fa\u51c6", None))
        self.base_l_flap.setText(QCoreApplication.translate("mainWindow", u"15", None))
        self.label_38.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_36.setText(QCoreApplication.translate("mainWindow", u"   \u53f3\u80f8\u9ccd\u6446\u5e45\u57fa\u51c6", None))
        self.base_r_flap.setText(QCoreApplication.translate("mainWindow", u"15", None))
        self.label_35.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_41.setText(QCoreApplication.translate("mainWindow", u"\u5de6\u80f8\u9ccd\u626d\u5e45\u57fa\u51c6", None))
        self.base_l_roll.setText(QCoreApplication.translate("mainWindow", u"30", None))
        self.label_42.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_40.setText(QCoreApplication.translate("mainWindow", u"   \u53f3\u80f8\u9ccd\u626d\u5e45\u57fa\u51c6", None))
        self.base_r_roll.setText(QCoreApplication.translate("mainWindow", u"27", None))
        self.label_39.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_50.setText(QCoreApplication.translate("mainWindow", u"\u5de6\u80f8\u9ccd\u504f\u7f6e\u57fa\u51c6", None))
        self.base_l_bias.setText(QCoreApplication.translate("mainWindow", u"0", None))
        self.label_49.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.label_48.setText(QCoreApplication.translate("mainWindow", u"   \u53f3\u80f8\u9ccd\u504f\u7f6e\u57fa\u51c6", None))
        self.base_r_bias.setText(QCoreApplication.translate("mainWindow", u"4", None))
        self.label_47.setText(QCoreApplication.translate("mainWindow", u"\u00b0", None))
        self.button_base_send.setText(QCoreApplication.translate("mainWindow", u"SEND Base", None))
    # retranslateUi

