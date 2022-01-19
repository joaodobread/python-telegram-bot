from environs import Env
from marshmallow.validate import Length

env = Env(expand_vars=True, eager=False)
env.read_env('.env')
env.str("TELEGRAM_TOKEN", validate=[Length(1)])
