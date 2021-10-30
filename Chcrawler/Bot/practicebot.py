import requests
from bs4 import BeautifulSoup
import os
import telegram

bot = telegram.Bot(token='1255283054:AAGxo1AvTDBjQ5DGd_CB37ycZxtDMPo15eU')
chat_id = bot.getUpdates()[-1].message.chat.id

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://www.clien.net/service/recommend')
req.encoding = 'utf-8'

html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('span.subject_fixed')
latest = posts[0].text

with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
    before = f_read.readline()
    if before != latest:
    # 같은 경우는 에러 없이 넘기고, 다른 경우에만 메시지 보내는 로직
        bot.sendMessage(chat_id=chat_id, text='새 글이 올라왔어요!')
    else:
        bot.sendMessage(chat_id=chat_id, text='새 글이 없어요 ㅠㅠ')
    f_read.close()

with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
    f_write.write(latest)
    f_write.close()
