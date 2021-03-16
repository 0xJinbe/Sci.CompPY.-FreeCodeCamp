#manipulando arquivos

#ex1: file handle as a sequence

#xfile = open('mbox.txt')
#for cheese in xfile:
#print(cheese)

#ex2: counting lines in a file
#fhand = open('mbox.txt')
#count = 0
#for line in fhand:
#    count = count + 1
#print('Line count:', count)

#reading the whole file

#fhand = open('mbox-short.txt')
#inp = fhand.read()
#print(len(inp))
#print(inp[:20])

#reading atraves de arquivo, tirando whitespace noise e usando continue

#fhand = open('mbox-short.txt')
#for line in fhand:
#   line = line.rstrip()
#   if not line.startswith('From: '):
#       continue
#   print(line)
