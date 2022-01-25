import instaloader

# making instances
ig = instaloader.Instaloader()

while(True):
    # type of account
    type_of_account =input(" Enter Public or Private : ")

    if(type_of_account=="Public" or type_of_account =="public" or type_of_account =="PUBLIC"):
        Username = input("Enter Insta username : ")
        ig.download_profile(Username)
        print("Download Complete ")
        break

    #     if account id private only profile picture can be downloadable
    elif(type_of_account=="Private" or type_of_account=="private" or type_of_account =="PRIVATE"):
        Username = input("Enter Insta username : ")
        ig.download_profile(Username, profile_pic_only=True)
        print("Download Complete ")
        break
    



