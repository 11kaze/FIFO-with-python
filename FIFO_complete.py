s = list()
frame_tray = list()
print("enter no. of pages in string")
np = int(input())
print("enter page string")
i = 0
for x in range(np):
    a = int(input())
    s.insert(i,a)
    i +=1
s.insert(i,12345)    
print("enter no. of frame")
nf = int(input())
i=0
for y in range(nf):
    frame_tray.insert(i,0)
    i += 1
print(frame_tray)
m = 0
p = 0
u = 0
for z in range(np):
    if m < np:
        for x in range(nf):
            if frame_tray[u] == 0 and s[m] not in frame_tray:
                del frame_tray[u]
                frame_tray.insert(u,s[m])
                print(frame_tray,"page fault")
                u += 1
                m += 1
                p += 1
                if u == 4:
                    u = 0
            elif s[m] in frame_tray and m < np:
                print(frame_tray)
                m += 1
            elif frame_tray[u] != 0 and s[m] not in frame_tray and m < np:
                del frame_tray[u]
                frame_tray.insert(u,s[m])
                print(frame_tray,"page fault")
                u += 1
                p += 1
                m += 1
                if u == 4:
                    u = 0
    else:
        break
print("total no, of page fault are:",p)
print("thank you for using this program")            
        
        
                  
                  
                
                
        
            
            
    
    
 
