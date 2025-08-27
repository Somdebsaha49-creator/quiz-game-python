import numpy as np
ques={
    'A' : 'A train 120 m long passes a pole in 12 seconds. What is its speed in km/h? (Marks:- 5)',
    'B' : 'Which country is known as the "Land of the Rising Sun"? (Marks:- 10)',
    'C' : 'If MANGO is coded as 51347 and APPLE as 15528, how will PEAR be coded (Marks:- 15)',
    'D' : 'Which data structure works on the principle of FIFO (First In, First Out)? (Marks:- 20)',
    'E' : 'Who was the first President of independent India? (Marks:- 25)',
    'F' : "Which gas is most abundant in Earth's atmosphere? (Marks:- 30)",
    'G' : 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I? (Marks:- 35)'
}
print(ques)
print('')
print("From 'A' to 'G', choose any one of the alphabets, to solve the desired quiz questions, remember dont choose the same alphabet twice")
li=[]
c=0
a1=a2=a3=a4=a5=a6=a7=0
for i in range (1,8):
    a=input("Enter a desired Alphabet from 'A' to 'G' :- ").upper()
    for j in li:
        if a == j:
            print('Sorry Dear, you have already choose this alphabet once, try another one')
            c=1
    if c == 0:
        if a == 'A':
            print('Congratulations you have chosen:-')
            print('')
            print(ques[a])
            b=input('You Answer Please (in km/h):- ')
            if b == '36 km/h':
                a1=5
            else:
                a1=0
        elif a == 'B':
            print('Congratulations you have chosen:-')
            print('')
            print(ques[a])
            b=input('You Answer Please:- ')
            if b == 'Japan':
                a2=10
            else:
                a2=0
        elif a == 'C':
            print('Congratulations you have chosen:-')
            print('')
            print(ques[a])
            b=input('Your Answer Please:- ')
            if b == '5 8 1 _':
                a3=15
            else:
                a3=0
        elif a == 'D':
            print('Congratulations you have chosen:-')
            print('')
            print(ques[a])
            b=input('Your Answer Please:- ')
            if b == 'Queue':
                a4=20
            else:
                a4=0
        elif a == 'E':
            print('Congratulations you have chosen:-')
            print('')
            print(ques[a])
            b=input('Your Answer Please:- ')
            if b == 'Dr. Rajendra Prasad':
                a5=25
            else:
                a5=0
        elif a == 'F':
            print('Congratulations you have chosen:-')
            print('')
            print(ques[a])
            b=input('Your Answer Please:- ')
            if b == 'Nitrogen':
                a6=30
            else:
                a6=0
        elif a == 'G':
            print('Congratulations you have chosen:-')
            print('')
            print(ques[a])
            b=input('Your Answer Please:- ')
            if b == 'Echo':
                a7=35
            else:
                a7=0
    li.append(a)
    c=0
x=np.array(['A','B','C','D','E','F','G'])
y=np.array([a1,a2,a3,a4,a5,a6,a7])
me=np.mean(y)
print('')
print('Mean Score of Player is ',me)
print('')
import matplotlib.pyplot as plt
plt.bar(x,y,color=['red','green','blue','violet','pink','orange','purple','black'],width=0.5)
plt.title('Player Quiz Score Bar Graph')
plt.show()