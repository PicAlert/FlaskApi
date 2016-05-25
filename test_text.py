from twilio.rest import TwilioRestClient

config = {}
execfile('settings.conf', config)
ACCOUNT_SID = config['ACCOUNT_SID']
AUTH_TOKEN = config['AUTH_TOKEN']
toNum = config["toNum"]
fromNum = config["fromNum"]
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to = toNum,
    from_ = fromNum,
    body = "Hello! This is a test!"
)