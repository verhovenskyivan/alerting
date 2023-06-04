import smtplib 
from email.message import Message

def alert(subject, body, to):
    message = Message()
    message.set_content(body)
    message['subject'] = subject
    message['body'] = body
    message['to'] = to
    
    user = "verhovenskyivan@gmail.com"
    password = ""
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(message)
    
    server.quit()
    
if __name__ == '__main__':
    alert('hello','brother', 'verhovenskyivan@gmail.com')