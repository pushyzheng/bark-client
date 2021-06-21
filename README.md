# bark-client

## 1. Quick start

python client：

```python
from bark_client import BarkClient, SoundType

client = BarkClient(domain='api.day.app', key_list=['your key'])

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
```