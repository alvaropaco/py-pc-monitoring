import couchdb

class Store:

    def __init__(self, url, db):
        self.conn = couchdb.client.Server(url)
        #self.conn = couchdb.Server(host + ':' + password + '@' + host + ':' + port)
        self.db = self.conn[db]

    def __str__(self):
        return self.conn.version()

    def save(doc):
        print(doc)
        self.db.save(doc)