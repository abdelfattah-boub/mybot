import random 
import telebot
from telebot import types
import requests
import time
from telebot import custom_filters
from telebot.custom_filters import TextFilter, TextMatchFilter, IsReplyFilter
from telebot.handler_backends import ContinueHandling


BOTTOKEN =  "5927806541:AAF725ZDHo-bPno-VwLQXOMH6UxLWk-fSHQ"
bot = telebot.TeleBot(BOTTOKEN)


a = ["بسم الله","اللهم عافني في بدني، اللهم عافني في سمعي، اللهم عافني في بصري.",
"لاحول ولا قوة إلا بالله.",
"اللهم إني أسألك الجنة وأعوذ بك من النار",
"حسبي الله ونعم الوكيل.",
"قدر الله وماشاه فعل",
"اللهم إني أسألك برحمتك التي وسعت كل شيء أن تغفر لي",
"ربنا أفرغ علينا صبرًا، وثبت أقدامنا، وانصرنا على القوم الكافرين",
"ربنا آتنا في الدنيا حسنة، وفي الآخرة حسنة، وقنا عذاب النار",
"ربنا إننا آمنا فاغفر لنا ذنوبنا وقنا عذاب النار",
"اللهم إني أسألك برحمتك التي وسعت كل شي أن تغفر لي",
"سبحان ربي العظيم",
"سبحانك اللهم ربنا وبحمدك"]

b = ["Oh Allah, Grant Health to my body, Oh Allah Grant health to my hearing, Oh Allah, Grant health to my sight",
"There is no might nor power except with Allah",
"Oh Allah, I ask For Paradise, and Protection from the fire",
"Allah is sufficient for me, and how fine a trust he is",
"Allah has decreed and what he wills, he does",
"O Allah,  I ask you by your mercy which envelopes all things, that you forgive me",
"Our Lord! Pour forth on us patience and make us ” victorious over the disbelieving people",
"Our Lord!We have indeed believed, so forgive us our, sins and save us from the punishment of the Fire",
"Our Lord! Let not our hearts deviate (from the truth) ” after You have guided us, and grant us mercy from You. Truly, You are the Bestower",
"Allaah has decreed and what he wills , he does",
"Allaah is sufficient for me . and how fine a trustee he is",
"There is no might nor power except with Allaah"
]

c = ["О Аллах, Даруй здоровье моему телу, О Аллах Даруй здоровье моему слуху, О Аллах, Даруй здоровье моему зрению",
"Нет ни могущества, ни силы, кроме как с Аллахом",
"О Аллах, я прошу Рая и Защиты от огня",
"Аллаха достаточно для меня, и как хорошо он доверяет",
"Аллах повелел и то, что пожелает, он делает",
"О Аллах, я прошу Тебя по Твоей милости, которая окутывает все сущее, чтобы Ты простил меня",
"Господь наш! Изливайте на нас терпение и делайте нас «победоносными над неверующим народом»",
"Господь наш! Мы действительно уверовали, так простите нам наши грехи и спасите нас от наказания Огнем",
"Господь наш! Пусть сердца наши не отклоняются (от истины)» после того, как Ты направил нас, и даруй нам милость от Тебя. Воистину, Ты – Бестауэр",
"Аллах повелел и то, что пожелает, он делает",
"Аллаха мне достаточно. и насколько он прекрасен с доверенным лицом",
"Нет ни могущества, ни силы, кроме как с Аллахом"
]



