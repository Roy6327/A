#預約相關功能都寫在這
from line_bot_api import*
from urllib.parse import parse_qsl

# services = {
#     1: {
#         'category':'計畫一',
#         'img_url':'',
#         'title':'強制保險一年',
#         'description': '賠付對方體傷',
#         'price':'658',
#         'post_url':''
#     },
#     2: {
#         'category':'計畫一',
#         'img_url':'',
#         'title':'強制保險兩年',
#         'description': '賠付對方體傷',
#         'price':'1200',
#         'post_url':''
#     },
#     3: {
#         'category':'計畫二',
#         'img_url':'',
#         'title':'強制保險+第三人責任險',
#         'description': '賠付對方體傷、財損',
#         'price':'1800',
#         'post_url':''
#     },
#     4: {
#         'category':'計畫三',
#         'img_url':'',
#         'title':'強制保險+第三人責任險',
#         'description': '賠付對方體傷、財損',
#         'price':'2500',
#         'post_url':''
#     },
#     5: {
#         'category':'計畫三',
#         'img_url':'',
#         'title':'強制保險+第三人責任險',
#         'description': '賠付對方體傷、財損',
#         'price':'2500',
#         'post_url':''
#     },
#     6: {
#         'category':'計畫三',
#         'img_url':'',
#         'title':'強制保險+第三人責任險',
#         'description': '賠付對方體傷、財損',
#         'price':'2500',
#         'post_url':''
#     }
# }

def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='請選擇想服務類別',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://drive.google.com/uc?export=download&id=1UbeFJNmNF3PfPYDdoEEWPxZma5M82x-T',
                    action=PostbackAction(
                        label='按摩調理',
                        display_text='想了解按摩調理',
                        data='action=service&category=按摩調理'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://drive.google.com/uc?export=download&id=1-n-1HqfSsCJQmUhlYhPgWMowE6NTBDUR',
                    action=PostbackAction(
                        label='臉部護理',
                        display_text='想了解臉部護理',
                        data='action=service&category=臉部護理'
                    )
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [image_carousel_template_message])

# def service_category_event(event):
#     data = dict(parse_qsl(event.postback.data))
    
#     bubbles = []
    
#     for service_id in services:
#         if services[service_id]['category'] == data['category']:
#             service = services[service_id]
#             bubble = {
#                 "type": "bubble",
#                 "hero": {
#                 "type": "image",
#                 "size": "full",
#                 "aspectRatio": "20:13",
#                 "aspectMode": "cover",
#                 "url": service['img_url']
#                 },
#                 "body": {
#                 "type": "box",
#                 "layout": "vertical",
#                 "spacing": "sm",
#                 "contents": [
#                     {
#                     "type": "text",
#                     "text": service['title'],
#                     "wrap": True,
#                     "weight": "bold",
#                     "size": "xl"
#                     },
#                     {
#                     "type": "text",
#                     "text": service['duration'],
#                     "size": "md",
#                     "weight": "bold"
#                     },
#                     {
#                     "type": "text",
#                     "text": service['description'],
#                     "margin": "lg",
#                     "wrap": True
#                     },
#                     {
#                     "type": "box",
#                     "layout": "baseline",
#                     "contents": [
#                         {
#                         "type": "text",
#                         "text": f"NT$ {service['price']}",
#                         "wrap": True,
#                         "weight": "bold",
#                         "size": "xl",
#                         "flex": 0
#                         }
#                     ],
#                     "margin": "xl"
#                     }
#                 ]
#                 },
#                 "footer": {
#                 "type": "box",
#                 "layout": "vertical",
#                 "spacing": "sm",
#                 "contents": [
#                     {
#                     "type": "button",
#                     "style": "primary",
#                     "action": {
#                         "type": "postback",
#                         "label": "預約",
#                         "data": f"action=select_date&service_id={service_id}",
#                         "displayText": f"我想預約【{service['title']} {service['duration']}】"
#                     },
#                     "color": "#b28530"
#                     },
#                     {
#                     "type": "button",
#                     "action": {
#                         "type": "uri",
#                         "label": "了解詳情",
#                         "uri": service['post_url']
#                     }
#                     }
#                 ]
#                 }
#             }

#             bubbles.append(bubble)
    
#     flex_message = FlexSendMessage(
#         alt_text='請選擇預約項目',
#         contents={
#             'type':'carouesl',
#             'contents': bubbles
#         }
#     )
