class Customer(object):

    def __init__(self, firstname, lastname):
        self.bankaccount = Bankaccount("transfer account")
        self.firstname = firstname
        self.lastname = lastname

    def find_bankaccount_id(self, given_id):
        for customerobject in self.customerlist:
            for my_id in customerobject:
                if given_id is customerobject.id:
                    return self.Bankaccount

    def fill_customer_database(self, customerobject):
        customerlist = []
        customerlist.append(customerobject)

class Bankaccount(object):

    def __init__(self, my_type):
        self.type = my_type
        self.id = Bankaccount.set_my_id(self)
        self.balance = 0

    def set_my_id(self):

        my_id = 1
        return my_id
        my_id += 1


class Bank(object):

    def deposit(self, bankaccount, amount):
        myaccount = bankaccount
        myaccount.balance += amount

    def withdraw(self, bankaccount, amount):
        myaccount = bankaccount
        temp_balance = myaccount.balance - amount
        if temp_balance < 0:
            return False
        else:
            myaccount.balance -= amount
            return True

    def transaction(self, bankaccount1, bankaccount2, amount):
        if self.withdraw(bankaccount1, amount):
            self.deposit(bankaccount2, amount)
            return True
        else:
            print("Not enough money on account %d" % bankaccount2.id)

    def bank_account_info(self, firstname, lastname):
        print("Account Information for %s, %s:" % Customer.firstname, Customer.lastname)
        for customer in Customer.customerlist:
            if customer.firstname is firstname and customer.lastname is lastname:
                print("Account type: %s" % Bankaccount.type)
                print("Your Balance for account with the ID '%d' is: %f" % customer.bankaccount.id, customer.bankaccount.balance)




philip = Customer('philip', 'krueger')
Bank.bank_account_info(Bank, "philip", "krueger")