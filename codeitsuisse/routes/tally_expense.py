import logging

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/tally-expense', methods=['POST'])
def tally_expense():
    data = request.get_json()
    logging.info(data)
    persons = data.get("persons")
    num_of_persons = len(persons)
    expenses = data.get("expenses")
    person_paid = {}
    person_expense = {}
    need_to_pay = {}
    for p in persons:
        person_paid[p] = 0
        person_expense[p] = 0
        need_to_pay[p] = 0  # negative number means need_to_receive
    for e in expenses:
        paid_by = e.get("paidBy")
        amount = e.get("amount")
        person_paid[paid_by] += amount
        if len(e) == 4:
            exclude = e.get("exclude")
            num_of_persons_exclude = len(exclude)
            for key in person_expense:
                if key not in exclude:
                    person_expense[key] += (amount / num_of_persons_exclude)
        else:
            for key in person_expense:
                person_expense[key] += (amount / num_of_persons)

    for p in persons:
        need_to_pay[p] = person_expense[p] - person_paid[p]

    transactions = []

    for key1 in need_to_pay:
        if need_to_pay[key1] == 0:
            continue
        if need_to_pay[key1] > 0:
            for key2 in need_to_pay:
                if need_to_pay[key2] < 0:
                    transaction = {}
                    transaction['from'] = key1
                    transaction['to'] = key2
                    if need_to_pay[key1] <= -(need_to_pay[key2]):
                        transaction['amount'] = need_to_pay[key1]
                        need_to_pay[key1] = 0
                        need_to_pay[key2] += transaction['amount']
                        transactions.append(transaction)
                        break
                    else:
                        transaction['amount'] = -(need_to_pay[key2])
                        need_to_pay[key2] = 0
                        need_to_pay[key1] -= transaction['amount']

                        transactions.append(transaction)


    for item in transactions:
        myamount = round(item['amount'],2)
        item['amount'] = myamount

    output = {"transactions": transactions}
    logging.info(output)

    return jsonify(output)
