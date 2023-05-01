import abc
import random

import tornado.web

from names import surnames


class MainPageHandler(tornado.web.RequestHandler, abc.ABC):
    def get(self):
        card = self.get_argument('card')
        re_format_card = '\t'.join([card[i * 4: i * 4 + 4] for i in range(len(card) // 4)])
        balance = self.get_argument('balance')
        print(card.split())

        rub = random.randint(401, 499)
        liters = random.randint(101, 199)

        surname = random.choice(surnames)

        context = {
            'card': re_format_card, 'balance': balance, 'rub': rub, 'liters': liters, 'surname': surname
        }

        return self.render('templates/page.html', context=context)
