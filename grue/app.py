import logging

import os.path

from gevent import monkey
monkey.patch_all()

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.events import subscriber, ApplicationCreated
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from .gamepool import GamePool
from .frotz import Frotz

logging.basicConfig()
log = logging.getLogger(__name__)


here = os.path.dirname(os.path.abspath(__file__))


def game_creator():
    return Frotz(os.path.join(here, 'games', 'zork1.z5'))

pool = GamePool(creator=game_creator)


def new_game(request):
    # make a new game (frotz instance) and set it in the session
    game_id = pool.spawn()
    request.session['game_id'] = game_id


@view_config(route_name='new')
def new_view(request):
    # remove the existing game, if any
    game_id = request.session['game_id']
    pool.kill(game_id)
    # make a new one
    new_game(request)
    return HTTPFound(location=request.route_url('index'))


@view_config(route_name='move', renderer='json')
def move_view(request):
    game_id = request.session['game_id']
    game = pool.get(game_id)

    move = request.POST.get('move')
    if move:
        game.tell(move)

    resp = game.listen()

    resp = resp.replace('\n', '<br>')

    return {
        'response': resp,
        'location': game.location,
        'score': game.score,
        'moves': game.moves,
    }


@view_config(route_name='index', renderer='index.mako')
def index_view(request):
    if 'game_id' not in request.session:
        new_game(request)
    return {}


def make_app():
    settings = {}
    settings['reload_all'] = True
    settings['debug_all'] = True
    settings['mako.directories'] = os.path.join(here, 'templates')

    session_factory = UnencryptedCookieSessionFactoryConfig('s3krit')
    config = Configurator(settings=settings, session_factory=session_factory)

    config.add_route('index', '/')
    config.add_route('new', '/new')
    config.add_route('move', '/move')

    config.add_static_view('static', os.path.join(here, 'static'))

    config.scan()

    app = config.make_wsgi_app()

    return app
