

from django.shortcuts import HttpResponse
from django.core.mail import EmailMessage

import random


def meramail(request):
    otp =random.randrange(111111,999999)
    user_mail=['shuklashubham728@gmail.com',
               'raj.django@gmail.com',
               'rmbbd0077@gmail.com'
            ]
    m =EmailMessage('Verification',f'Your otp is {otp} ',to=user_mail)
    m.send()
    a="mail send"
    return HttpResponse(a)
