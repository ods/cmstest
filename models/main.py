from sqlalchemy.schema import MetaData
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from iktomi.db.sqla.declarative import AutoTableNameMeta, TableArgsMeta


metadata = MetaData()

TABLE_ARGS = {
    'mysql_engine': 'InnoDB',
    'mysql_default charset': 'utf8',
}

class ModelsMeta(AutoTableNameMeta, TableArgsMeta(TABLE_ARGS)):
    pass


Base = declarative_base(
    metadata=metadata,
    name='Base',
    metaclass=ModelsMeta,
)


class Tag(Base):

    id = Column(Integer, primary_key=True)
    title = Column(String(500), default='')


class Doc_Tag(Base):
    doc_id = Column(Integer,
                    ForeignKey('Doc.id', ondelete='cascade'),
                    primary_key=True)
    tag_id = Column(Integer,
                    ForeignKey('Tag.id', ondelete='cascade'),
                    primary_key=True)
    order = Column(Integer)


class Doc(Base):

    id = Column(Integer, primary_key=True)
    title = Column(String(500), default='')
    tags = relationship(Tag, secondary=Doc_Tag.__table__)

