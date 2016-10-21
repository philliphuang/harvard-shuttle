import json

def results(parsed, original_query):
    try:
        target = parsed['~target']
    except KeyError:
        target = 0

    # mather
    if target in ('m', 'mather', 'Mather'):
        url = 'http://harvard.transloc.com/m/stop/code/113'
        title = 'Harvard Shuttle - Mather'

    # lamont
    elif target in ('l', 'lamont', 'Lamont'):
        url = 'http://harvard.transloc.com/m/stop/code/109'
        title = 'Harvard Shuttle - Lamont'

    # quad
    elif target in ('q', 'quad', 'Quad'):
        url = 'http://harvard.transloc.com/m/stop/code/101'
        title = 'Harvard Shuttle - Quad'

    # # maxwell dworkin
    # elif target in ('md', 'MD', 'Maxwell', 'Maxwell Dworkin', 'Dworkin'):
    #     url = 'http://harvard.transloc.com/m/stop/code/101'
    #     title = 'Harvard Shuttle - Quad'

    # general
    else:
        url = 'http://harvard.transloc.com/m/'
        title = 'Harvard Shuttle'

    return {
        "title": title,
        "html": "<script>window.location=%s</script>" % json.dumps(url),
        # "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
        # "webview_links_open_in_browser": True,
        "run_args": [url]
    }

def run(url):
    import os
    os.system('open "{0}"'.format(url))