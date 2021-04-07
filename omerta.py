from holehe.core import *
from holehe.localuseragent import *

async def omerta_la(email, client, out) :
    name = "omerta_la"
    domain = "omerta.la"
    method= "register"
    frequent_rate_limit=False

    url = "https://omerta.la/register/"

    headers = {
        'Host': 'omerta.la',
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://omerta.la/register/',
        'Cookie': '__cfduid=d7ebe97392e1232a9da7339ff35411efa1617793339;',
        'TE': 'Trailers'
    }

    try :
        response = await client.get(url, headers=headers)

        soup = BeautifulSoup(response.text, features="html.parser")
        try:
            csrfKey = soup.find('input', {'name': 'csrfKey'}).get('value')
        except:
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                "rateLimit": True,
                "exists": False,
                "emailrecovery": None,
                "phoneNumber": None,
                "others": None
            })

        params = {
            'app': 'core',
            'module': 'system',
            'controller': 'ajax',
            'do': 'emailExists',
            'csrfKey': csrfKey,
            'input': email
        }

        response = await client.get("https://omerta.la/", headers=headers, params=params)

        if "fail" in response.text :
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                "rateLimit": False,
                "exists": True,
                "emailrecovery": None,
                "phoneNumber": None,
                "others": None
            })
        else :
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                "rateLimit": False,
                "exists": False,
                "emailrecovery": None,
                "phoneNumber": None,
                "others": None
            })
    except :
        out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
            "rateLimit": True,
            "exists": False,
            "emailrecovery": None,
            "phoneNumber": None,
            "others": None
        })

    return None