@bot.message_handler(commands=["start"])
def welcom(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('🇸🇦 العربية')
    itembtn2 = types.KeyboardButton('English 🇺🇸')
    itembtn3 = types.KeyboardButton('Русский 🇷🇺')
    markup.add(itembtn1, itembtn2,itembtn3)
    bot.send_message(message.chat.id,
     "السلام عليكم ورحمة الله وبركاته\nمرحبا بك في منصة اذكار المسلم على التلغرام \nبدايةً, فضلا قم باختيار اللغة المفضلة لك ...\n"+
     "Hi ,\nWelcome with us in athkar Bot ,\nStarting , please choose the language you prefer ...\n "+
     "Привет,\nДобро пожаловать с нами в athkar Bot,\nПусковой,пожалуйста, выберите язык, который вы предпочитаете ...")
    bot.send_message(message.chat.id
    , "فضلا قم باختيار اللغة :\nPlease select the language:\nПожалуйста, выберите язык:", reply_markup=markup)


@bot.message_handler(text='🇸🇦 العربية')
def hello_handler(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('🟥عالي')
    itembtn2 = types.KeyboardButton('🟧متوسط')
    itembtn3 = types.KeyboardButton('🟨منخفض')
    itembtn4 = types.KeyboardButton('مخصص➰')
    markup.add(itembtn1, itembtn2, itembtn3,itembtn4)
    bot.send_message(message.chat.id, "حسنا,الان يمكنك اختيار معدل ارسال الاذكار.",
    reply_markup = types.ReplyKeyboardRemove())
    time.sleep(1)
    bot.send_message(message.chat.id, "فضلا اختر معدل الارسال:", reply_markup=markup)


@bot.message_handler(text='🟥عالي')
def avrg(message):
    bot.send_message(message.chat.id,"حسنا,سيتم ارسال دعاء او ذكر عشوائي بعد كل نصف ساعة.",
    reply_markup = types.ReplyKeyboardRemove())
    while True:
        time.sleep(1800)
        AA = random.choice(a)
        bot.send_message(message.chat.id,AA)


@bot.message_handler(text='🟧متوسط')
def avrg(message):
    bot.send_message(message.chat.id,"حسنا,سيتم ارسال دعاء او ذكر عشوائي بعد كل ساعة و نصف.",
    reply_markup = types.ReplyKeyboardRemove())
    while True:
        time.sleep((5400))
        AA = random.choice(a)
        bot.send_message(message.chat.id,AA)


@bot.message_handler(text='🟨منخفض')
def avrg(message):
    bot.send_message(message.chat.id,"حسنا,سيتم ارسال دعاء او ذكر عشوائي بعد كل اربع ساعات .",
    reply_markup = types.ReplyKeyboardRemove())
    while True:
        time.sleep(14400)
        AA = random.choice(a)
        bot.send_message(message.chat.id,AA)
 

                
@bot.message_handler(text='مخصص➰')
def hello_handler(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton("ادخال الوقت بالثواني S")
    itembtn2 = types.KeyboardButton("ادخال الوقت بالدقائق M")
    itembtn3 = types.KeyboardButton("ادخال الوقت بالساعات H")
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message,"الان اختر طريقة الادخال:",reply_markup=markup)



@bot.message_handler(text="ادخال الوقت بالثواني S")
def hello_handler(message):
    bot.reply_to(message,"حسنا ,ادخل الوقت: \n عند ادخال الرقم يجب كتابة ars \n مثل: ars 20",
    reply_markup = types.ReplyKeyboardRemove())
@bot.message_handler(text=TextFilter(starts_with='ars', ignore_case=True))  # STark, sTeve, stONE
def num(message: types.Message):
    num = message.text.split()
    
    if num[1] is not str:
        bot.send_message(message.chat.id,f"حسنا,سيتم ارسال دعاء او ذكر عشوائي بعد {num[1]} ثانية.")
        while True:
            time.sleep(float(num[1]))
            AA = random.choice(a)
            bot.send_message(message.chat.id,AA)
    else:
        bot.reply_to(message,"رجاءا ادقل رقما:")
    return ContinueHandling()
        


@bot.message_handler(text="ادخال الوقت بالدقائق M")
def hello_handler(message):
    bot.reply_to(message,"حسنا ,ادخل الوقت: \n عند ادخال الرقم يجب كتابة arm \n مثل: arm 20",
    reply_markup = types.ReplyKeyboardRemove())
@bot.message_handler(text=TextFilter(starts_with='arm', ignore_case=True))  # STark, sTeve, stONE
def num(message: types.Message):
    num = message.text.split()
    
    if num[1] is not str:
        bot.send_message(message.chat.id,f"حسنا,سيتم ارسال دعاء او ذكر عشوائي بعد {num[1]} دقيقة.")
        s = float(num[1]) * 60
        while True:
            time.sleep(s)
            AA = random.choice(a)
            bot.send_message(message.chat.id,AA)
    else:
        bot.reply_to(message,"رجاءا ادقل رقما:")
    return ContinueHandling()


@bot.message_handler(text="ادخال الوقت بالساعات H")
def hello_handler(message):
    bot.reply_to(message,"حسنا ,ادخل الوقت: \n عند ادخال الرقم يجب كتابة arh \n مثل: arh 20",
    reply_markup = types.ReplyKeyboardRemove())
@bot.message_handler(text=TextFilter(starts_with='arh', ignore_case=True))  # STark, sTeve, stONE
def num(message: types.Message):
    num = message.text.split()
    
    if num[1] is not str:
        bot.send_message(message.chat.id,f"حسنا,سيتم ارسال دعاء او ذكر عشوائي بعد {num[1]} ساعة.")
        s = float(message.text) * 3600
        while True:
            time.sleep(float(num[1]))
            AA = random.choice(a)
            bot.send_message(message.chat.id,AA)
    else:
        bot.reply_to(message,"رجاءا ادقل رقما:")
    return ContinueHandling()
        


#!######################################################################################
#!######################################################################################


@bot.message_handler(text='English 🇺🇸')
def hello_handler(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('🟥often')
    itembtn2 = types.KeyboardButton('🟧normally')
    itembtn3 = types.KeyboardButton('🟨rarely')
    itembtn4 = types.KeyboardButton('custom➰')
    markup.add(itembtn1, itembtn2, itembtn3,itembtn4)
    bot.send_message(message.chat.id, "OK ,Now you can choose the sending avrage:",
    reply_markup = types.ReplyKeyboardRemove())
    time.sleep(1)
    bot.send_message(message.chat.id, "Pleas select one of them:", reply_markup=markup)
    @bot.message_handler(text=['🟥often','🟧normally','🟨rarely'])
    def avrg(message):
        if message.text == '🟥often' :
            bot.send_message(message.chat.id,"OK, The bot will send prayers or athkar after each 30 min",
            reply_markup = types.ReplyKeyboardRemove())
            while True:
                time.sleep(1800)
                BB = random.choice(b)
                bot.send_message(message.chat.id,BB)
        elif message.text == '🟧normally' :
            bot.send_message(message.chat.id,"OK, The bot will send prayers or athkar after each 90 min",
            reply_markup = types.ReplyKeyboardRemove())
            while True:
                time.sleep(5400)
                BB = random.choice(b)
                bot.send_message(message.chat.id,BB)
        elif message.text == '🟨rarely' : 
            bot.send_message(message.chat.id,"OK, The bot will send prayers or athkar after each 4 h",
            reply_markup = types.ReplyKeyboardRemove())
            while True:
                time.sleep(14400)
                BB = random.choice(b)
                bot.send_message(message.chat.id,BB)



                
@bot.message_handler(text='custom➰')
def hello_handler(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton("Enter the time in seconds")
    itembtn2 = types.KeyboardButton("Enter the time in minutes")
    itembtn3 = types.KeyboardButton("Enter the time in hours")
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message,"Now , choose the enter the input method :",reply_markup=markup)



@bot.message_handler(text="Enter the time in seconds")
def hello_handler(message):
    bot.reply_to(message,"Enter the time in seconds \nAdd ens before the numer\nEX: ens 20 ",
    reply_markup = types.ReplyKeyboardRemove())
@bot.message_handler(text=TextFilter(starts_with='ens', ignore_case=True))  # STark, sTeve, stONE
def num(message: types.Message):
    num = message.text.split()
    
    if num[1] is not str:
        bot.send_message(message.chat.id,f"Great,It will send random prayers or athkar in each {num[1]} seconds.")
        while True:
            time.sleep(float(num[1]))
            BB = random.choice(b)
            bot.send_message(message.chat.id,BB)
    else:
        bot.reply_to(message,"Please enter a number")
    return ContinueHandling()
        


@bot.message_handler(text="Enter the time in minutes")
def hello_handler(message):
    bot.reply_to(message,"Enter the time in minuts \nAdd enm before the numer\nEX: enm 20 ",
    reply_markup = types.ReplyKeyboardRemove())
@bot.message_handler(text=TextFilter(starts_with='enm', ignore_case=True))  # STark, sTeve, stONE
def num(message: types.Message):
    num = message.text.split()
    
    if num[1] is not str:
        bot.send_message(message.chat.id,f"Great,It will send random prayers or athkar in each {num[1]} minuts.")
        s = float(num[1]) * 60
        while True:
            time.sleep(s)
            BB = random.choice(b)
            bot.send_message(message.chat.id,BB)
    else:
        bot.reply_to(message,"Please enter a number")
    return ContinueHandling()
        



@bot.message_handler(text="Enter the time in hours")
def hello_handler(message):
    bot.reply_to(message,"Enter the time in hours \nAdd enh before the numer\nEX: enh 20 ",
    reply_markup = types.ReplyKeyboardRemove())
@bot.message_handler(text=TextFilter(starts_with='enh', ignore_case=True))  # STark, sTeve, stONE
def num(message: types.Message):
    num = message.text.split()
    
    if num[1] is not str:
        bot.send_message(message.chat.id,f"Great,It will send random prayers or athkar in each {num[1]} hours.")
        s = float(message.text) * 3600
        while True:
            time.sleep(float(num[1]))
            BB = random.choice(b)
            bot.send_message(message.chat.id,BB)
    else:
        bot.reply_to(message,"Please enter a number")
    return ContinueHandling()
        


#!#########################################################################################
#!#########################################################################################

@bot.message_handler(text='Русский 🇷🇺')
def hello_handler(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('🟥часто')
    itembtn2 = types.KeyboardButton('🟧обычно')
    itembtn3 = types.KeyboardButton('🟨редко')
    itembtn4 = types.KeyboardButton('обычай➰')
    markup.add(itembtn1, itembtn2, itembtn3,itembtn4)
    bot.send_message(message.chat.id, "OK ,Теперь вы можете выбрать отправку скорость:",
    reply_markup = types.ReplyKeyboardRemove())
    time.sleep(1)
    bot.send_message(message.chat.id, "Пожалуйста, выберите один из них:", reply_markup=markup)
    @bot.message_handler(text=['🟥часто','🟧обычно','🟨редко'])
    def avrg(message):
        if message.text == '🟥часто' :
            bot.send_message(message.chat.id,"Хорошо, бот будет отправлять молитвы или аткар через каждые 30 минут",
            reply_markup = types.ReplyKeyboardRemove())
            while True:
                time.sleep(1800)
                CC = random.choice(c)
                bot.send_message(message.chat.id,CC)
        elif message.text == '🟧обычно' :
            bot.send_message(message.chat.id,"Хорошо, бот будет отправлять молитвы или аткар через каждые 90 минут",
            reply_markup = types.ReplyKeyboardRemove())
            while True:
                time.sleep(5400)
                CC = random.choice(c)
                bot.send_message(message.chat.id,CC)
        elif message.text == '🟨редко' : 
            bot.send_message(message.chat.id,"Хорошо, бот будет отправлять молитвы или аткар через каждые 4 часа",
            reply_markup = types.ReplyKeyboardRemove())
            while True:
                time.sleep(14400)
                CC = random.choice(c)
                bot.send_message(message.chat.id,CC)



                
@bot.message_handler(text='обычай➰')
def hello_handler(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton("Введите время в секундах")
    itembtn2 = types.KeyboardButton("Введите время в минутах")
    itembtn3 = types.KeyboardButton("Введите время в часах")
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message,"Now , choose the enter the input method :",reply_markup=markup)



@bot.message_handler(text="Введите время в секундах")
def hello_handler(message):
    bot.reply_to(message,"Введите время в секундах \nДобавить rus перед числом\nEX: rus 20 ",
    reply_markup = types.ReplyKeyboardRemove())
@bot.message_handler(text=TextFilter(starts_with='rus', ignore_case=True))  # STark, sTeve, stONE
def num(message: types.Message):
    num = message.text.split()
    
    if num[1] is not str:
        bot.send_message(message.chat.id,f"Великий, он будет посылать случайные молитвы или аткар в каждом {num[1]} секунда.")
        while True:
            time.sleep(float(num[1]))
            CC = random.choice(c)
            bot.send_message(message.chat.id,CC)
    else:
        bot.reply_to(message,"Пожалуйста, введите номер")
    return ContinueHandling()
        


@bot.message_handler(text="Введите время в минутах")
def hello_handler(message):
    bot.reply_to(message,"Введите время в минутах \nДобавить rum перед числом\nEX: rum 20 ",
    reply_markup = types.ReplyKeyboardRemove())
@bot.message_handler(text=TextFilter(starts_with='rum', ignore_case=True))  # STark, sTeve, stONE
def num(message: types.Message):
    num = message.text.split()
    
    if num[1] is not str:
        bot.send_message(message.chat.id,f"Великий, он будет посылать случайные молитвы или аткар в каждом {num[1]} протокол.")
        s = float(num[1]) * 60
        while True:
            time.sleep(s)
            CC = random.choice(c)
            bot.send_message(message.chat.id,CC)
    else:
        bot.reply_to(message,"Пожалуйста, введите номер")
    return ContinueHandling()
        



@bot.message_handler(text="Введите время в часах")
def hello_handler(message):
    bot.reply_to(message,"Введите время в минутах \nДобавить ruh перед числом\nEX: ruh 20 ",
    reply_markup = types.ReplyKeyboardRemove())
@bot.message_handler(text=TextFilter(starts_with='ruh', ignore_case=True))  # STark, sTeve, stONE
def num(message: types.Message):
    num = message.text.split()
    
    if num[1] is not str:
        bot.send_message(message.chat.id,f"Великий, он будет посылать случайные молитвы или аткар в каждом {num[1]} Часов.")
        s = float(message.text) * 3600
        while True:
            time.sleep(float(num[1]))
            CC = random.choice(c)
            bot.send_message(message.chat.id,CC)
    else:
        bot.reply_to(message,"Пожалуйста, введите номер")
    return ContinueHandling()



    

bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.infinity_polling()