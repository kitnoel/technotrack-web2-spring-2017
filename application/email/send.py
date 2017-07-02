import os
from datetime import time, datetime, timedelta

from templated_email import InlineImage, send_templated_mail


def send_daily_mail(user, day):
    tomorrow = day + timedelta(days=1)
    day_start = datetime.combine(day, time())
    day_end = datetime.combine(tomorrow, time())

    from ugc.models import Post
    posts = Post.objects.filter(created__lte=day_end, created__gte=day_start)
    # From a file
    f = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'img.png')
    with open(f, 'rb') as img:
        image = img.read()
    inline_image = InlineImage(filename="img.png", content=image)

    send_templated_mail(
        template_name='daily',
        from_email='from@example.com',
        recipient_list=[user.email],
        context={
            'username': user.username,
            'posts': posts,
            'date': day,
            'image': inline_image,
        },
        create_link=True
        # Optional:
        # cc=['cc@example.com'],
        # bcc=['bcc@example.com'],
        # headers={'My-Custom-Header':'Custom Value'},
        # template_prefix="my_emails/",
        # template_suffix="email",
    )
