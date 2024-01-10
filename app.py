# function to print the email variables to the log
def new_message(to_email, from_email, subject, message):
    print("FROM: ", from_email)
    print("TO: ", to_email)
    print("Subject: ", subject)
    print("Message: ", message)
    return


new_message("receiver@whatever.com",
            "me@here.com",
            "Hey",
            "Did you see the old lady fall on the sidewalk? Casi se mata")

print("\n")

new_message("alejandra@receive_email.com",
            "carlos@sender_email.com",
            "Yo",
            "What's up?")