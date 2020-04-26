#pip install plyer
from plyer import notification

notification.notify(
    title='Here is the title',
    message='Here is the message',
    app_icon=None,  # e.g. 'C:\\icon.ico'
    timeout=10,  # seconds
)
