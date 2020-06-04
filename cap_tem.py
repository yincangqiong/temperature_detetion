import serial
import math
import cv2

portx="COM7"
bps=115200
timex=5
#串口执行到这已经打开 再用open命令会报错
ser = serial.Serial(portx, int(bps), timeout=1, parity=serial.PARITY_NONE,stopbits=1)
if (ser.isOpen()):
    print("open success")

    while (True):
        ret, frame = cap.read()
        temp = 0
        # 向端口些数据 字符串必须译码
        ser.write("VCMD=TMP".encode())
        for i in range(6):
            line = ser.readline()
            if i==1:
                temp_str=line.strip().decode().split('=0x')[1]
                for j in range(4):
                        if temp_str[j]== 'A':
                            temp = temp + 10 * math.pow(16,(3-j))

                        elif temp_str[j] == 'B':
                            temp = temp + 11 * math.pow(16,(3-j))

                        elif temp_str[j] == 'C':
                            temp = temp + 12 * math.pow(16,(3-j))

                        elif temp_str[j] == 'D':
                            temp = temp + 13 * math.pow(16, (3-j))

                        elif temp_str[j] == 'E':
                            temp = temp + 14 * math.pow(16, (3-j))

                        elif temp_str[j] == 'F':
                            temp = temp + 15 * math.pow(16,(3-j))

                        elif temp_str[j] == '0':
                            temp = temp + 0 * math.pow(16,(3-j))

                        elif temp_str[j] == '1':
                            temp = temp + 1 * math.pow(16,(3-j))

                        elif temp_str[j] == '2':
                            temp = temp + 2 * math.pow(16,(3-j))

                        elif temp_str[j] == '3':
                            temp = temp + 3 * math.pow(16,(3-j))

                        elif temp_str[j] == '4':
                            temp = temp + 4 * math.pow(16,(3-j))

                        elif temp_str[j] == '5':
                            temp = temp + 5 * math.pow(16,(3-j))

                        elif temp_str[j] =='6':
                            temp = temp + 6 * math.pow(16,(3-j))

                        elif temp_str[j] == '7':
                            temp = temp + 0 * math.pow(16,(3-j))

                        elif temp_str[j] == '8':
                            temp = temp + 0 * math.pow(16,(3-j))

                        elif temp_str[j] == '9':
                            temp = temp + 0 * math.pow(16,(3-j))

                temp = round(temp / 10, 1)
                if (temp < 35):
                    temp = 35.0
                print(temp)
                #line=0
        font=cv2.FONT_HERSHEY_SIMPLEX #使用默认字体
        if temp < 37:
            cv2.putText(frame, 'temperature:{}'.format(temp), (0, 40), font, 0.5, (0, 255, 0), 2)
        else:
            cv2.putText(frame, 'temperature:{}'.format(temp), (0, 40), font, 0.5, (0, 0, 255), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

else:
	print("open failed")
ser.close()#关闭端口

