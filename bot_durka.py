import discord
import random
from bot_logic import gen_pass

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

intents = discord.Intents.default()
intents.message_content = True

PREFIX = "!"  # Префикс для команд

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)
    
    
    if message.content.startswith(PREFIX + "rps"):
        choices = ["камень", "бумага", "ножницы","вода","воздух","огонь","губка"]
        bot = random.choice(choices)
        user = message.content.split()[-1].lower()
        if user not in choices:
            await message.channel.send("Неверный выбор. Попробуйте снова.")
            return
            
    if bot == user:
        result = "Ничья!"
    elif (
        (bot == "камень" and user == "бумага") or
        (bot == "ножницы"and user == "бумага") or
        (bot == "камень" and user == "ножницы") or
        (bot == "огонь"  and user == "бумага")  or
        (bot == "огонь"  and user == "губка")  or
        (bot == "губка"  and user == "камень")  or
        (bot == "камень"  and user == "огонь")  or
        (bot == "огонь"  and user == "ножницы")  or
        (bot == "ножницы"  and user == "губка")  or
        (bot == "губка"  and user == "бумага")  or
        (bot == "бумага"  and user == "воздух")  or
        (bot == "воздух"  and user == "вода")  or
        (bot == "вода"  and user == "камень")  or
        (bot == "ножницы"  and user == "воздух")  or
        (bot == "губка"  and user == "воздух")  or
        (bot == "губка"  and user == "вода")  or
        (bot == "бумага"  and user == "вода")  or
        (bot == "воздух"  and user == "огонь")  or
        (bot == "воздух"  and user == "камень")  or
        (bot == "вода"  and user == "ножницы")  or
        (bot == "вода"  and user == "огонь")  
    ):
        result = "Вы проиграли!"
    else:
        result = "Вы победили!"
        
    await message.channel.send(f"Бот выбрал: {bot}\nВы выбрали: {user}\nРезультат: {result}")

client.run('MTEzNDQ5MTM2ODIzNzA0Nzg3OA.GbvNHd.I-lJXgASojKC_dEx8oSrZCvmOUCs8vkfVAZxlw')
