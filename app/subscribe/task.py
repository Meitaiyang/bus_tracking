from flask_mail import Message
import requests
from datetime import datetime
from app.extensions import celery, mail
from app.models.user import Users

@celery.task
def check_users():
    # send the request to route "/user"
    headers = {'Connection': 'close', 'Content-Type': 'application/json'}
    response = requests.get("http://172.23.0.3:5050/subscribe/user")
    # get the response data
    data = response.json()
    
    for user in data:
        # get the current system time in seconds
        current_time = int(datetime.now().timestamp())

        print("\n\n\n",current_time,"\n\n\n")
    
        # calculate the time difference in minutes
        time_diff = user['estimated_time'] - current_time

        # check if the time difference is less than 3 minutes
        if time_diff < 180:

            response = requests.post(f"http://172.23.0.3:5050/subscribe/mail/{user['user_id']}")
            # create a new email message
            # msg = Message('Bus Arrival Alert', sender='shrek473@gmail.com', recipients=[user['email']])
            # msg.body = f"The bus number {user['bus_number']} is arriving at station {user['station']} in {time_diff} minutes."

            # send the email
            # mail.send(msg)
            print("mail send")
            print(user)
            response = requests.delete(f"http://172.23.0.3:5050/subscribe/delete/{user['user_id']}")

# Run the check_users task every minute
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3.0, check_users.s())