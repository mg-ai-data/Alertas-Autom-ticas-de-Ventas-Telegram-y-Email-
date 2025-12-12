Para Telegram:

!pip install python-telegram-bot --quiet

from telegram import Bot
import nest_asyncio
import asyncio

nest_asyncio.apply()  # parcha el loop de colab

TOKEN = "TU_TOKEN"
CHAT_ID = "TU_CHAT_ID"

bot = Bot(token=TOKEN)

async def enviar_alerta(ventas):
    await bot.send_message(chat_id=CHAT_ID, text=f"⚠️ Alerta: ventas = {ventas}")

ventas = 120

if ventas > 100:
    await enviar_alerta(ventas)

print("Listo")

---

Para email:

import smtplib

SENDER = "tu_email@gmail.com"
PASSWORD = "LA_APP_PASSWORD"
RECEIVER = "destino@gmail.com"

def enviar_mail():
    mensaje = "⚠ Alerta: ventas altas!"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER, PASSWORD)
    server.sendmail(SENDER, RECEIVER, mensaje)
    server.quit()

ventas = 120

if ventas > 100:
    enviar_mail()

print("Email enviado.")
