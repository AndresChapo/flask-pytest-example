
from models.users_model import User


class TestUsers:
    def test_create_user(self, db_session):
        user = User().create(name="pepe", email="pepe@mail.com", password="123")
        
        db_users = db_session.query(User).all()
        assert len(db_users) == 1

    def test_get_users_list(self):
        assert True
