import discord
import asyncio

client = discord.Client()
#phrase that will have your key be sent to the user that sent the post
key_phrase='#keyplease'

#user who has been sent a key
sent_users=[]

#keys that have been sent to a user
used_keys=[]

#reads in any usernames or keys that have already been sent out
with open(r'sent_user_list.txt',r+) as users:
    for i in users:
        sent_users.append(i.strip('\n'))

with open(r'used_keys.txt','r+') as old_keys:
    for j in old_keys:
        used_keys.append(j.strip('\n'))





'''list of un-used keys. please enter each key in similar format to this
['235FP-45GY1-E56F5','3RG45-GHU75-DPI67','4GH6H-KHP76-67YGG',....]'''
not_used_keys=['enter','each','key','in','here']



sent_users=[]

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith(key_phrase) and message.author not in sent_users:
        print('{} not in sent_user list. Sending key' .format(message.author))
        await client.send_message(message.author,not_used_keys[0])
        await client.send_message(message.author,
                                  'Hope you enjoy it :)\n'
                                  'I would appreciate an upvote or comment on reddit so people know its legit\n'
                                  'Please remember it is multiplayer only (2-4 players) best with 4.'
                                  'So you should get a group together through Discord in the #lookingforgroup channel.\n'
                                  'When you\'ve had enough time to try out full 4 player games, it would be cool if you'
                                  'would share your support on Reddit to spread the word about the game.\n')
        print('Key sent to {}' .format(message.author))
        if not_used_keys[0] not in used_keys:
            print('adding sent key ({}) to used key list' .format(not_used_keys[0]))
            used_keys.append(not_used_keys[0])
            print('deleting key :  {}   from un-used key list' .format(not_used_keys[0]))
            del not_used_keys[0]
            print('adding {} to sent_user list' .format(message.author))
            sent_users.append(message.author)
                                


                                  


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



# enter your specific token into this. look to youtube for how to
# make a discord bot with python to find out how to do this
client.run('token')
    
