"""Utilities for querying Trino system tables."""

import trino


class TrinoClient:
    """Minimal Trino client placeholder."""

    def __init__(self, host: str, port: int = 8080, user: str | None = None):
        self.host = host
        self.port = port
        self.user = user or "trino"
        self._conn = None

    def connect(self):
        """Establish a connection to Trino."""
        self._conn = trino.dbapi.connect(
            host=self.host,
            port=self.port,
            user=self.user,
        )
        return self._conn

    def query(self, sql: str):
        """Execute a query and return results."""
        if not self._conn:
            self.connect()
        cur = self._conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
