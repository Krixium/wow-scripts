import json
import os
import requests

# TODO: make this file actually do something


def printResponse(response):
    print(json.dumps(response.json(), indent=2))


def run(query, variables):
    access_token = ""
    with requests.Session() as session:
        session.auth = (
            os.environ.get("wclUserID") or "",
            os.environ.get("wclUserSecret") or "",
        )
        response = session.post(
            "https://www.warcraftlogs.com/oauth/token",
            data={"grant_type": "client_credentials"},
        )

        if response.status_code == 200:
            access_token = response.json().get("access_token")
        else:
            print(response)

    if access_token == "":
        print("could not get access token")
        return

    with requests.Session() as session:
        session.headers = {"Authorization": f"Bearer {access_token}"}
        response = session.get(
            "https://www.warcraftlogs.com/api/v2/client",
            json={"query": query, "variables": variables},
        )

        printResponse(response)


if __name__ == "__main__":
    query = """
    query($code:String){
        reportData {
            report(code:$code){
                fights{
                    id
                    name
                    startTime
                    endTime
                }
            }
        }
    }
    """
    variables = {"code": "cRYTLBPfnXGNpV96"}
    run(query, variables)
