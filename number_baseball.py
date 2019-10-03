u=input('enter number: ')
def calculate(j,k):
    if j==k:
        return 'you win'
        
        
    else:
        ball=0
        strike=0
        for i in range(0,3):
            if j[i]==k[i]:
                strike+=1
                    
        for i in range(0,9):
            if str(i) in j and str(i) in k:
                ball+=1
        ball-=strike
        
        if strike>=1 and ball>0:
            return f'strike:{strike}, ball:{ball}!!!'
                
        elif strike>=1:
            return f'strike:{strike}!!!'
        elif ball>0:
            return f'ball:{ball}!!!'
        else:
            return f'out!!!'
# print(calculate('2648','2648'))
from socket import *
serverSock=socket(AF_INET,SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

clientSock, addr=serverSock.accept()

    

    
    
print('<start!>\n')



num=clientSock.recv(1024)
num=num.decode(('utf-8'))
n=1
while True:
    
    st=f'{n} round, 숫자를 입력: '
    clientSock.send(st.encode('utf-8'))
    msg=clientSock.recv(1024)
    t=msg.decode(('utf-8'))
    if len(t)<=2:
        clientSock.send('다시하세요!!!'.encode('utf-8'))
        continue
    result=calculate(u,t)
        
    
              
    clientSock.send(result.encode('utf-8'))
    if 'you win'in result:
        print('you lose')
        break
    
    g=input(st)
    
    if len(g)<=2:
        print('다시하세요!!!')
        continue
    result=calculate(num,g)
        
    
              
    print(result)
    if 'you win'in result:
        print('you win')
        clientSock.send('you lose'.encode('utf-8'))
        break
    n+=1
    
    
        
print('<the_end!>')
        
            
    
