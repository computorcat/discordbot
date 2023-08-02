# database - userid, guildid, level, xp
# GAH whats a suitable level system algorithm thingy
# i think i'll just do a simple one
# Sorry about the bad names. I cant come up with anything useful!
# python can sort out all the level incrementing and stuff

from sqlalchemy import create_engine, MetaData, Table, Column, BigInteger, Integer

engine = create_engine('sqlite:///levels.db')
metadata = MetaData()

levelsdb = Table(
    'levels',
    metadata,
    Column('userid', BigInteger, primary_key=True),
    Column('guildid', BigInteger, primary_key=True),
    Column('level', Integer, default=1),
    Column('xp', Integer, default=0)
)

metadata.create_all(engine)


