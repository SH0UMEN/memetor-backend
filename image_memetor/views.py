from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Image, Mem
import json
from django.core.files.images import ImageFile
from PIL import Image as PILImage, ImageDraw, ImageFont, ImageColor
from vue_django_app.settings import STATICFILES_DIRS, BASE_DIR
import os


def allImages(request):
    ims = Image.objects.all()
    response = {}
    for i in ims:
        response[i.pk] = 'http://{}/{}'.format(request.get_host(), i.image.url)
    return JsonResponse(response)


def allMemes(request):
    memes = Mem.objects.all()
    response = {
        'memes': []
    }
    for i in memes:
        url = os.path.relpath(i.image.path, start=BASE_DIR)
        response['memes'].append('http://{}/{}'.format(request.get_host(), url))
    return JsonResponse(response)


@csrf_exempt
def createMem(request):
    if (request.method == 'POST'):
        req = json.loads(request.body.decode('UTF-8'))

        image = Image.objects.get(pk=req['image'][0]).image.path
        base = PILImage.open(image).convert('RGBA')

        k = base.size[0] / int(req['current-width'])

        txt = PILImage.new('RGBA', base.size, (255, 255, 255, 0))

        d = ImageDraw.Draw(txt)

        for te in req['textElems']:
            fnt = ImageFont.truetype(os.path.join(STATICFILES_DIRS[0], 'fonts/micross.ttf'),
                                     int((int(te['fontSize'])) * k))
            d.text((te['left'] * k, te['top'] * k), te['text'], font=fnt, fill=ImageColor.getrgb(te['color']))

        pathToImage = os.path.join(STATICFILES_DIRS[0], 'memes/mem.png')
        out = PILImage.alpha_composite(base, txt)
        out.save(pathToImage)
        mem = Mem(image=ImageFile(open(pathToImage, 'rb')))
        mem.save()
        os.remove(pathToImage)
        return JsonResponse(req)
