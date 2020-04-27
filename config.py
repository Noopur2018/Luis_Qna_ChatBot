#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "fc0d3706-d3a1-4940-81e0-bcecae442512")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "aWDAxvrxKd2dUENCkzRRK.X8wSf97[?]")

    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "463dcaac-0310-4422-9a85-8a3814ae44a3")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "17460967-f805-4584-9e33-69c8fac6b95c")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://slimeqna.azurewebsites.net/qnamaker")

    LUIS_APP_ID = os.environ.get("LuisAppId", "fda4d8d4-4f41-411d-bd6c-b57260929a5e")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "606f23e8934c4b568062b95885503d29")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westus.api.cognitive.microsoft.com")
