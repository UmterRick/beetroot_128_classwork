from datetime import datetime


class AbstractUser:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def login(self, password):
        pass






class User(AbstractUser):
    def login(self, password):
        return True if password == "password" else False


class GoogleUser(AbstractUser):
    def login(self, password):
        is_login_from_google = True
        return True if is_login_from_google else False


class Author:
    def __init__(self):
        self.subscribers = [1, 2, 3, 4]

class Post:
    def __init__(self):
        self.text = None
        self.author = None
        self.created_at = None
        self.create_handlers = (PostAds, PostAnalytics, PostRecommendations, PostNotif)


    def create(self, author, text, date):
        self.text = text
        self.author = author
        self.created_at = date



        for handler in self.create_handlers:
            handler().handle(self)
        return self


class PostHandler:

    def handle(self, post: Post):
        pass

    def transform_post_to_comfort_standart(self):
        ...



class PostAnalytics(PostHandler):
    def handle(self, post: Post):
        print("Get analytics")



class PostRecommendations(PostHandler):
    def handle(self, post: Post):
        print(f"Is {post} recommended?")


class PostAds(PostHandler):
    def handle(self, post: Post):
        print(f"Add ads to {post}")


class PostNotif(PostHandler):
    def handle(self, post: Post):
        for user in post.author.subscribers:
            print("Send notification")



new_post = Post()
new_post.create(Author(), "Hello", datetime.today())

