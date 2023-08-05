from django.conf import settings

def hello_world(message, message2="message 2"):
    print('first message is %s' %(message))
    print('second message:: %s' %(settings.Q_CLUSTER))
    print('3rd message is:: %s' %(message2))
