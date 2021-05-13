from models import *


class TopicService:

    def __init__(self):
        self.topics = []

    def add_topic(self, topic):
        self.topics.append(topic)

    def find_by_topic_name(self, topic_name):
        for topic in self.topics:
            if topic.topic_name == topic_name:
                return topic
        return None

    def process_messages(self):
        for topic in self.topics:
            topic.broadcast()


class UserService:

    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def find_by_user_name(self, user_name):
        for user in self.users:
            if user.username == user_name:
                return user
        return None


class MessageService:

    def __init__(self):
        self.messages = []

    def add_message(self, message, topic):
        self.messages.append(message)
        topic.messages.append(message)


class SubscriptionService:

    def __init__(self):
        self.subscriptions = []

    def add_subscription(self, subscription):
        self.subscriptions.append(subscription)
        subscription.user.topics.append(subscription.topic)
        subscription.topic.subscribed_users.append(subscription.user)


class AsyncService:

    def __init__(self):
        self.executor = None


class ConsoleService:

    def __init__(self):
        self.user_service = UserService()
        self.topic_service = TopicService()
        self.message_service = MessageService()
        self.subscription_service = SubscriptionService()

    def process_command(self, command_input):
        command_data = command_input.split()
        if command_data[0] == 'addUser':
            self.add_user(command_data[1], command_data[2])
        elif command_data[0] == 'addTopic':
            self.add_topic(command_data[1], command_data[2])
        elif command_data[0] == 'subscribeTopic':
            self.subscribe_topic(command_data[1], command_data[2])
        elif command_data[0] == 'postEvent':
            self.post_event(command_data[1], command_data[2], command_data[3])
        elif command_data[0] == 'processMessages':
            self.process_messages()
        elif command_data[0] == 'exit':
            exit(0)

    def add_user(self, user_name, role):
        self.user_service.add_user(User(user_name, role))

    def add_topic(self, topic_name, user_name):
        user = self.user_service.find_by_user_name(user_name)
        if user.role == 'Admin':
            self.topic_service.add_topic(Topic(topic_name))

    def subscribe_topic(self, topic_name, user_name):
        user = self.user_service.find_by_user_name(user_name)
        topic = self.topic_service.find_by_topic_name(topic_name)
        subscription = Subscription(user, topic)
        self.subscription_service.add_subscription(subscription)

    def post_event(self, message_id, topic_name, text):
        message = Message(message_id, topic_name, text)
        topic = self.topic_service.find_by_topic_name(topic_name)
        self.message_service.add_message(message, topic)

    def process_messages(self):
        self.topic_service.process_messages()
