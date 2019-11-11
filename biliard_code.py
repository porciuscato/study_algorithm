import socket
import time
import math

# User and Game Server Information
NICKNAME = 'Jinhong'
HOST = '127.0.0.1'
# HOST = '70.12.107.40'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%f/%f' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0    
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    angle = 0
    power = 0
    ######################################################################################
    # 주어진 정보를 바탕으로 샷을 할 방향과 세기를 결정해서 angle, power 값으로 지정 #
    ######################################################################################
    custom_holes = [
        [3, 127], # 0
        [130.7, 127], # 0
        [256.5, 127.5], # ??
        [2.5, 2.5], # 0
        [130.7, 3], # 0
        [257, 3] # 0
    ]
    ball_x = gameData.balls[0][0]
    ball_y = gameData.balls[0][1]

    # 칠 수 있는 볼을 찾기
    for i in range(1, NUMBER_OF_BALLS + 1):
        if gameData.balls[i][0]:
            target_x = gameData.balls[i][0]
            target_y = gameData.balls[i][1]
            break
    
    # ball과 target의 좌표를 기반으로 갈 만한 hole을 찾는다. 일단은 6번으로
    find_x = ball_x - target_x
    find_y = ball_y - target_y

    if find_x <= 0 and find_y <= 0: # 1
        direc = 1
    elif find_x <= 0 and find_y > 0: # 4
        direc = 4
    elif find_x >= 0 and find_y <= 0: # 2
        direc = 2
    elif find_x >= 0 and find_y > 0: # 3
        direc = 3

    # ball 좌표를 기준으로 hole을 찾자
    hubo = []
    for c_x, c_y in custom_holes:
        if direc == 1:
            if c_y >= ball_y and c_x >= ball_x:
                hubo.append([c_x, c_y])
        elif direc == 2:
            if c_y >= ball_y and c_x <= ball_x:
                hubo.append([c_x, c_y])
        elif direc == 3:
            if c_y <= ball_y and c_x <= ball_x:
                hubo.append([c_x, c_y])
        elif direc == 4:
            if c_y <= ball_y and c_x >= ball_x:
                hubo.append([c_x, c_y])

    if len(hubo) == 1:
        hole_x = hubo[0][0]
        hole_y = hubo[0][1]
    else:
        if direc == 1:
            if target_x <= hubo[0][0]:
                hole_x = hubo[0][0]
                hole_y = hubo[0][1]
            else:
                hole_x = hubo[1][0]
                hole_y = hubo[1][1]
        elif direc == 2:
            if target_x >= hubo[1][0]:
                hole_x = hubo[1][0]
                hole_y = hubo[1][1]
            else:
                hole_x = hubo[0][0]
                hole_y = hubo[0][1]
        elif direc == 3:
            if target_x >= hubo[1][0]:
                hole_x = hubo[1][0]
                hole_y = hubo[1][1]
            else:
                hole_x = hubo[0][0]
                hole_y = hubo[0][1]
        elif direc == 4:
            if target_x <= hubo[0][0]:
                hole_x = hubo[0][0]
                hole_y = hubo[0][1]
            else:
                hole_x = hubo[1][0]
                hole_y = hubo[1][1]

    
    # 이때 세 객체의 
    
    # direc에 따라 각도 변화를 다르게 주자
    b_angle = math.degrees(math.atan2((hole_x - ball_x), (hole_y - ball_y)))
    t_angle = math.degrees(math.atan2((hole_x - target_x), (hole_y - target_y)))
    cha = abs(b_angle - t_angle)
    
    print(cha)
    
    if cha < 5:
        var = 1.5
    elif cha < 10:
        var = 3
    elif cha < 15:
        var = 3.1
    elif cha < 20:
        var = 3.2
    else:
        var = 3.3
    if direc == 1: # 됐어
        if b_angle == t_angle:
            to_target_angle = math.degrees(math.atan2((target_x - ball_x), (target_y - ball_y)))
        if b_angle < t_angle:
            # b은 t의 왼쪽을 쳐라
            to_target_angle = math.degrees(math.atan2((target_x - var - ball_x), (target_y + var - ball_y)))
        else:
            # b은 t의 오른쪽을 쳐라
            to_target_angle = math.degrees(math.atan2((target_x + var - ball_x), (target_y - var - ball_y)))
    elif direc == 2:
        if b_angle == t_angle:
            to_target_angle = math.degrees(math.atan2((target_x - ball_x), (target_y - ball_y)))
        if b_angle < t_angle:
            # b은 t의 왼쪽을 쳐라
            to_target_angle = math.degrees(math.atan2((target_x - var - ball_x), (target_y - var - ball_y)))
        else:
            # b은 t의 오른쪽을 쳐라
            to_target_angle = math.degrees(math.atan2((target_x + var - ball_x), (target_y + var - ball_y)))
    elif direc == 3:
        if b_angle == t_angle:
            to_target_angle = math.degrees(math.atan2((target_x - ball_x), (target_y - ball_y)))
        if b_angle < t_angle:
            # b은 t의 왼쪽을 쳐라
            to_target_angle = math.degrees(math.atan2((target_x + var - ball_x), (target_y - var - ball_y)))
        else:
            # b은 t의 오른쪽을 쳐라
            to_target_angle = math.degrees(math.atan2((target_x - var - ball_x), (target_y + var - ball_y)))
    elif direc == 4:
        if b_angle == t_angle:
            to_target_angle = math.degrees(math.atan2((target_x - ball_x), (target_y - ball_y)))
        if b_angle < t_angle:
            # b은 t의 왼쪽을 쳐라
            to_target_angle = math.degrees(math.atan2((target_x + var - ball_x), (target_y + var - ball_y)))
        else:
            # b은 t의 오른쪽을 쳐라
            to_target_angle = math.degrees(math.atan2((target_x - var - ball_x), (target_y - var - ball_y)))


    # to_target_angle = math.degrees(math.atan2((target_x - ball_x), (target_y - ball_y)))

    angle = to_target_angle

    divi = 2.5
    multi = 1.37
    power = ((math.sqrt((hole_x - ball_x)**2 + (hole_y - ball_y)**2)) / divi) * multi
    if power < 60:
        power = 60
    print(angle, power)
    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
