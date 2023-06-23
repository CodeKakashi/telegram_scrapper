import json
from apscheduler.schedulers.blocking import BlockingScheduler

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import PeerChannel

from creadentials import API_HASH, API_KEY, PHONE, USERNAME

# Setting configuration values
api_id = API_KEY
api_hash = API_HASH
phone = PHONE
username = USERNAME

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

async def main(phone):
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    me = await client.get_me()

    user_input_channel = input("enter entity (Telegram URL or entity id):")

    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel

    my_channel = await client.get_entity(entity)

    offset = 0
    limit = 100
    all_participants = []

    while True:
        participants = await client(GetParticipantsRequest(
            my_channel, ChannelParticipantsSearch(''), offset, limit,
            hash=0
        ))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)

    all_user_details = []
    for participant in all_participants:
        all_user_details.append(
            {"id": participant.id, "first_name": participant.first_name, "last_name": participant.last_name,
             "user": participant.username, "phone": participant.phone, "is_bot": participant.bot})

    with open('user_data.json', 'w') as outfile:
        json.dump(all_user_details, outfile)

def job():
    with client:
        client.loop.run_until_complete(main(phone))

# Create a scheduler instance
scheduler = BlockingScheduler()

# Schedule the job to run every day at a specific time
scheduler.add_job(job, 'cron', day_of_week='*', hour=12, minute=0)

# Start the scheduler
scheduler.start()
