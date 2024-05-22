
def notifications_processor(request):
    if request.user.is_authenticated:
        notifications = request.user.received_notifications.filter(is_read=False)
        print(notifications)
        unread_count = notifications.count()
    else:
        notifications = None
        unread_count = 0

    return {
        'notifications': notifications,
        'unread_count': unread_count,
    }