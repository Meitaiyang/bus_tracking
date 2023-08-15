from app.extensions import celery
from app.models.user import Users

@celery.task
def check_users():
    users = Users.query.all()
    if users is not None:
        for user in users:
            print(user.email)

# Run the check_users task every minute
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3.0, check_users.s())