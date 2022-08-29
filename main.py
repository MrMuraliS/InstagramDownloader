import os
import shutil

import instaloader
from fake_useragent import UserAgent
from instaloader import Post, Profile


def get_the_link_id(link: str) -> str:
    """
    This function does take the link and return the ID of the link.
    Example link is ==> https://www.instagram.com/p/ChzjcMkMd9X/?utm_source=ig_web_copy_link
    Example ID ==> ChzjcMkMd9X
    :param link:
    :return:
    """
    return link.split('/')[4]


def get_user_agent() -> str:
    """
    this function will return the fake user agent so websites may not be able to block your IP/User Agent.
    :return:
    """
    try:
        ua = UserAgent(verify_ssl=False)
        return ua.random
    except Exception as e:
        get_user_agent()


class InstaDownloader:

    def __init__(self):
        self.instance = instaloader.Instaloader(user_agent=get_user_agent())
        self.instance.login(user="stfugtfout", passwd="Asdf@121")
        if os.path.exists("folderName"): shutil.rmtree("folderName")
        if os.path.exists('Stories'): shutil.rmtree("Stories")

    def download_single_post(self, post_link: str):
        """
        This method will help you download single post of Instagram.
        :param post_link:
        :return:
        """
        post_id = get_the_link_id(post_link)
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
        self.instance.download_stories(userids=[profile.userid], filename_target=f'Stories')


obj = InstaDownloader()
# obj.download_single_post("https://www.instagram.com/p/Ch1pgKRLj6M/?utm_source=ig_web_copy_link")
# obj.download_hashtag("music", 5)
obj.download_instagram_stories("addicted_to__memes")
