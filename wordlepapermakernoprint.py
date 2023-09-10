import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
myFont = ImageFont.truetype('C:\WINDOWS\FONTS\CONSOLA.TTF', 24)

import random
times = int(input("put the number of wordles to be generated here, input 1 to specify the word:"))
word = ""
if times == 1:
  word = input("place word here:")
else:
  file = open("resources/5letterwords.txt","r")
  words = file.read()
  words = words.split("\n")
  file.close()
scramble = input("put 1 number the wordles made, 2 to title the image the word:")
chars = "abcdefghijklmnopqrstuvwxyzбджилцчщф"
for p in range(times):
  img = Image.open('resources/template.png')
  I1 = ImageDraw.Draw(img)  
  if times != 1:
    word = random.choice(words)
  endletters = {"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[],}
  for j in range(6):
    templetters = {"a":"","b":"","c":"","d":"","e":"","f":"","g":"","h":"","i":"","j":"","k":"","l":"","m":"","n":"","o":"","p":"","q":"","r":"","s":"","t":"","u":"","v":"","w":"","x":"","y":"","z":"",}
    bannednumbers = []
    bannedletters = ""
    letters = []
    count = 0
    for i in word:
      if i not in letters:
        letters.append(i)
        count += 1
    while len(bannednumbers) != 5:
      if word[len(bannednumbers)] not in word[:len(bannednumbers)]:
        tempnum = random.randrange(6,32)
        if tempnum not in bannednumbers:
          bannednumbers.append(tempnum)
      else:
        bannednumbers.append(bannednumbers[word.find(word[len(bannednumbers)])])
    while len(bannedletters) != 5:
      templetter = random.choice(chars)
      if templetter not in bannedletters:
        bannedletters+=templetter
    printedletters = ""
    while len(printedletters) != 5:
      letter2 = random.choice(bannedletters)
      if letter2 not in printedletters:
        #print(letter2,end = "")
        printedletters += letter2
    spacer = 0
    if j>3:
      spacer = 20
    I1.text((800, 270+(222*j)+spacer), printedletters, font=myFont, fill =(0, 0, 0))
    #print("")
    #print(bannednumbers,end = "")
    #print("   ",end = "")
    number2l = []
    for i in range(len(bannednumbers)):
      number3 = bannednumbers[i]
      chosen = 0
      while chosen == 0:
        number2 = random.randrange(6,36)
        if number2 not in [number3-5,number3-4,number3-3,number3-2,number3-1,number3,number3+1,number3+2,number3+3,number3+4,number3+5] and number2-number3 not in [-1,-2,-3,-4,-5,1,2,3,4,5] and number2 not in number2l:
          chosen = 1
          number2l.append(number2)
      if number2 > number3:
        equation = (str(number2)+"-"+str(number2-number3))
        #print(equation,end = "")
      if number2 < number3:
        equation = (str(number2)+"+"+str(number3-number2))
        #print(equation,end = "")
      I1.text((360+(217*i), 320+(222*j)+spacer), equation, font=myFont, fill =(0, 0, 0))
      #print("  ", end = "")
    #print("")
    for k in range(len(word)):
      space = ""
      if len(str(bannednumbers[k])) == 1:
        space = " "
      templetters[word[k]] = bannedletters[k] + " " + str(bannednumbers[k]) + space
    for i in range(26):
      if templetters[chars[i]] == "":
        numberfound = 0
        letterfound = 0
        while numberfound == 0:
          number = random.randrange(6,32)
          if number not in bannednumbers:
            numberfound = 1
        while letterfound == 0:
          letter = random.choice(chars)
          if letter not in bannedletters:
            letterfound = 1
        space = ""
        if len(str(number)) == 1:
          space = " "
        templetters[chars[i]] = letter+" "+str(number) + space
        bannedletters += letter
        bannednumbers.append(number)
    for i in range(26):
      endletters[chars[i]].append(templetters[chars[i]])
  for k in range(6):
    for i in range(26):
          #print(endletters[chars[i]][k]," ",end = "")
          I1.text((25+(64*i), 1972+(31*k)), endletters[chars[i]][k], font=myFont, fill =(0, 0, 0))
    #print("")
  for i in range(26):
    #print(chars[i]+"     ",end="")
    pass
  if scramble == "1":
    img.save(str(p+1)+".png")
  else:
    img.save(word+".png")
