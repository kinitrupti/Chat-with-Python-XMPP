import xmpp

username = 'yourusernameofgtalk' #just username. Don't use @gmail.com
passwd = 'yourpassword'
recipients = ['friend1@gmail.com','friend2@gmail.com']
msg='hello :)'

for recipient in recipients:
        client = xmpp.Client('gmail.com')
        client.connect(server=('talk.google.com',5223))
        client.auth(username, passwd)
        client.sendInitPresence()

        message = xmpp.Message(recipient, msg)
        message.setAttr('type', 'chat')
        client.send(message)

