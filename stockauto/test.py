import requests


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer "+token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


myToken = "xoxb-123*****"

post_message(
    "xoxb-1852632646227-1852439465682-N1QzuCF493ebuxYVbbf7gKju", "#-c-java", "준일입니다.")
