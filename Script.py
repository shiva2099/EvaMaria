class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
என் பெயர்  <a href=https://t.me/{}>{}</a>, 
நான் திரைப்படத்தை வழங்க முடியும், ஆனால் எனது சேனலான @trvpn க்கு நீங்கள் குழுசேர வேண்டும் 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}

இதைப் பயன்படுத்துவதற்கு முன் எங்கள் முதன்மை நிர்வாகியிடம் அனுமதி கேட்கவும்."""
    ABOUT_TXT = """✯ என் பெயர்: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/Trvpn>Team S.A Developers </a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: Tamil Nadu 
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: தமிழ்
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: Trvpn Server 
✯ 𝚂𝙴𝚁𝚅𝙴𝚁: AWS
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- தமிழ் ஒரு சிறந்த மொழி"""
    MANUELFILTER_TXT = """Help: 
போராடினால் நாம் வெல்லலாம்
வான் வீதியில் கால் வைக்கலாம்
பூலோகமே தேன் சொல்லலாம்
சாகாமலே நாம் வாழலாம்"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- போராடினால் நாம் வெல்லலாம்
வான் வீதியில் கால் வைக்கலாம்
பூலோகமே தேன் சொல்லலாம்
சாகாமலே நாம் வாழலாம்
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/trvpn)</code>

"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
