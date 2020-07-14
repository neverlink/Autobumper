## Autobumper

### Requirements
- Python 3.6 or later
- Requests

### config.json
- Open the network tab in your browser console and reply to a thread
- "cookie":  Under Request Headers, copy the whole value of "cookie" or just "ogusersmybbuser=XXXXXXXXXXXXX;"
- "my_post_key":  Copy the value under Form Data
- "signature":  Whether it's included while bumping
- "bump_delay": 
  - "posts"  - delay between bumping each thread (in seconds)
  - "threads" - delay between each bump per thread
- Get ThreadID from the address bar after clicking reply on a thread.
