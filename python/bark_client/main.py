import requests
import json
from bark_client.utils import logger, is_blank


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

    def get_request_url(self, content, key, title=None, group=None,
                        url=None, sound=None, automatically_copy=False):
        base_url = 'https://{domain}/{key}'.format(domain=self.domain, key=key)
        if title:
            base_url += '/{title}'.format(title=title)
        base_url += '/{}'.format(content)

        params = {
            'group': None if is_blank(group) else group,
            'automatically_copy': None if is_blank(automatically_copy) else automatically_copy,
            'url': None if is_blank(url) else url,
            'sound': None if is_blank(sound) else sound
        }
        return base_url, params

    def push(self, content, title=None, url=None, group=None,
             receivers=None, sound=None, automatically_copy=False):
        failing_receiver = []
        for key in (receivers or self.key_list):
            base_url, params = self.get_request_url(
                content=content, key=key, title=title,
                group=group, url=url, sound=sound,
                automatically_copy=automatically_copy
            )
            logger.info("Push to {}".format(base_url))

            resp = requests.get(base_url, params=params)
            data = json.loads(resp.text)
            if not (resp.status_code == 200 and data['code'] == 200):
                logger.error("Fail to push to [{}], error message = {}".format(key, data['message']))
                failing_receiver.append(key)

        logger.info("Number of failed pushes: {}".format(len(failing_receiver)))
        return failing_receiver
