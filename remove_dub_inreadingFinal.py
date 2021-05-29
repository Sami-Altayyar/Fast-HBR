import os
import sys
import gzip
import threading
import menu


#======================================test without reverse
def remove_se_fastq_norev(filename1,outfile1):
# Remove from fastq file paire end
    #hashs = set()
    count = 0
    subs = 0
    f = open(filename1, "r")
    fo = open(outfile1 , "w")
    hashsarr=[set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
    #fremoved = open(removedfile , "w")
    #t={84: 65, 65: 84, 71: 67, 67: 71}
    while True:
        h1= f.readline()
        s1 = f.readline()
        q1 = f.readline()
        p1 = f.readline()
        if h1:
            temphash = hash (s1 )
            ind=temphash % 10
            if temphash in hashsarr[ind]: # hashs:
                subs += 1
            else:
                hashsarr[ind].add (temphash) #hashs.add(temphash)
                fo.write(h1 + s1 +  q1  + p1  )
                count = count + 1
        else:
            break


    f.close()
    fo.close()
    #fremoved.close()
    return count,subs


#===========================================================

def remove_se_fastq(filename1,outfile1):
# Remove from fastq file paire end
    #hashs = set()
    count = 0
    subs = 0
    f = open(filename1, "r")
    fo = open(outfile1 , "w")
    hashsarr=[set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
    #fremoved = open(removedfile , "w")
    t={84: 65, 65: 84, 71: 67, 67: 71}
    while True:
        h1= f.readline()#.rstrip()
        s1 = f.readline().rstrip()
        q1 = f.readline()#.rstrip()
        p1 = f.readline()#.rstrip()
        if h1:
            temphash = hash (s1 )
            ind=temphash % 10
            if temphash in hashsarr[ind]: # hashs:
                subs += 1
            else:
                rev1=s1[::-1].translate(t)
                temphash2 =  hash(rev1 )
                ind2=temphash2 % 10
                if temphash2 in hashsarr[ind2]: # hashs:
                    subs += 1
                else:
                    #hashs.add(temphash)
                    hashsarr[ind].add (temphash)
                    fo.write(h1 + s1  + "\n" + q1  + p1  )
                    count = count + 1
        else:
            break


    f.close()
    fo.close()
    #fremoved.close()
    return count,subs




#2 files PE without reverse complement
def remove_pe_twofiles(filename1,filename2,outfile1,outfile2):
# Remove from fastq file paire end 
    #hashs = set()
    count = 0
    subs = 0
    #t={84: 65, 65: 84, 71: 67, 67: 71}
    f=open(filename1,"r")
    f2=open(filename2, "r")
    fo = open(outfile1 , "w")
    fo2 = open(outfile2 , "w")
    hashsarr=[set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]

    p=0
    while True: 
    	h1= f.readline()
    	s1 = f.readline().rstrip()  
    	q1 = f.readline()
    	p1 = f.readline()
    	h2= f2.readline()
    	s2 = f2.readline().rstrip()  
    	q2 = f2.readline()
    	p2 = f2.readline() 
    	if h1:
    	    # rev=s1[::-1].translate(t)
    	    # rev2=s2[::-1].translate(t)
    	    #temphash2 =  hash(rev )+ hash(rev2 )       
    	    temphash = hash (s1 ) +  hash (s2 )   
    	    ind=temphash % 10


    	    if temphash in hashsarr[ind]:#hashs:# or  temphash2 in hashs: #finalhash1 in hashs or finalhash2 in hashs: if temphash in hashs:# or  temphash2 in hashs: #finalhash1 in hashs or finalhash2 in hashs:
    	        subs += 1
    	    else:
#    	        hashs.add(temphash) #finalhash1)
    	        hashsarr[ind].add(temphash)
    	        fo.write(h1 + s1 + "\n" + q1 + p1 )           
    	        fo2.write(h2 + s2 + "\n" + q2 + p2 )                    
    	        count = count + 1
    	else:
    	    break

    f.close()
    f2.close()
    fo.close()
    fo2.close()
    return count,subs




#888888888888888888888888888888888888  concatinate reads
#2 files PE without reverse complement
def remove_pe_twofiles_norev_con(filename1,filename2,outfile1,outfile2):
# Remove from fastq file paire end
    #hashs = set()
    count = 0
    subs = 0
    f=open(filename1,"r")
    f2=open(filename2, "r")
    fo = open(outfile1 , "w")
    fo2 = open(outfile2 , "w")

    hashsarr=[set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
    p=0
    while True:
        h1= f.readline()
        s1 = f.readline().rstrip()
        q1 = f.readline()
        p1 = f.readline()
        h2= f2.readline()
        s2 = f2.readline().rstrip()
        q2 = f2.readline()
        p2 = f2.readline()
        if h1:
            s= (s1 + s2 )
            temphash =hash (s)  #hash (s1 ) -  hash (s2 ) # hash (s)
            ind=temphash%10
            if temphash in hashsarr[ind]:#hashs:# or  temphash2 in hashs: #finalhash1 in hashs or finalhash2 in hashs:
                subs += 1
            else:
                #hashs.add(temphash) #finalhash1)
                hashsarr[ind].add(temphash)
                fo.write(h1 + s1 + "\n" + q1 + p1 )

                fo2.write(h2 + s2 + "\n" + q2 + p2 )
                count = count + 1
        else:
            break

    f.close()
    f2.close()
    fo.close()
    fo2.close()
    return count,subs
#888888888888888888888888888888888888  concatinate reads







app = menu.CommandLine()

#print (app.filetype)
#print (app.filelist)


#filename1 = sys.argv[1]
#filename2 = sys.argv[2] 

if app.filetype==1:
    if app.rev:
        c,s=remove_se_fastq(app.filelist[0],app.filelist[0]+"_Uniqe")
    else:
        c,s=remove_se_fastq_norev(app.filelist[0],app.filelist[0]+"_Uniqe")
if app.filetype==2:
    if app.rev:
        c,s=remove_pe_twofiles(app.filelist[0],app.filelist[1],app.filelist[0]+"_Uniqe",app.filelist[1]+"_Uniqe")
    else:
        c,s=remove_pe_twofiles_norev_con(app.filelist[0],app.filelist[1],app.filelist[0]+"_Uniqe",app.filelist[1]+"_Uniqe")


#fname, fext = os.path.splitext(filename1 )
#base=os.path.basename(filename1)
#if fext == ".gz":
#   filetype="rt"
#   ext= fname, fext = os.path.splitext(filename1[:len(filename1)-3] )
#else:
#   filetype="r"
#   ext=fext








#Two Files PE creating output files names
#outfile1 = base[:len(filename1)-len(ext)] + "_1Final" + ext
#outfile2 = base[:len(filename1)-len(ext)] + "_2Final" + ext

#c,s=remove_pe_twofiles_norev(filename1,filename2,outfile1,outfile2)


print ("total reads")
print (c + s)
print ("non redundent reads")
print (c)
