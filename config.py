import os

# ─── Read .env file manually (no dotenv dependency) ───
def _load_env():
    env_file = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.exists(env_file):
        print("[!] .env file not found!")
        return {}
    env = {}
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, _, value = line.partition("=")
            env[key.strip()] = value.strip()
    return env

_env = _load_env()

# ─── Core ───
TOKEN = _env.get("DISCORD_TOKEN", "")
GUILD_ID = int(_env.get("GUILD_ID", "0"))
OWNER_ID = int(_env.get("OWNER_ID", "0"))

# ─── FFmpeg (rooted at c:\test-bot) ───
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FFMPEG_PATH = os.path.join(BASE_DIR, "bin", "ffmpeg", "ffmpeg.exe")

# ─── Colors ───
PRIMARY = 0x5865F2
SUCCESS = 0x57F287
WARNING = 0xFEE75C
ERROR = 0xED4245
MUSIC = 0x9B59B6

# ─── Categories ───
CATEGORIES = {
    "music":      {"emoji": "🎵", "desc": "Music playback & queue management"},
    "moderation": {"emoji": "🛠️", "desc": "Server moderation & management"},
    "utility":    {"emoji": "🔧", "desc": "General utility commands"},
    "fun":        {"emoji": "🎉", "desc": "Fun, memes & entertainment"},
    "economy":    {"emoji": "💰", "desc": "Virtual economy & banking"},
    "games":      {"emoji": "🎮", "desc": "Minigames & activities"},
    "info":       {"emoji": "📊", "desc": "Information & lookups"},
    "admin":      {"emoji": "⚙️", "desc": "Server configuration tools"},
    "owner":      {"emoji": "👑", "desc": "Owner-only commands"},
    "leveling":   {"emoji": "🏆", "desc": "XP & leveling system"},
    "roles":      {"emoji": "🎭", "desc": "Role management"},
    "image":      {"emoji": "🖼️", "desc": "Image manipulation"},
    "misc":       {"emoji": "📁", "desc": "Miscellaneous commands"},
}