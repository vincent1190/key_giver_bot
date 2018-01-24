from discord.ext.commands import Bot
import asyncio


def read_in_content:
  # adding in the key list
  with open('keys.txt','r') as key_file:
    keys=key_file.read()
    keys=keys.split('\n')

  # adding in the old keys/user list
  #format for each line is [user ' ' old_key] as in user, space, then old_key
  with open('old_keys.txt','r') as old_key_file:
    for i in old_key_file.readlines():
      used_keys.append(i.split())

def refresh(key_list,old_key_list):
  # updating old and new key files
  with open('keys.txt','w')as updated_key_file:
    for updated_key in key_list:
      updated_key_file.write(updated_key+'\n')

  with open('used_keys.txt','w') as updated_used_key_file:
    for used in old_key_list:
      updated_used_key_file.write(used[0]+' '+used[1]+'\n')

client = Bot('/keybot_', pm_help=False)
keys=[]

#users who have been sent a key
used_keys=[]

read_in_content()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.command()
async def send_key(message):
  # this will send the key
  if not any(message.author in users for users in used) :
    print('{} not in sent_user list. Sending key' .format(message.author))
    await client.send_message(message.author,keys[0])
    await client.send_message(message.author,
                              'Hope you enjoy it :)\n'
                              'I would appreciate an upvote or comment on reddit so people know its legit\n'
                              'Please remember it is multiplayer only (2-4 players) best with 4.'
                              'So you should get a group together through Discord in the #lookingforgroup channel.\n'
                              'When you\'ve had enough time to try out full 4 player games, it would be cool if you'
                              'would share your support on Reddit to spread the word about the game.\n')
    print('Key sent to {}' .format(message.author))

    # now adding the old key and username to old list and removing used key from the keys list
    print('adding user ({}) and sent key ({}) to used key list' .format(keys[0],message.author))
    used_keys.append([message.author,keys[0]])

    print('deleting key: ({}) from un-used key list' .format(keys[0]))
    keys.remove(keys[0])
    
    print('refreshing lists')
    refresh(keys,used_keys) 

# enter your specific token into this. look to youtube for how to
# make a discord bot with python to find out how to do this
client.run('token')
    
