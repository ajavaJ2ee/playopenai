import re


def securefilename(filename):

    #expresssion1='^[A-z\_]+[A-z\(]+[A-z\-]+[0-9\_]+[0-9\-]+(com|net)'
    #expresssion2 = '^[A-z\_]+[A-z\(]+[A-z\-]+[0-9\_]+[0-9\-]+[0-9\.]+(jpg|jpeg|png|gif)'
    expresssion3='^[a-zA-Z0-9][a-zA-Z0-9_()-.]*(jpg|jpeg|png|gif)'
    return re.match(expresssion3,filename) is not None

filename1='abhi932525-sai_pooja.jpg'
result= securefilename(filename1)
filename2='H(e-llo_05645.gif'
result= securefilename(filename2)
filename3='H(e-llo_05)645.jpg'
result= securefilename(filename3)

print(result)