from config import db

class Contact(db.Model):
    id = db.column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80),unqiue = False, nullible = False)
    last_name = db.Column(db.String(80),unqiue = False, nullible = False)
    email = db.Column(db.String(120),unqiue = False, nullible = False)

    def to_json(self):
        return {
            "id": self.id,
            "firstName":self.first_name,
            "lastName":self.last_name,
            "email":self.email
        }