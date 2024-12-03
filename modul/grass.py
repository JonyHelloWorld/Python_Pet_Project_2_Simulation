from modul.entity import Entity
from logging import getLogger

logger = getLogger(__name__)

class Grass(Entity):
    """
    класс Трава - еда для травоядных
    """
    def __init__(self, row, col, map_instance):
        super().__init__(row=row, col=col, avatar="\U0001F331", map_instance=map_instance)
