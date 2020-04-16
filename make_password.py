#!/usr/bin/env python3

import fileinput
import os
import platform
import secrets

def addToClipBoard(text):
  if platform.system() == "Linux":
    command = 'echo -n "{}" | xclip -selection c'.format(text.strip())
  else:
    command = 'echo | set /p nul=' + text.strip() + '| clip'
  os.system(command)

print( "Is pseudorandomization ok? (yes/no)" )
print( "> ", end='')

fin = fileinput.input()

pseudorandom = next(fin).lower().startswith( "y" )

if pseudorandom:
  line = ""
  for _ in range(30):
    line += str( secrets.randbelow(6)+1 )
else:
  print( "Please provide random 30 dice:" )
  print( "https://www.random.org/dice/" )
  line = next(fin)
  line = line.replace( " ", "" ).strip()

print( "using {} numbers".format( len(line) ) )
print( line )

result = ""

while( len(line) >= 5 ):
  piece = line[:5]
  line = line[5:]

  with open( "eff_large_wordlist.txt", 'r' ) as words_in:
    for words_line in words_in:
      if words_line.startswith( piece ):
        word = words_line.split( "\t" )[1]
        result += " " + word.strip()
	 

print( "Password:" + result )


addToClipBoard(result)


print( "The password is on your clipboard" )
