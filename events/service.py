#預約相關功能都寫在這
from line_bot_api import*
from urllib.parse import parse_qsl

services = {
    1: {
        'category':'計畫一',
        'img_url':'https://i.imgur.com/w5Uc5dK.jpg',
        'title':'輕型機車',
        'duration':'30min',
        'description': '第三人責任險200/400/30+慰問金5萬+乘客險100萬+駕駛人險200萬',
        'price':'1,827',
        'post_url':'https://tw.piliapp.com/facebook-symbols/'
    },
    2: {
        'category':'計畫一',
        'img_url':'https://i.imgur.com/w5Uc5dK.jpg',
        'title':'普通重型機車',
        'duration':'30min',
        'description': '第三人責任險200/400/30+慰問金5萬+乘客險100萬+駕駛人險200萬',
        'price':'2,546',
        'post_url':'https://tw.piliapp.com/facebook-symbols/'
    },
    3: {
        'category':'計畫二',
        'img_url':'https://i.imgur.com/w5Uc5dK.jpg',
        'title':'輕型機車',
        'duration':'30min',
        'description': '第三人責任險200/400/30+慰問金5萬+駕駛人險200萬+超額1000萬',
        'price':'1,992',
        'post_url':'https://tw.piliapp.com/facebook-symbols/'
    },
    4: {
        'category':'計畫二',
        'img_url':'https://i.imgur.com/w5Uc5dK.jpg',
        'title':'普通重型機車',
        'duration':'30min',
        'description': '第三人責任險200/400/30+慰問金5萬+駕駛人險200萬+超額1000萬',
        'price':'2,904',
        'post_url':'https://tw.piliapp.com/facebook-symbols/'
    },
    5: {
        'category':'計畫三',
        'img_url':'https://i.imgur.com/w5Uc5dK.jpg',
        'title':'輕型機車',
        'duration':'30min',
        'description': '第三人責任險200/400/30+慰問金5萬+乘客險100萬+駕駛人險200萬+超額300萬',
        'price':'2,181',
        'post_url':'https://tw.piliapp.com/facebook-symbols/'
    },
    6: {
        'category':'計畫三',
        'img_url':'https://i.imgur.com/w5Uc5dK.jpg',
        'title':'普通重型機車',
        'duration':'30min',
        'description': '第三人責任險200/400/30+慰問金5萬+乘客險100萬+駕駛人險200萬+超額300萬',
        'price':'3,009',
        'post_url':'https://tw.piliapp.com/facebook-symbols/'
    }
}

def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='請選擇想服務類別',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://drive.google.com/uc?export=download&id=1UbeFJNmNF3PfPYDdoEEWPxZma5M82x-T',
                    action=PostbackAction(
                        label='計畫一',
                        display_text='想了解計畫一',
                        data='action=service&category=計畫一'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://drive.google.com/uc?export=download&id=1UbeFJNmNF3PfPYDdoEEWPxZma5M82x-T',
                    action=PostbackAction(
                        label='計畫二',
                        display_text='想了解計畫二',
                        data='action=service&category=計畫二'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://drive.google.com/uc?export=download&id=1UbeFJNmNF3PfPYDdoEEWPxZma5M82x-T',
                    action=PostbackAction(
                        label='計畫三',
                        display_text='想了解計畫三',
                        data='action=service&category=計畫三'
                    )
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [image_carousel_template_message])

def service_event(event):
    data = dict(parse_qsl(event.postback.data))
    
    bubbles = []
    
    for service_id in services:
        if services[service_id]['category'] == data['category']:
            service = services[service_id]
            bubble = {
                "type": "bubble",
                "hero": {
                "type": "image",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "url": service['img_url']
                },
                "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": service['title'],
                    "wrap": True,
                    "weight": "bold",
                    "size": "xl"
                    },
                    {
                    "type": "text",
                    "text": service['duration'],
                    "size": "md",
                    "weight": "bold"
                    },
                    {
                    "type": "text",
                    "text": service['description'],
                    "margin": "lg",
                    "wrap": True
                    },
                    {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                        "type": "text",
                        "text": f"NT$ {service['price']}",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl",
                        "flex": 0
                        }
                    ],
                    "margin": "xl"
                    }
                ]
                },
                "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "button",
                    "style": "primary",
                    "action": {
                        "type": "postback",
                        "label": "預約",
                        "data": f"action=select_date&service_id={service_id}",
                        "displayText": f"我想預約【{service['title']} {service['duration']}】"
                    },
                    "color": "#b28530"
                    },
                    {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "了解詳情",
                        "uri": service['post_url']
                    }
                    }
                ]
                }
            }

            bubbles.append(bubble)
    
    flex_message = FlexSendMessage(
        alt_text='請選擇預約項目',
        contents={
            'type':'carouesl',
            'contents': bubbles
        }
    )

