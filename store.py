import couchdb

class Store:

    def __init__(self, url, db):
        self.conn = couchdb.client.Server(url)
        self.db = self.conn[db]

    def __str__(self):
        return self.conn.version()

    def save(self, doc):
        return self.db.save(doc)