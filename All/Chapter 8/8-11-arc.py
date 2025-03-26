msgs = ['I love you!', 'hug you!', 'kiss you.', 'touch you.']
def show_msg(mesgs):
    """print all messages"""
    for mesg in mesgs:
        print(mesg)

show_msg(msgs)
print()

def send_msg(unsent_msgs, sent_msgs):
    """send message and move the msgs into the sent_msg"""
    while unsent_msgs:
        sending_msg = unsent_msgs.pop()
        print(sending_msg)
        sent_msgs.append(sending_msg)

sent_mesgs = []

send_msg(msgs[:], sent_mesgs)

print("\nThe final:")
print(msgs)
print(sent_mesgs)
