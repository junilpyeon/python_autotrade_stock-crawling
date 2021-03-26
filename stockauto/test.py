import requests


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer "+token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


myToken = "xoxb-123*****"

post_message('xoxb-1852632646227-1902785869699-V0rh72GiMUKnsdXam8NhQ8go',
             "#-c-java", "junil hi")
