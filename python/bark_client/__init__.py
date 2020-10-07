import requests
import json
from bark_client.utils import logger


class SoundType(object):
    ALARM = 'alarm'
    ANTICIPATE = 'anticipate'
    BELL = 'bell'
    BIRDSONG = 'birdsong'
    BLOOM = 'bloom'
    CALYPSO = 'calypso'
    CHIME = 'chime'
    CHOO = 'choo'
    DESCENT = 'descent'
    ELECTRONIC = 'electronic'
    FANFARE = 'fanfare'
    GLASS = 'glass'
    GOTOSLEEP = 'gotosleep'
    HEALTHNOTIFICATION = 'healthnotification'
    HORN = 'horn'
    LADDER = 'ladder'
    MAILSEND = 'mailsend'
    MINUET = 'minuet'
    MULTIWAYINVITATION = 'multiwayinvitation'
    NEWMAIL = 'newmail'
    NEWSFLASH = 'newsflash'
    NOIR = 'noir'
    PAYMENTSUCCESS = 'paymentsuccess'
    SHAKE = 'shake'
    SHERWOODFOREST = 'sherwoodforest'
    SPELL = 'spell'
    SUSPENSE = 'suspense'
    TELEGRAPH = 'telegraph'
    TIPTOES = 'tiptoes'
    TYPEWRITERS = 'typewriters'
    UPDATE = 'update'


class BarkClient(object):

    def __init__(self, domain, key_list):
        self.domain = domain
        self.key_list = key_list

    def get_request_url(self, content, key, title=None,
                        url=None, sound=None, automatically_copy=False):
        result = 'https://{domain}/{key}'.format(domain=self.domain, key=key)
        if title:
            result += '/{title}'.format(title=title)

        result += '/{content}?automatically_copy={automatically_copy}'.format(
            base_url=result,
            content=content,
            automatically_copy=automatically_copy
        )

        if url and len(url) != 0:
            result += '&url={}'.format(url)

        if sound and len(sound) != 0:
            result = result + '&sound={}'.format(sound)

        return result

    def push(self, content, title=None, url=None,
             receivers=None, sound=None, automatically_copy=False):
        failing_receiver = []
        for key in (receivers or self.key_list):
            url = self.get_request_url(content, key, title, url, sound, automatically_copy)
            logger.info("Push to {}".format(url))

            resp = requests.get(url)
            data = json.loads(resp.text)
            if not (resp.status_code == 200 and data['code'] == 200):
                logger.error("Fail to push to [{}], error message = {}".format(key, data['message']))
                failing_receiver.append(key)

        logger.info("Number of failed pushes: {}".format(len(failing_receiver)))
        return failing_receiver
