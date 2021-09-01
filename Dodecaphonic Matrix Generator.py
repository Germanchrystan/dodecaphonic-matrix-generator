notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

print ("Welcome to Dodecaphonic Matrix Generator.\nThis piece of code was finished by Germán Chrystan in May of 2019.\nKeep in mind this was created by a newbie, so any suggestion or critique is welcome. Contact me at germanchrystan@gmail.com.\n \nATTENTION: This software only reads alterations in the form of sharp notes (not flat).\n If you introduce ¨Bb¨ for instance, the software won´t read it. Write all notes in Upper case, and in the case of sharp notes write the # simbol right next to the name of the note (for example use ¨C#¨for C sharp)\n \n\n \n")  

def gen_():#this function ask the user to input one note at a time
    s = []
    while len(s)!=12:
        in_ = input("Input the note number " + str(len(s)+1) + ", please\n", )
        if in_ in notes and in_ not in s:
          s.append(in_)
          print(" \n"+str(s)+"\n " )
        else:
          print("Input not valid, try again\n ")
    if len(s)==12:
      return s
result=gen_()


def pitch(): #This function returns the values of each note
  a=result[0]
  c=notes[notes.index(a):]+notes[0:notes.index(a)]#Creates a chromatic scale that starts with the first note of the original row
  i=0
  e=[]
  while i !=12:
      f=c.index(result[i])
      e.append(f)
      i=i+1
      
  return e
  
pitchresult=pitch()

def addspacetopitch():
  global pitchresult
  addspace=[]
  for x in pitchresult:
    if len(str(x))==1:
      x=" "+str(x)
    elif len(str(x))==2:
      x=""+str(x)
    addspace.append(x)
  print(str("  ")+ str(addspace))

def addspace():
  addspace=[]
  for x in result:
    if len(x)==1:
      x=" "+x
    addspace.append(x)
  print(str(" 0")+ str(addspace))



def rows():    #This function returns the value of each of the rows below the original 
  f=[]
  i=1
  while len(f)!=11:
    e=12-pitchresult[i]
    f.append(e)
    i=i+1
  return f    

rowsresult=rows()

def originalchromatic():
    fn=result[0]
    ocr=notes[notes.index(fn):]+notes[0:notes.index(fn)]
    return ocr 

ocr=originalchromatic()

def chromatic():#this function creates a chromatic scales over each note of the row, so that it can be used to create the dodecaphonic rows of the matrix. Then, it uses each chromatic scale to create each row.
  for x in rowsresult:
    chromaticscales=ocr[x:]+ocr[0: x]
    num=str(x)
    if len(str(num))==1:
      num=" "+str(num)
    f=[]
    for x in pitchresult:
      csrx=chromaticscales[x]
      if len(csrx)==1:
        csrx=" "+csrx
      f.append(csrx)
  
    print(str(num)+str(f))

addspacetopitchresult=addspacetopitch()     
addspaceresult=addspace()
chromaticresult=chromatic()