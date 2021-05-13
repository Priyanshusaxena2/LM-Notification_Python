class User:

    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.topics = []

    def broadcast(self, message):
        print("id: " + message.id + ", message: "
              + message.text + ", sentTo: " + self.username)


class Topic:

    def __init__(self, topic_name):
        self.topic_name = topic_name
        self.subscribed_users = []
        self.messages = []

    def broadcast(self):
        for message in self.messages:
            if not message.is_broadcasted:
                for user in self.subscribed_users:
                    user.broadcast(message)


class Subscription:

    def __init__(self, user, topic):
        self.user = user
        self.topic = topic


class Message:

    def __init__(self, message_id, topic_name, text):
        self.id = message_id
        self.topic_name = topic_name
        self.text = text
        self.is_broadcasted = False
