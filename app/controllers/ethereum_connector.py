"""
This module connects to the blockchain server
"""
### Imports ###
import json, httplib2

### Global variables ###

ngrok_tunnel = "http://localhost:5000"
h = httplib2.Http(".cache")

### Functions ###

def fetch_open_contracts():
    """
        Makes a request to the blockchain server and retrieves a list
        of open driver contracts.

        Args:
            None
        Returns:
            A json list of the following:
            {
                "contract_hash": Hash of the contract (string),
                "driver_name": Name of the driver (string),
                "drp": Driver Rating Points (int),
                "rate_per_km": Driver's rate/km (int)
            }
    """
    print "[fetch_open_contracts] Fetching open contracts from blockchain server at %s" % ngrok_tunnel

    url = ngrok_tunnel + "/fetch_open_contracts"

    resp, content = h.request(url, "GET")

    return convert_from_raw(content)

def convert_from_raw(content):
    json_data = json.loads(content)
    return json_data

def send_rider_details(user_details):
    """
        This function is called when the user decides to sign the contract.
        It sends the user's details blockchain server, which will write the data to the block.

        Args:
            user_details (dict) : This should look like the following:
                {
                    "contract_hash": Hash of the contract (string),
                    "rider_id": Rider's id (string),
                    "crp": Customer Rating Points (int),
                    "bitcoin_addr": Rider's bitcoin address (string)
                }
        Returns:
            The Response object from making the request.
    """
    url = ngrok_tunnel + "/send_rider_details"

    resp, content = h.request(
        uri=url,
        method="POST",
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(user_details)
    )
    return resp

def send_flag(flag, data=None):
    """
        Sends a flag/signal to the blockchain server.
        The flag can indicate multiple things. For example, if flag=="finished",
        this tells the server that the ride has ended. Data can be sent along with
        the flag as well.

        Args:
            flag (string)   :   The flag
            data (dict)
        Returns:
            Response object
    """
    url = ngrok_tunnel + "/send_flag"

    dictionary = {
        "flag": flag,
    }

    if data is not None:
        dictionary["data"] = data

    resp, content = h.request(
        uri=url,
        method="POST",
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(dictionary)
    )

    return resp
