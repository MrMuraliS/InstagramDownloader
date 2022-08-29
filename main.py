import getpass
from Instaloader import InstaDownloader

if __name__ == "__main__":
    UserID = input("Please enter your Instagram ID: ")
    Password = getpass.getpass("Please enter your Instagram Password: ")
    login = InstaDownloader(UserID, Password)

    while True:
        print("Please select the required option from below: \n")
        print(
            "1. Download single post using Instagram Link.\n"
            "2. Download posts using hashtag.\n"
            "3. Download the stories of the required user.\n"
            "4. Download your saved posts.\n"
            "5. Download entire profile of required user.\n"
            "6. Download profile pic of required user.\n"
            "7. Exit.\n"
        )

        try:
            user_input = int(
                input("Please enter your choice appropriately between 1-7: \n")
            )
            if user_input == 7:
                print("Thank you for using our services. Bye..\n")
                break
            elif user_input > 7:
                print("You have selected wrong option, Please try again..\n")
                continue
            else:
                if user_input == 1:
                    link = input("\n Please enter post link: ")
                    login.download_single_post(link)
                elif user_input == 2:
                    hashtag = input("Enter the tag: ")
                    count = int(
                        input("Enter the number of posts you wanted to download: ")
                    )
                    login.download_hashtag()
                elif user_input == 3:
                    user_id = input("Please enter user ID: ")
                    login.download_instagram_stories(user_id)
                elif user_input == 4:
                    login.download_your_saved_posts()
                elif user_input == 5:
                    user_id = input("Please enter user ID: ")
                    login.download_entire_profile(user_id)
                elif user_input == 6:
                    user_id = input("Please enter user ID: ")
                    login.download_profile_pic(user_id)

        except Exception as e:
            print(e)
            print()
            print(
                "INVALID OPTION, Please select the options correctly between 1-7.\n\n"
            )
