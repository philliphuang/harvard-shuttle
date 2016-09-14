import json

def results(parsed, original_query):
    # target = parsed.values()[0]
    # print target
    # if target in ('mather', 'Mather', 'Mather Shuttle'):
    #     url = 'http://harvard.transloc.com/m/stop/code/113'
    # else:
    url = 'http://harvard.transloc.com/m/'
    return {
        "title": "Harvard Shuttle",
        "html": "<script>window.location=%s</script>" % json.dumps(url),
        # "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
        # "webview_links_open_in_browser": True,
        "run_args": [url]
    }

def run(url):
    import os
    os.system('open "{0}"'.format(url))