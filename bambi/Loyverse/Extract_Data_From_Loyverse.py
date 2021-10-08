


# --------------------------------------  Historial  --------------------------------------
"""
Versión 1:  Este programa no funciona porque tiene protección ReCaptcha y sólo es posible
            resolverlo a través de Selenium


import requests
from lxml import html

headers = {'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.132 Safari/537.36'}

login_form_url = 'https://loyverse.com/en/login'

session = requests.Session()

login_form_res = session.get(login_form_url, headers=headers)

parser = html.fromstring(login_form_res.text)
captcha_token = parser.xpath('//input[@id="recaptcha-token"]/@value/text()')

print(captcha_token)


login_url = 'https://r.loyverse.com/data/cabinetlogin'
login_data = {
    'email': 'pizzeriabambi@hotmail.com',
    'password': open('password.txt').readline().strip(),
    'recaptchaResponse': '03AGdBq24kRv5KJ5eQqailVk_6t3GkwvLaJeFPOuC_2e20ytLMJ'
                         'xkvvidbth3jSZg1Fq493Oj9woFacK-iIV-cInQfu33gDJBaWzYN'
                         'e5grI2PM22T_9lEgtXQuDSfhWpU2zwoB5bqubUNpAcDuWp3Qf5w'
                         'onDsZeCLl4asDrxlKSam6QV2bmiKSEgJDnNNArxVjMbK49LuEeA'
                         'cpsbu8c5g4aS4OcyBJDdZrHsjvvqJcpIaw6hxLh6Yk8jvE6kIYK'
                         '5Y1KtsGx76R7vrVf0gBC2uXpmQTGn5gYLZF5wkRA6wU1S4hXtvv'
                         'IjwBKMr23hOFaZ-56t8pZIoPRb6J9KGeSggM7u3rKcUGtNrC8Sp'
                         'D7gfyrWiecEN8U5aYOYG4Yv1DxBDQ4I3MR3ovSAqZy1Hj5WljvS'
                         'GBVME2fbDb9TQ_NquAaoaW54KvwhNj5RZiEKTm6BLWinhjZOa81'
                         'TtWVhK1nuETMlau0xMUflkDK3zmVQPySJoQMrfDr97URhO4uPIQ'
                         'l160NZEyscHo3jTnWpmPH6rnuM_z0iEW7c9OoeaV66h7w7riyNB'
                         'A1XkHz32-PNXGY9SY0-zu8Kaa21jqMqFRJ6kvjlxgBmgAgfKA_W'
                         'ry0yy0JJuWem48LytsKFPpQCHKG8AlKiao5W2Y7X_TS_rqwatT5'
                         'UzUnjHIOvaGIVH-rkfwbZjKatwc9QebrWm9Vv1_unghlbBn6-k-'
                         'ACQ6Yyq9pVWzRWe_640al4x-1_94wwpR9dGg0Xh91f5t0n9jVtI'
                         'WACEd_9WebXomJbu5qR6JZmGXUEu8afgkQyBheHX_KncXi6kAea'
                         'XnIZJ91up0aFBIMhfzq8Tf9sM7LK9LWAtm4VSaUOnRDEVN40YYQ'
                         '1UXnRpPG-F0WXBDcpn3C5V4S10ZyFmd5KnGkt0xAtNxYXklPgcp'
                         'EjXs6c46ytH8SnvbWsolesBlOPxhHwfisc59oLTsafuLqy3DiVE'
                         '4gsYhg6f40eDyyM2QDrdNchzpD6ylJ9dAyE2Tb7z28QPSQ32jaT'
                         'QSWPOnf2z-WkXgu0y__9rVyj2ngkZ6ifQEAbd_1eB7Hv07ltKiH'
                         'jczvj2oITYZRRqI1Ab-WMqbZDlYqw-zco5cD-S6lKPSICp969VL'
                         'DHMbcwCtCycrXo5rKyYmPt0v-Y4ieJqdj067Cyx1MZDftJ2-2_v'
                         'urBFtgrVKA1T30vF2nvlIelbEgfnvmTJVlQA'
}

session.post(
    login_url,
    data=login_data,
    headers=headers
)

data_url = 'https://r.loyverse.com/dashboard/#/report/' \
           'average?page=0&limit=10&periodName=lastThirty&periodLength=30d&' \
           'from=2021-09-10%2000:00:00&to=2021-09-16%2023:59:59&fromHour=0&toHour=0&type=all&' \
           'outletsIds=all&merchantsIds=all'

respuesta = session.get(
    data_url,
    headers=headers
)

parser = html.fromstring(respuesta.text)
clientes = parser.xpath('//div[@ng-if="receipt.clientName"]/text()')
for cliente in clientes:
    print(cliente)
"""