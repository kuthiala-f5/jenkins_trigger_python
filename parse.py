import re
import time
from calendar import timegm
import urllib

def main():
    url = 'https://github.com/f5devcentral/f5-sphinx-theme/releases.atom'
    try:
        file_contents = urllib.urlopen(url).read()
        pattern = re.compile("<id>tag:github.com.*?(v\d+\.\d+\.\d+)</id>\n.*?<updated>(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)")
        releases = re.findall(pattern, file_contents)
        for i in releases:
            utc_time = time.strptime(i[1], "%Y-%m-%dT%H:%M:%SZ")
            release_time_since_epoch = timegm(utc_time)
            if int(time.time()-release_time_since_epoch) <= 303:
                print i[0]
                break
        else:
            print 'no_build'
    except:
        print 'no_build'

if __name__ == '__main__':
    main()
