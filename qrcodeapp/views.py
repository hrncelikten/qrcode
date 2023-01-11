# qrcodeapp/views.py

from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from pathlib import WindowsPath

def qr_gen(request):
    if request.method == 'POST':
        data = request.POST['data']
        img = make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        media_root = WindowsPath(settings.MEDIA_ROOT)
        path = media_root.joinpath(img_name)
        img.save(path)
        # img.save(settings.MEDIA_ROOT + '/' + img_name)
        # qr = QRCode(
        #     version=1,
        #     error_correction=ERROR_CORRECT_L,
        #     box_size=50,
        #     border=2,
        # )
        # qr.add_data(data)
        # img_name = 'qr' + str(time.time()) + '.png'
        # img=qr.make_image(fill_color="black", back_color="white")
        img.save("media" + '/' + img_name)
        return render(request, 'index.html', {'img_name': img_name})
    return render(request, 'index.html')