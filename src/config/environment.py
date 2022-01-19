from environs import Env
from marshmallow.validate import Length, URL

env = Env(expand_vars=True, eager=False)
env.read_env('.env')
env.str("TELEGRAM_TOKEN", validate=[Length(1)])
env.str("MONGO_URI", validate=[URL()])
