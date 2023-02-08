import instaloader
import getpass


old_followers = []
f = open("followers.txt", "r")
for line in f:
    old_followers.append(line)
f.close()

l = instaloader.Instaloader()

username = input("enter ur username: ")
password = getpass.getpass("enter ur password: ")

l.login(username, password)
print("logged in successfull")

profile = instaloader.Profile.from_username(l.context, "s.sina_hosseini.v")

new_followers = []
for follower in profile.get_followers:
    new_followers.append(follower)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower + "\n")
f.close()
