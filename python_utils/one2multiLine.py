import sys  
  
fp = open (sys.argv[1], 'r')   
fp_dis = open (sys.argv[2], 'w')  
tnum = 0  
for buffer in fp :  
    print (len(buffer))  
    for buf in buffer :  
        if ( buf == '{' ) :  
            fp_dis.write("\n" + "\t" * tnum)  
            tnum+=1  
            fp_dis.write(buf + "\n" + "\t" * tnum)  
        elif ( buf == ';' ) :  
            fp_dis.write(buf + "\n" + "\t" * tnum)  
        elif ( buf == '}' ) :  
            tnum-=1  
            fp_dis.write("\n" + "\t" * tnum + buf + "\n" + "\t" * tnum)  
        else :  
            fp_dis.write(buf)  
fp.close()  
fp_dis.close() 