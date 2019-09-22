u=input('enter number: ')  
from socket import *
serverSock=socket(AF_INET,SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

clientSock, addr=serverSock.accept()

    
    
    



    
    
print('<start!>\n')


ball=0
strike=0
n=1
while True:
    strike=0
    ball=0
    st=f'{n} round, 숫자를 입력: '
    clientSock.send(st.encode('utf-8'))
    msg=clientSock.recv(1024)
    
    
    t=msg.decode('utf-8')
    if len(t)<=2:
        clientSock.send('다시하세요!!!'.encode('utf-8'))
        continue
    if u==t:
        clientSock.send('cleared'.encode('utf-8'))
        break
    else:
        for i in range(0,3):
            if u[i]==t[i]:
                strike+=1
                
        for i in range(0,9):
            if str(i) in u and str(i) in t:
                ball+=1
        ball-=strike
        result=''
        if strike>=1 and ball>0:
            result=f'strike:{strike}, ball:{ball}!!!'
            
        elif strike>=1:
            result=f'strike:{strike}!!!'
        elif ball>0:
            result=f'ball:{ball}!!!'
        else:
            result=f'out!!!'
        if n>=9:
            result += ' game over'
            
        clientSock.send(result.encode('utf-8'))
        if 'game over' in result:
            break
        n+=1
print('<the_end!>')
        
            
    
