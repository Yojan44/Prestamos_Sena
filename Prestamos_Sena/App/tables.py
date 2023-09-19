from models import Prestamo
from table import Table
from table.columns import Column

class PrestamosTable(Table):
    id = Column(field='id')
    name = Column(field='name')
    class Meta:
        model = Prestamo