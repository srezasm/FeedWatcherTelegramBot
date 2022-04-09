import config
import feedparser

def fetch_new_items(feed):
    p = feedparser.parse(feed['url'])
    items = p.entries
    name = feed['name']

    with open(config.getids()) as fr:
        oldlines = fr.read().splitlines()
        oldids = []
        newlines = oldlines.copy()

        isn = False
        for ol in oldlines:
            if ol.startswith(name):
                isn = True

                # fill the old_ids with current feed ids
                oldids.extend(ol.split('::'))
                oldids.pop(0)

                break

        if not isn:
            ii = []
            for i in items:
                ii.append(i.id)

            newlines.append(name + '::' + '::'.join(ii))
            with open(config.getids(), 'w') as fw:
                fw.write('\n'.join(newlines))
            return items

        # fill new_items
        newitems = items.copy()
        for id in oldids:
            for it in items:
                if id == it.id:
                    newitems.remove(it)
                    break
        
        if len(newitems) == 0:
            return []

        # fill new_ids
        newids = []
        for i in range(len(newitems)):
            newitems[i]['category'] = feed['category']
            newids.append(newitems[i].id)

        # add new items ids to the file
        for i in range(len(newlines)):
            nl = newlines[i]

            if nl.startswith(name):
                newlines[i] = nl + '::' + '::'.join(newids)
                break

        # write new_lines into ids file
        config.writeids('\n'.join(newlines))

        # if feed['category'] == 'youtube':
        #     # TODO: download youtube video https://www.the-analytics.club/download-youtube-videos-in-python
        
        return newitems


def write_etag(name, etag):
    with open(config.getetags()) as fr:
        lines = fr.read().splitlines()

        if len(lines) == 0:
            lines.append(f'{name}::{etag}')

        for ni in range(len(lines)):
            l = lines[ni]
            if l.startswith(name):
                l = f'{name}::{etag}'
                break

        config.writeetags('\n'.join(lines))


def get_etag(name):
    with open(config.getetags()) as fr:
        lines = fr.read().splitlines()

        if name not in fr.read():
            return ''

        else:
            for l in lines:
                if l.startswith(name):
                    return l.split('::')[1]