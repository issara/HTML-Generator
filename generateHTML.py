from random import *
import time

def main():
	
	#output three test html files
	generateHTML('config1.txt','hw1_example1.html') 
	generateHTML('config2.txt','hw1_example2.html')
	generateHTML('config3.txt','hw1_example3.html')

def generateHTML(readfile,outfile):
	
	config = open(readfile, 'r')
	
	BODY_BACKGROUND=getInfo(config.readline()) #first line is background color
	CELL_BACKGROUND1=getInfo(config.readline()) #next line is cell background1
	CELL_BACKGROUND2=getInfo(config.readline()) #next line is cell background2
	TABLE_BORDER_COLOR=getInfo(config.readline()) #next line is table border
	TABLE_BORDER_PX=getInfo(config.readline()) #next line is table border thickness
	AUTHORS=getInfo(config.readline()) #next line is authors
	TITLE=getInfo(config.readline()) #next line is the title
	CONTENT=config.readline() #will either be "IMAGES" or "LETTERS"
	
	outString='<html>\n<head>\n'
	
	bodyString='body {background-color:'+BODY_BACKGROUND+';}\n'
	outString=outString+'<style type="text/css">\n'
	outString=outString+bodyString
	outString=outString+'.odd {background-color: '+CELL_BACKGROUND1+';}\n'
	outString=outString+'.even {background-color: '+CELL_BACKGROUND2+';}\n'
	outString=outString+'td {border: '+TABLE_BORDER_PX+'px solid '+TABLE_BORDER_COLOR+';\n'
	outString=outString+'text-align: center;}\n'
	outString=outString+'table {width: 60%; border-collapse: collapse;}\n'
	outString=outString+'h2 {font-size: 14;}\n'
	outString=outString+'img { width: 100; height: 100;}'
	
	outString=outString+'</style>\n'
	outString=outString+'</head>'
	outString=outString+"<body>"
	outString=outString+"<center>"
	outString=outString+wrap("<h1>",'~ '+TITLE+' ~')
	
	

	if (CONTENT=='LETTERS\n'):
		SIZE=config.readline() #size of table in row X column
		
		outString=outString+letterTable(SIZE)
	
	elif (CONTENT=='IMAGES\n'):
		outString=outString+imageTable(config) #run table of images
		
	
	else: #if line does not read 'LETTERS' or 'IMAGES'
		outString=outString+'<img src="images/cam1.png"/>' #a picture to make user happy
		oops="Sorry, I don't know what you want to see here." #error message
		outString=outString+wrap("<h3>",oops)
	
	
	
	mytime=time.localtime()
	year=str(mytime[0])
	month=str(mytime[1])
	date=str(mytime[2])
	hour=str(mytime[3])
	min=str(mytime[4])
	days=['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']
	day=days[mytime[6]] #get day of week in string form
	
	timeString=day+'day, '+month+'/'+date+'/'+year+' at '+hour+':'+min+' Army time'
	outString=outString+wrap('<h2>','Created automatically on '+timeString)
	outString=outString+wrap('<h2>',"Authors: "+AUTHORS)
	outString=outString+"</center>"
	outString=outString+'\n</body>\n</html>'
	
	file = open(outfile, 'w')
	file.write(outString)
	
	
def letterTable(SIZE): #for random letter output
	rByC=SIZE.split('x')
	numRows=eval(rByC[0]) #number of rows
	numCols=eval(rByC[1]) #number of columns
	
	total=numRows*numCols #total number of cells
	randLetters=randomLetters(total)
	count=0
	outString='<table>\n'
	
	for r in range(numRows):
		outString=outString+'<tr>\n'
		for c in range(numCols):	
			if (r+c)%2==0: #even. use even class
				par="even"	#parity is even. use even cell class
			else:
				par="odd"
			
			letter=randLetters[count]
			outString=outString+wrap('<td class='+par+'>',letter)
			count=count+1
		outString=outString+'</tr>\n' #end row
	

	outString=outString+'</table>\n'
	return outString
	
def imageTable(file): #for table of selected images

	rows=[]
	curRow=file.readline()
	outString='<table>\n'
	rowNum=0
	while curRow != '': #until row is blank
	
		images=curRow.split('\t') #image names separated by tabs
		rowString=''
		for i in range(len(images)):
			im=images[i]
			if ((rowNum+i)%2==0):
				par='even' #parity is even. use even cell class
			else:
				par='odd'
			rowString=rowString+wrap('<td class='+par+'>','<img src="images/'+im+'"/>')
		
		outString=outString+wrap('<tr>',rowString) #end row
		curRow=file.readline() #get next row of images
		rowNum=rowNum+1
	
	outString=outString+'</table>\n'
	return outString
	
def wrap(tag,string):

	endTag='</' #beginning of end tag
	for i in range(1,len(tag)-1): #look inside < >
		char=tag[i]
		if char==' ': #chop off at space
			break
		endTag=endTag+char
	
	return tag+string+endTag+'>\n'
	
def getInfo(string): #gets the information of row (usually a color) from config
	items=string.split('\t')
	info=items[1][:-1] #second  word is the info, chop off \n
	return info
	
def randomLetters(num): #outputs a list of num random letters (num<52)
	sortedLetters=[] #letters in alphabetical order
	
	letterNum=ord('A')
	for i in range(26): #add 26 capital letters
		sortedLetters.append(chr(letterNum))
		letterNum=letterNum+1
	
	letterNum=ord('a')
	for i in range(26): #add 26 lowercase letters
		sortedLetters.append(chr(letterNum))
		letterNum=letterNum+1
	
	randomLetters=[]
	for i in range(num):
		r=randrange(num-i) #number of letters left goes down by 1 each time
		letter=sortedLetters[r] #take letter and random index
		randomLetters.append(letter)
		sortedLetters.remove(letter) #remove this letter so we dont pick it again
	
	return randomLetters
	


main()