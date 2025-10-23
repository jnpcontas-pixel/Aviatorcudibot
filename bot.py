import telebot

TOKEN = '8271463189:AAFByFlzypRrm_WJyIBbMic8pFn2aXYyxs8'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'ajuda'])
def send_welcome(message):
    bot.reply_to(message, "👋 Olá! Eu sou o AviatorCudibot.\n\nComandos disponíveis:\n/sinal → Receber sinal\n/ajuda → Ver comandos")

@bot.message_handler(commands=['sinal'])
def send_signal(message):
    bot.reply_to(message, "🎯 Sinal: Entrar após 1.60x e sair em 2x ✅")

print("✅ AviatorCudibot está ativo e online!")
bot.polling()
