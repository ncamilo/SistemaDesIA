from sqlite3 import Connection

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.pool import ConnectionPoolEntry


class Base(DeclarativeBase):
    pass


def build_database(url: str) -> tuple[Engine, sessionmaker[Session]]:
    engine = create_engine(url, connect_args={"check_same_thread": False})

    @event.listens_for(engine, "connect")
    def enable_foreign_keys(connection: Connection, _record: ConnectionPoolEntry) -> None:
        connection.execute("PRAGMA foreign_keys=ON")

    return engine, sessionmaker(bind=engine, expire_on_commit=False)
