import logging

log = logging.getLogger(__name__)


class GamePool(object):
    """
    Implement a pool of Frotz resources, keyed by id.
    """
    def __init__(self, creator):
        self.creator = creator
        self.games = {}

    def spawn(self):
        """
        Spawn a new game resource, and return its ID.
        """
        new = self.creator()
        id = len(self.games)
        self.games[id] = new
        log.warn("Started new game: %s", id)
        return id

    def kill(self, id):
        """
        Kill a game resource, by ID.
        """
        # FIXME will leak memory like a sieve.
        log.warn("Killed game: %s", id)
        del self.games[id]

    def get(self, id):
        """
        Get a game resource, by ID.
        """
        log.warn("Loading game: %s", id)
        if id not in self.games:
            self.games[id] = self.creator()
        return self.games[id]
