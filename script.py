import sys ,os
def Final(path):
	text=["'Siha","' :{'Titre' :'"," ','source' : '","','resume' : ' ','contenu' : '","'},"]
	newPath2=path+".txt"
	newPath3=newPath2+".txt"
	inputfile=open(path,'r')
	outputfile=open(newPath2,'w')
	mytext=inputfile.readlines()
	outputfile.write(text[0])
	
	i=1
	for line in mytext:
		if i<=3:
			outputfile.write(text[i])
			outputfile.write(line)
		if i>3:
			line=line.replace('\n','<br/> ').replace('\r','<br/> ')
			outputfile.write(line)
		i=i+1
	
	outputfile.write(text[4])
	outputfile.close()
	inputfile.close()
	return newPath2
	

def browseDir(dirPath):
	n=0
	directory = os.listdir(dirPath)
	if dirPath[len(dirPath)-1] != '/':
		dirPath=dirPath+'/'
	for file in directory:
		if file[0]!=".":
			path=dirPath+file
			if os.path.isdir(path):
				browseDir(path)
			else:
				txt2HTML(Final(path)) 

def txt2HTML(pathFile):
	new=open(pathFile,'r')
	transform=new.read()
	transform=transform.replace('\n','<br/> ').replace('\r','<br/> ')
	
	final.write(transform)
	
	new.close()


newPath4="C:/Users/elie-_000/Desktop/hv.txt"
final=open(newPath4,'w')
x=1
close =False
while(close=False):
        if len(sys.argv)==2:
	path=sys.argv[1]
        else:
                path=input("please enter a path")
        if os.path.isdir(path):
                n=browseDir(path)
        else:
                txt2HTML(Final(path))
        rep=input("Do you whant to continue yes: y   no: n")
        if(rep=="no"):
                close=True
                final.close()
        x=x+1
        

	
