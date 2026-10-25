def send_messages(messages,sent_messages):
    while messages:
            current_message = messages.pop()
            print(f"Sending message: {current_message}")
            sent_messages.append(current_message)  
    print("\nThe following message has been sent:")
    for sent_message in sent_messages:
        print(sent_message)
        
messages = ['Hi, good evening!', "How's your day?", 'Happy lunch!', 'Goodluck!']
sent_messages = []

send_messages(messages[:],sent_messages)
print(f"Messages: {messages}")
print(f"Messages sent: {sent_messages}")