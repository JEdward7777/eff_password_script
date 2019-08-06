import fileinput
print( "Please provide random 30 dice:" )
print( "https://www.random.org/dice/" )

line = next(fileinput.input())

line = line.replace( " ", "" )

result = ""

while( len(line) > 5 ):
  piece = line[:5]
  line = line[5:]

  with open( "eff_large_wordlist.txt", 'r' ) as words_in:
    for words_line in words_in:
      if words_line.startswith( piece ):
        word = words_line.split( "\t" )[1]
        result += " " + word.strip()
	 

print( "Password:" + result )