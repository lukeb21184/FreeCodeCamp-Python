
alice = User("Alice")
bob = User("Bob")

alice.send_email(bob, "Hello", "Hi Bob! How are you?")
alice.send_email(bob, "Meeting", "Don't forget our meeting at 3 PM.")

bob.inbox.list_emails()


bob.inbox.read_email(1)


bob.inbox.list_emails()
