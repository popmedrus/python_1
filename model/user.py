class User:
    def __init__(self, user_name=None, user_email=None, user_password=None, id=None):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.user_name, self.user_email, self.user_password)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.user_name == other.user_name
