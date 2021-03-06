from bark_client import BarkClient, SoundType
from bark_client.utils import logger

client = BarkClient(domain='api.day.app', key_list=['your key'])

if __name__ == '__main__':
    logger.info("start")

    # Only content
    client.push('Content')

    # Title and content
    client.push('Content', title='Title')

    # Use custom sound
    client.push('Content', title='Title', sound=SoundType.CHOO)

    # Set url
    client.push('Content', title='Title', url='https://google.com')

    # Designated receiver
    client.push('Content', title='Title', url='https://google.com', receivers=['your key'])

    # Set automatically copy
    client.push('Content', title='Title', url='https://google.com', receivers=['your key'], automatically_copy=True)
