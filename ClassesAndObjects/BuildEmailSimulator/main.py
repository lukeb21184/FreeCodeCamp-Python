    def read_email(self, index):
        if not self.emails:
            print("Inbox is empty.\n")
            return

        actual_index = index - 1

        if 0 <= actual_index < len(self.emails):
            self.emails[actual_index].display_full_email()
        else:
            print("Invalid email number.\n")


alice = User("Alice")
bob = User("Bob")

alice.send_email(bob, "Hello", "Hi Bob! How are you?")
alice.send_email(bob, "Meeting", "Don't forget our meeting at 3 PM.")

bob.inbox.list_emails()


bob.inbox.read_email(1)


bob.inbox.list_emails()
