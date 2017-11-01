#!/opt/datadog-agent/embedded/bin/python

import time
import yaml
import re
import time
from datetime import datetime

def parse_log(logger,line):
    f = open('/opt/datadog-agent/agent/checks.d/log.yaml')
    data = yaml.load(f)
    f.close()

    severity = [ 'not_set','debug','info','warn','error','alert','emerg' ]

    for c in data['config']:
        if re.match(c['check_regex'],line) and not re.match(c['ignore_regex'],line):
            now = datetime.now()
            date = int(time.mktime(now.timetuple()))
            logger_event = {
                'msg_title': c['title'],
                'timestamp': date,
                'msg_text': line,
                'alert_type': 'error',
                'event_type': 'dada',
                'aggregation_key': 'popo',
                'tags': [
                    'id:' + c['id'],
                    'severity:'+ severity[c['severity']]
                 ],
                'priority': 'normal'
            }

            return logger_event
    return 'naiyo!'

def test():
    import logging
    logging.basicConfig(level=logging.DEBUG)

    line = 'something error'
    print parse_log(logging,line)

    line = 'poipoi error'
    print parse_log(logging,line)


if __name__ == '__main__':
    test()
