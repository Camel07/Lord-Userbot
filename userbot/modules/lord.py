from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.lord(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`HALLO LORD AKU ADALAH BOT, DAN AKU AKAN SELALU MEMBANTU MU UNTUK BERSENANG-SENANG DI DUNIA TELEGRAM`")
    sleep(2)
    await typew.edit("`\n█████████`"
                     "`\n█▄█████▄█`"
                     "`\n█▼▼▼▼▼`"
                     "`\n█    AKU ADALAH LORD`"
                     "`\n█▲▲▲▲▲`"
                     "`\n█████████`"
                     "`\n ██   ██`")
    sleep(2)
    await typew.edit("`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
                     "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
                     "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈Yo Bro`"
                     "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")
    sleep(1)
    await typew.edit("\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃LORD┊👑`"
                     "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮LORD┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
                     "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`")
    sleep(2)
    await typew.edit("`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
                     "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
                     "`\n┫┈┈ LORD\n┃┈╰╰━━━━╯`"
                     "`\n┗━━┻━┛`")
    sleep(2)
    await typew.edit("`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▏╱▋▋╮┈`"
                     "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
                     "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `")
    sleep(1)
    await typew.edit("` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫★★★┣╯┃ \n╰━┫★★★┣━╯`"
                     "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `")
    sleep(3)
    await typew.edit("`\n█████████`"
                     "`\n█▄█████▄█`"
                     "`\n█▼▼▼▼▼`"
                     "`\n█    AKU ADALAH LORD`"
                     "`\n█▲▲▲▲▲`"
                     "`\n█████████`"
                     "`\n ██   ██`")


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ●  |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣    )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n__Punten__")


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ●  |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣    )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n__Masih Ku Pantau__")


# Create by myself @localheart

CMD_HELP.update({
    "lord":
    "`.lord`\
\nUsage: Bot\
\n\n`.sadboy`\
\nUsage: hiks"
})
