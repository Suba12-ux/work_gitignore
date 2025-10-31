from datetime import datetime, date, timedelta
from decimal import Decimal
import traceback

def add(items, title, amount, expiration_date=None):
    if expiration_date != None:
        # Преобразуем строку в datetime.date
        #if isinstance(expiration_date, str):
        expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
        
    items_dict = {
        'amount': amount,
        'expiration_date': expiration_date,
        }

    if title not in items:
        items[title] = [items_dict]
    else:
        items[title].append(items_dict)

def add_by_note(items, note):
    data = note.split()
    try:
        amount = Decimal(data[-2])
    except:
        amount = Decimal(data[-1])

    title = ' '.join(data[:data.index(str(amount))])
    try:
        expiration_date =  data[-1] if datetime.strptime(data[-1], '%Y-%m-%d') else None
    except:
        expiration_date = None
        
    add(items, title, amount, expiration_date)

def find(items, needle):
    return [key for key in items if needle.lower() in key.lower()]

def get_amount(items, needle):
    result = Decimal(0)
    for title in items:
        if  needle.lower() in title.lower():
            for item in items[title]:
                result += item['amount']
    return Decimal(result)

def get_expired(items, in_advance_days=0):
    today = date.today()
    deadline = today + timedelta(days=in_advance_days)
    result = []
        
    for title, parts in items.items():
        amount = Decimal(0)
        for part in parts:
            exp_date = part['expiration_date']
            if exp_date is not None and exp_date <= deadline:
                    amount += part['amount']
            
        if amount > 0:
            result.append((title, amount))
        
    return result


if __name__ == '__main__':
    try:
        goods = {'Яйца Фабрики №1': [{'amount': Decimal('1'),'expiration_date': date(2025, 10, 29)}],'Фабрика №2: яйца': [{'amount': Decimal('2'), 'expiration_date': None},{'amount': Decimal('3'),'expiration_date': date(2025, 10, 27)}],'макароны': [{'amount': Decimal('100'), 'expiration_date': None}]}
        new_doct = {}

        add(new_doct, 'Яйца Фабрики №1', Decimal('4'), '2023-07-15')
        add_by_note(new_doct, 'Макароны 1.5')
        x1 = get_amount(goods, 'Фабрик')
        print(x1)
        for key in new_doct:
            print(key, new_doct[key])



    except Exception as error:
        print('Ошибка', error)
        print(traceback.format_exc())