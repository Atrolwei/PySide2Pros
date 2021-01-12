# Test git
# File: main.py
import sys
from PySide2.QtWidgets import QApplication,QMainWindow
from Ui_MantaCtrlWindow import Ui_mainWindow
from PySide2.QtCore import QFile, QIODevice, Slot
from PySide2.QtNetwork import QTcpSocket
from PySide2.QtNetwork import QAbstractSocket
from PySide2.QtCore import QTimer


class MantaSocket:
    def __init__(self) -> None:
        self.socket=QTcpSocket()
        self.timer=QTimer()
        self.timer.timeout.connect(self.client_listening)
        self.timer.start(1000)

        self.socket.readyRead.connect(self.read_data)
        self.socket.disconnected.connect(self.client_socket_disconnected)
        self.writeflag=0

    def client_listening(self):
        if self.socket.state()==QAbstractSocket.ConnectedState:
            pass
        else:
            self.socket.connectToHost('192.168.7.2',2345)
            if not self.socket.waitForConnected(200):
                return
            print('Connected!!!')
            # self.write_data()

    def read_data(self):
        print("read!!!")
        receive_data=self.socket.readAll()
        if not receive_data.isEmpty():
            # print(socketdata)
            self.socket_data_analysis(receive_data)


    def write_data(self):
        # obj=bytes('hello'.encode())
        # send_str=QByteArray(obj)
        send_str='hello yeah world'
        if self.writeflag:
            self.socket.writeData(send_str,len(send_str))

    def client_socket_disconnected(self):
        print('Socket Disconnect!!!')

    def socket_data_analysis(self,receive):
        '''
        pos_left,pos_right,pos_left_roll,pos_right_roll,dpos_left,dpos_right,dpos_left_roll,dpos_right_roll,pos_behind_left,pos_behind_right,
        roll,yaw,left_A,right_A,yaw_desire,pitch,left_behind,right_behind,pitch_desire,depth_c,depth;
        '''
        # print(receive)
        pos_str = "$POS"
        pos_str_index=receive.indexOf(pos_str.encode())
        aux_num=0
        data_index=0

        data_index=pos_str_index+(4+1)
        aux_num=5
        pos_left=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=5
        pos_right=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=5
        pos_left_roll=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=5
        pos_right_roll=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=5
        dpos_left=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=5
        dpos_right=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=5
        dpos_left_roll=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=5
        dpos_right_roll=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=5
        pos_behind_left=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=5
        pos_behind_right=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=6
        roll=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=6
        yaw=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=6
        left_A=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=6
        right_A=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=6
        yaw_desire=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=6
        pitch=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=6
        left_behind=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=6
        right_behind=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=6
        pitch_desire=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=6
        depth_c=receive.mid(data_index,aux_num).toFloat()[0]

        data_index+=aux_num+1
        aux_num=7
        depth=receive.mid(data_index,aux_num).toFloat()[0]

        # Window UI Display
        window.ui.pitch_label.setText(str(pitch))
        window.ui.roll_label.setText(str(roll))
        window.ui.yaw_label.setText(str(yaw))
        window.ui.depth_label.setText(str(depth))




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui=Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.button_desire_send.clicked.connect(self.send_desire)
        self.ui.button_PID_send.clicked.connect(self.send_PID)
        self.ui.button_MFAC_send.clicked.connect(self.send_MFAC)
        self.ui.button_base_send.clicked.connect(self.send_base)
        self.ui.button_OL_RUN.clicked.connect(self.send_open_loop)
        self.ui.button_STOP.clicked.connect(self.send_STOP)


    def send_desire(self):
        # 发送期望信号
        send_desire="$DESIR,{},{},{},{},\r\n".format(
            int(self.ui.ctrl_begin.text()),
            float(self.ui.yaw_desire.text()),
            float(self.ui.pitch_desire.text()),
            float(self.ui.depth_desire.text()))
        if manta_socket.socket.state()==QAbstractSocket.ConnectedState:
            manta_socket.socket.writeData(send_desire,len(send_desire))
            print('desire send {}'.format(send_desire))
            # Log the command in file...

    def send_PID(self):
        # 发送PID参数
        send_PID="$PID,{},{},{},{},{},{},{},{},{},\r\n".format(
            float(self.ui.yaw_kp.text()),
            float(self.ui.yaw_ki.text()),
            float(self.ui.yaw_kd.text()),
            float(self.ui.pitch_kd.text()),
            float(self.ui.pitch_ki.text()),
            float(self.ui.pitch_kd.text()),
            float(self.ui.depth_kp.text()),
            float(self.ui.depth_ki.text()),
            float(self.ui.depth_kd.text()))
        if manta_socket.socket.state()==QAbstractSocket.ConnectedState:
            manta_socket.socket.writeData(send_PID,len(send_PID))
            print('PID send {}'.format(send_PID))
            # Log the command in file...

    def send_MFAC(self):
        # 发送MFAC参数
        send_MFAC="$MFAC,{},{},{},{},{},{},{},{},{},{},\r\n".format(
            int(self.ui.yaw_pitch_depth.text()),
            float(self.ui.miu.text()),
            float(self.ui.yita.text()),
            float(self.ui.lamda.text()),
            float(self.ui.fai_init_0.text()),
            float(self.ui.fai_init_1.text()),
            float(self.ui.fai_init_2.text()),
            float(self.ui.rou_0.text()),
            float(self.ui.rou_1.text()),
            float(self.ui.rou_2.text()))
        if manta_socket.socket.state()==QAbstractSocket.ConnectedState:
            manta_socket.socket.writeData(send_MFAC,len(send_MFAC))
            print('MFAC send {}'.format(send_MFAC))
            # Log the command in file...

    def send_base(self):
        # 发送BASE参数
        send_base="$BASE,{},{},{},{},{},{},{},\r\n".format(
            float(self.ui.base_l_flap.text()),
            float(self.ui.base_r_flap.text()),
            float(self.ui.base_l_roll.text()),
            float(self.ui.base_r_roll.text()),
            # Pitch_c for depth
            0.0,
            float(self.ui.base_l_bias.text()),
            float(self.ui.base_r_bias.text()))
        if manta_socket.socket.state()==QAbstractSocket.ConnectedState:
            manta_socket.socket.writeData(send_base,len(send_base))
            print('base send {}'.format(send_base))
            # Log the command in file...

    def send_open_loop(self):
        # 发送open_loop参数
        send_open_loop="$DEBUG,{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},\r\n".format(
            #立刻运行开环指令
            1,
            float(self.ui.OL_flap_l.text()),
            float(self.ui.OL_frez_l.text()),
            0,
            float(self.ui.OL_flap_r.text()),
            float(self.ui.OL_frez_r.text()),
            0,
            float(self.ui.OL_twist_l.text()),
            float(self.ui.OL_frez_l.text()),
            float(self.ui.OL_dphi_l.text()),
            float(self.ui.OL_twist_r.text()),
            float(self.ui.OL_frez_r.text()),
            float(self.ui.OL_dphi_r.text()),
            float(self.ui.OL_tail_l.text()),
            float(self.ui.OL_tail_r.text()),
            0,
            float(self.ui.OL_bias_l.text()),
            float(self.ui.OL_bias_r.text()),
            float(self.ui.OL_twistbias_l.text()),
            float(self.ui.OL_twistbias_r.text()))
        if manta_socket.socket.state()==QAbstractSocket.ConnectedState:
            manta_socket.socket.writeData(send_open_loop,len(send_open_loop))
            print('open loop send {}'.format(send_open_loop))
            # Log the command in file...

    def send_STOP(self):
        send_stop="$DEBUG,1,0,0,0,0,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\r\n"
        if manta_socket.socket.state()==QAbstractSocket.ConnectedState:
            manta_socket.socket.writeData(send_stop,len(send_stop))
            print('STOP send {}'.format(send_stop))
            # Log the command in file...





    # def setwriteflag(self):
    #     if manta_socket.writeflag==0:
    #         manta_socket.writeflag=1
    #     else:
    #         manta_socket.writeflag=0


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    # User Defined
    manta_socket=MantaSocket()


    window.show()

    sys.exit(app.exec_())

