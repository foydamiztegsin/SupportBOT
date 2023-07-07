from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN") 
ADMINS = env.list("ADMINS")


# operatorlarni Telegram ID-larini yozing
support_ids = [
    123456789,
] 