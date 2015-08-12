from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from main.models import  PinsImages
from django.db import connection
import time
import crypton.settings 
from http_common import common_encrypt, get_crypto_object

class Command(BaseCommand):
    args = ''
    help = 'reset pins for all users'
    def handle(self, *args, **options):
        Oper = User.objects.get(id=1)
        for item in PinsImages.objects.filter(status='created'):
                (Obj, Iv) = get_crypto_object(crypton.settings.CRYPTO_KEY)
                RawVal = item.raw_value
                item.raw_value = ''
                item.req_vocabulary = ''
                item.status = 'processed'
                item.save()
                item.raw_value = common_encrypt(Obj, RawVal )
                item.iv_key = Iv
                item.save(using='security')
                        
                  


              

