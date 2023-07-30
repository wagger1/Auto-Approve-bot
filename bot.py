from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4',
    'https://telegra.ph/file/506898de518534ff68ba0.mp4',
    'https://telegra.ph/file/dae0156e5f48573f016da.mp4',
    'https://telegra.ph/file/3e2871e714f435d173b9e.mp4',
    'https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4',
    'https://telegra.ph/file/876edfcec678b64eac480.mp4',
    'https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4',
    'https://telegra.ph/file/b4834b434888de522fa49.mp4'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    buttons = [[
                 InlineKeyboardButton("🍷мαιи ϲнαииєℓ", url="https://t.me/CxMaxTG")
                 ],[
                 InlineKeyboardButton("🎯 gяουρ 1", url="https://t.me/CinemaxpressTM"),
                 InlineKeyboardButton("🎯 gяουρ 2", url="https://t.me/Cinemabasar")
              ]]                      
    reply_markup = InlineKeyboardMarkup(buttons)
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_message(kk.id, "**нєγ {} 🫂\nγουя яєգυєѕτ το נοιи {}\n\nωαѕ αϲϲєρτє∂**".format(m.from_user.mention, m.chat.title), reply_markup=reply_markup)
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            buttons = [[
                        InlineKeyboardButton("● α∂∂ мє το gяουρ οя ϲнαииєℓ ●", url="https://t.me/CxAutoBot?startgroup")
                        ],[
                        InlineKeyboardButton("🍷мαιи ϲнαииєℓ", url="https://t.me/CxMaxTG")
                      ]]          
            add_user(m.from_user.id)
            reply_markup = InlineKeyboardMarkup(buttons)
            await m.reply(
            text="<b>нєγ {} 🫂\nα∂∂ τнιѕ ϐοτ το γουя ϲнαииєℓѕ οя gяουρ το αϲϲєρτ נοιи яєգυєѕτѕ αυτοмατιϲαℓℓγ 😊\n\nѕнαяє αи∂ ѕυρροяτ υѕ 💪</b>".format(m.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
           )
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🥵ϲℓιϲκ нєяє🥵", url="https://t.me/CxAutoBot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**нєγ {} 🫂\nϲℓιϲκ ϐєℓοω το υѕє мє ☺🙈**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" 🥵 мγяαи ѕταяτє∂")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(" 💌 ᑕᕼᗴᑕᏦ ᗩᏀᗩᏆᑎ 💌  ", "chk")
                ]
            ]
        )
        await m.reply_text("**ѕοяяγ γου ∂ι∂и'τ נοιи мγ ϲнαииєℓ\n\nյօíղ հҽɾҽ 👉 @{} αƒτєя נοιиιиg ϲℓιϲκ τнє ϐєℓοω 💌 ϲнєϲκ αgαιи 💌 ϐυττοи 👇🏻**".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🍷мαιи ϲнαииєℓ", url="https://t.me/CxMaxTG")
                    ],[
                        InlineKeyboardButton("🎯 gяουρ 1", url="https://t.me/CinemaxpressTM"),
                        InlineKeyboardButton("🎯 gяουρ 2", url="https://t.me/Cinemabasar")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("**нєγ {} 🫂\nα∂∂ τнιѕ ϐοτ το γουя ϲнαииєℓѕ οя gяουρ το αϲϲєρτ נοιи яєգυєѕτѕ αυτοмατιϲαℓℓγ 😊\n\nѕнαяє αи∂ ѕυρροяτ υѕ 💪**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" 🥵 мγяαи ѕταяτє∂")
    except UserNotParticipant:
        await cb.answer("ᒍᝪᏆᑎ ᐯᖇᝪ 🥵")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("I'm Alive Now!")
app.run()
