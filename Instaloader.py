import os
import shutil

import instaloader
from fake_useragent import UserAgent
from instaloader import Post, Profile


class InstaDownloader:
    def __init__(self, insta_id, insta_password):
        self.instance = instaloader.Instaloader(
            user_agent=InstaDownloader.get_user_agent()
        )
        try:
            self.instance.login(user=insta_id, passwd=insta_password)
        except Exception as error:
            print(error)
            print(
                "At this moment, we are not redirecting you back to Login screen, Please stop the program and re-"
                "try again. Few of the functions may not work properly if login is unsuccessful\n"
            )
        if os.path.exists("folderName"):
            shutil.rmtree("folderName")
        if os.path.exists("Stories"):
            shutil.rmtree("Stories")
        if os.path.exists(":saved"):
            shutil.rmtree(":saved")

    @staticmethod
    def get_the_link_id(link: str) -> str:
        """
        This function does take the link and return the ID of the link.
        Example link is ==> https://www.instagram.com/p/ChzjcMkMd9X/?utm_source=ig_web_copy_link
        Example ID ==> ChzjcMkMd9X
        :param link:
        :return:
        """
        return link.split("/")[4]

    @staticmethod
    def get_user_agent() -> str:
        """
        this function will return the fake user agent so websites may not be able to block your IP/User Agent.
        :return:
        """
        try:
            ua = UserAgent(verify_ssl=False)
            return ua.random
        except Exception as error:
            print(error)
            InstaDownloader.get_user_agent()

    def download_single_post(self, post_link: str):
        """
        This method will help you download single post of Instagram.
        :param post_link:
        :return:
        """
        post_id = InstaDownloader.get_the_link_id(post_link)
        post = Post.from_shortcode(self.instance.context, post_id)
        self.instance.download_post(post, target="folderName")

    def download_hashtag(self, tag: str = "sample", count: int = 10):
        """
        This method will download the instagram posts based on the hashtag.
        :param tag:
        :param count:
        :return:
        """
        self.instance.download_hashtag(hashtag=tag, max_count=count)

    def download_instagram_stories(self, user: str):
        """
        This method will download the stories of specified user.
        :param user:
        :return:
        """
        profile = Profile.from_username(self.instance.context, username=user)
        self.instance.download_stories(
            userids=[profile.userid], filename_target=f"Stories"
        )

    def download_your_saved_posts(self):
        """
        If you just want to export your saved posts collections somewhere safe,
        then this method would help you with that.
        :return:
        """
        self.instance.download_saved_posts()

    def download_entire_profile(self, username):
        """
        This is the method to retrieve every single post, video and post carousel of any Instagram account:
        :param username:
        :return:
        """
        self.instance.download_profile(profile_name=username)

    def download_profile_pic(self, username):
        """
        This is to download the profile pic.
        :param username:
        :return:
        """
        self.instance.download_profilepic(username)
