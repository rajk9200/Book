# for i in range(5+1):
# # # #     for j in range(i):
# # # #         print("*", end="")
# # # #     print()
# # # #
# # # # # *
# # # # # **
# # # # # ***
# # # # # ****
# # # # # *****




# for i in range(5):
#     a=0
#     for j in (range(i)):
#         print(a, end=" ")
#         if a==0:
#             a=1
#         elif a==1:
#             a=0
#
#     print()
#

#party me bahar ke log allow nhi hai?
# 0
# 0 1
# 0 1 0
# 0 1 0 1

# for i in range(1,10+1):
#     for j in range(1,10+1):
#         i=i+1
#         print(i,end="")
#     print()


import pandas as pd
import pyqrcode
# text='helo'
# image =pyqrcode.create(text)
# image.svg('Qr.svg', scale='4')




def createQRCode():
    df = pd.read_csv('d.csv')
    # for index,values in df.iterrows():
    #     print(index,values)
    #     text=f"""
    #
    #     name {index}
    #
    #     """
    image =pyqrcode.create(str(df))
    image.svg('Qr.svg', scale='4')

createQRCode()




