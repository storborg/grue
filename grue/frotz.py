import re
import string
import pexpect


class Frotz(object):
    """
    Wraps the frotz command line z-code interpreter to send game moves, and
    receive content back.
    """
    prompt = '>'

    game_re = re.compile('('
                         '(?P<location>.*)'
                         'Score\:\ '
                         '(?P<score>\d+)'
                         '.+'
                         'Moves\:\ '
                         '(?P<moves>\d+)'
                         ')?'
                         '(?P<text>.+)',
                         re.DOTALL)

    def __init__(self, gamefile):
        self.score = None
        self.location = None
        self.moves = None

        self.strip_echo = 0

        self.frotz = pexpect.spawn('dfrotz %s' % gamefile)
        self.frotz.expect(self.prompt)

    def tell(self, line):
        line = line.strip()
        # Store the length of the input line that we're sending to the
        # interpreter process, so that we can remove it from the next response
        # we get.
        self.strip_echo = len(line)
        self.frotz.sendline(line)
        self.frotz.expect(self.prompt)

    def listen(self):
        resp = self.frotz.before[self.strip_echo:]

        m = self.game_re.search(resp)
        d = m.groupdict()

        if d.get('score'):
            self.score = int(d.get('score'))

        if d.get('moves'):
            self.moves = int(d.get('moves'))

        if d.get('location'):
            self.location = d.get('location').strip()

        return d['text'].strip()
