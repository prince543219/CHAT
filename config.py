from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 29565251))
API_HASH = getenv("API_HASH", "afaa92769fc8a8f85dbf1a11c2b41958")
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7932293909:AAFecHjroKHn6GpI1fNdQRcTjJGvejUTyBU")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://surajit54321:surajit54321@cluster0.7mn37.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", "7921906677"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/prince543219/CHAT")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
SUPPORT_GRP = "UmbrellaUCorp"
SUPPORT_GRP = getenv("SUPPORT_GRP", "UmbrellaUCorp")
UPDATE_CHNL = getenv("UPDATE_CHNL", "moviiieeeesss")
# GIT TOKEN ( if your edited repo is private)
OWNER_USERNAME = "johnnyzheycxee"
GIT_TOKEN = getenv("GIT_TOKEN", "")
    
