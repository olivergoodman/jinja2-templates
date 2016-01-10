from app import app, db

class Page(db.Model):
    page_id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    page_name = db.Column(db.String(80), unique=True)
    page_hits = db.Column(db.Integer, default=0)

    def __init__(self, page_hits, page_name):
        self.page_name = page_name
        self.page_hits = page_hits

    def __repr__(self):
        return '<Page Title %r>' % self.page_name

    #increment page_title for corresponding page_name <----------------- 
    def pageVisit():
    	page_hits += 1
  
