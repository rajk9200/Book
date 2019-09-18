# import random
# import string
#
# def gn_pass(a=6):
#     p_var = ''.join([random.choice(string.ascii_uppercase +
#                                    string.digits
#
#
#                                    )
#                     for i in range(a)])
#     return p_var
#
#
# print(gn_pass())
#

# v=[]
# uv='920017831'
# for i in range(len(uv)):
#     if i<2 or i==7 or i==8:
#         print(uv[i],end='')
#     else:
#         print('*',end="")
#         v.append(uv[i])
#
# print('')
# for m in v:
#     print(m, end='')



class Remote:
    def __int__(self):

        self.plus=0
        self.speed=0

        return self.speed
    def Up(self):
        self.speed =self.speed +1
        return self.speed
    def Down(self):
        self.speed = self.speed - 1
        return self.speed



class Tv(Remote):

    def __int__(self):
        self.tvname=''

    def showTv(self):
        return self.tvname

t =Tv()
t.tvname='Plazma Tv'
print(t.showTv())

t.speed=200
while(True):
    ch=input('Enter choice=')

    if ch=='0':
        print('bye bye')
        break
    elif(ch=='+'):
        t.Up()
        print(t.speed)
    elif (ch == '-'):
        t.Down()
        print(t.speed)










