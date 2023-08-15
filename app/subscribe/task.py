from app.extensions import celery

def print_hello():
    print("Hello")

@celery.task
def check_users():
    print_hello()
    return "Hello"


# Run the check_users task every minute
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(15.0, check_users.s())