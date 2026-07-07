    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')
            
    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
            
    def read_email(self, index):
        if not self.emails:
            print("Inbox is empty.\n")
            return

        actual_index = index - 1   
