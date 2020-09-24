import tweepy
import networkx as nx
import json
import yaml
import argparse

#--------------------------------------#
# Parse Command Line Arguments
#--------------------------------------#
parser = argparse.ArgumentParser(description='Download mutual connects between Twitter users.')
parser.add_argument('--add', dest='users_to_add', nargs='+', 
                    action='store',
                    help='Add users to the search list.')
args = parser.parse_args()
#----------------------------------------#
# Set Up Tweepy
#----------------------------------------#
# Get keys
with open("keys.yaml", "r") as file:
    keys = yaml.load(file, Loader = yaml.SafeLoader)

auth = tweepy.OAuthHandler(keys['twitter']['api_key'], keys['twitter']['api_secret_key'])
auth.set_access_token(keys['twitter']['access_token'], keys['twitter']['access_token_secret'])

# Construct the API instance
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

#---------------------------------------#
# Load in previous data.
#---------------------------------------#
# Try to read graph, otherwise reinit.
try:
    G = nx.read_adjlist("graph.adjlist")
except FileNotFoundError:
    print("Could not find graph file. Initialised new graph.")
    G = nx.Graph()

# Try to read users to check, otherwise reinit.
try:
    with open('users_to_check.list', 'r') as filehandle:
        users_to_check = json.load(filehandle)
except FileNotFoundError:
    print("Could not find users to check. Initialised new empty list.")
    users_to_check = []

# Add users to the checking list.
if (args.users_to_add is not None):
    users_to_check.extend(args.users_to_add)
    
#--------------------------------------#
# Data Collecting Loop
#--------------------------------------#
try:
    while True:
        current_user = users_to_check.pop(0)
        print(f"Current user: {current_user}")

        print("Getting friends...")
        friends = set()
        # Iterate through all of the current user's friends and put in list
        for friend in tweepy.Cursor(api.friends, id=current_user, count=200).items():
            # Process the friend here
            friends.add(friend.screen_name)

        print("Getting followers...")
        followers = set()
        # Iterate through all of the current user's followers and put in list
        for follower in tweepy.Cursor(api.followers, id=current_user, count=200).items():
            # Process the friend here
            followers.add(follower.screen_name)

        mutuals = friends.intersection(followers)
        
        # Add any mutuals who have not been seen before to set to be checked
        users_to_check.extend(mutuals.difference(set(G.nodes)))
        
        G.add_edges_from(map(lambda x: (current_user, x), mutuals))

except KeyboardInterrupt:
    # if we cancel the current user, add them back to the list. 
    users_to_check.insert(0, current_user)

finally:
    # Write Graph
    nx.write_adjlist(G, "graph.adjlist")
    # Write User list
    with open('users_to_check.list', 'w') as filehandle:
        json.dump(users_to_check, filehandle)