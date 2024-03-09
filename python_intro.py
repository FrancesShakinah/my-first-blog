print('Hello, Django girls!')
if 3>2:
    print('It works!')
if 5>2:
    print('5 is indeed greater then 2')
else:
    print('5 is not greater than 2')   

name = 'Olaf'
if name == 'Kinah':
    print('Hello Kinah')
elif name == 'Frances':
    print('Hey Frances!')
else:
    print('Hello anonymous')

volume = 57
if volume < 20:
    print("It's kinda quite.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :( ")

#Change the volume if it's too loud or too quite
if volume < 20 or volume > 80:
    volume = 50
    print("That's better")

#new example
def hi():
    print('Hi there!')
    print('How are you?')

hi()

#new
def hi(ngalan):
    if ngalan == 'Bebens':
        print('Hello Bebens')
    elif ngalan == 'Nenek':
        print('HELLOOO NENEEEEKKK')
    else:
        print(f'Hello {ngalan}')

hi("Nenek")

#new again

def hi(pangngalan):
    print('Hi '+pangngalan+ '!')

hi("Nenek")

#new new
#girls = ['Frances', 'Levi', 'Grace', 'Monica']
#for name in girls: 

def hi(mena):
    print('Hi ' +mena+ '!')

girls = ['Frances', 'Levi', 'Grace', 'Monica']
for mena in girls:
    hi(mena)
    print('Next girl')

#new new new
for i in range(1,6):
    print(i)