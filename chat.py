from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists
# required variables
OPENAI_API_KEY = env("OPENAI_API_KEY") 
print(OPENAI_API_KEY)