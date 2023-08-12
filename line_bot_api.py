from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage,
    FlexSendMessage,TemplateSendMessage,ImageCarouselTemplate,ImageCarouselColumn, PostbackAction,PostbackEvent
)
#Channel access token
#Channel secret
line_bot_api = LineBotApi('tHtDbQSQJjIZcgHRRkgXrgj0CPLVeKMHZNk6akbQJCVvnLRmPf0TiQF/L/CXZ6+ItpUKaG+Yh1Z8YmEFDrWg+lXBavoEw8YXvhsX6dysouoeJZUbHnkdBzekZSl+c535b21o0pvCNqv/UeD7EYR37QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9b896be843e2ba632a0f456162a8585e')
