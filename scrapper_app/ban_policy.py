from rotating_free_proxies.policy import BanDetectionPolicy


class CaptchaPolicy(BanDetectionPolicy):
    """
    Политика банов для proxy.
    """
    def response_is_ban(self, request, response):
        ban = super(CaptchaPolicy, self).response_is_ban(request, response)
        ban = ban or b'captcha' in response.url
        return ban

    def exception_is_ban(self, request, exception):
        return None
