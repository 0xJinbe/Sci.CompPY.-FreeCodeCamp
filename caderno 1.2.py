

#função com return

def quantidade_de_letras(palavra):
    quantidade = len(palavra)
    return quantidade
a = input('Digite uma palavra...     ')
b = input('Digite outra palavra...     ')

if quantidade_de_letras(a) > quantidade_de_letras(b):
    print
    'A menor palavra e ', b
elif quantidade_de_letras(a) == quantidade_de_letras(b):
    print
    'As duas palavras tem a mesma quantidade de letras'
else:
    print
    'A menor palavra e ',

sair = input('Tecle <ENTER> para encerrar...')

###############################################################################################################

# This is a really basic User Login Interface that may be slapped into another
# script that fuctions differently for different users. Security and other features
# could be plugged in.
#
# Rob Andrews
# rob@jam.rr.com

# Dictionary of UserIDs and their Passwords
pwds = {"guest":"anonymous", "rob":"deadparrot", "root":"spam"}
# Maximum number of login attempts set.
# maxlogin = input("Please specify the maximum number of allowed logins for this session. ")
maxlogin = 3
# UserId and Password are requested from the user a maximum number of times.
loginattempts = 0
while loginattempts < maxlogin:
	loginattempts = loginattempts + 1
	userid = input("Please enter your UserID: ")
	password = input("Please enter your Password: ")
	# If the UserID supplied by the user appears in the pwds dictionary,
	# test to see if the corresponding password is correct.
	if pwds.fromkeys(userid):
		if password == pwds[userid]:
			print("Consider yourself logged in!")
			break
		else:
			print("Your pathetic login attempt has failed!" )
	else:
		print("You appear to be ontologically challenged." )
input("Press [Enter] to end this session.\nIf you do not have a UserID,\ntry 'guest' with a Password of 'anonymous' next time. >")
