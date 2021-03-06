from django.db import models

from UserManagement.models import Customer, Admin, AdminBranch, Accountant, AdminATM, Cashier, LegalExpert, Branch


class BankAccount(models.Model):
    account_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    amount = models.BigIntegerField()
    branch = models.ForeignKey(Branch, on_delete=None, null=True)
    profit_until_now = models.BigIntegerField(default=0)


class Bank(models.Model):
    name = models.CharField(default="FaBank", max_length=255, primary_key=True, db_index=True)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    profit = models.IntegerField(default=18)
    card_fee = models.FloatField(default=1000)
    check_fee = models.IntegerField(default=100)
    alert_fee = models.IntegerField(default=10)
    card_transfer_fee = models.IntegerField(default=100)
    bankaccount_transfer_fee = models.IntegerField(default=100)

class Fees(models.Model):
    fees_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    fee = models.IntegerField(default=500)


class Loan(models.Model):
    loan_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    amount = models.BigIntegerField()
    installments = models.IntegerField(default=1)
    bank_account = models.ForeignKey(BankAccount, default=None)
    customer = models.ForeignKey(Customer, on_delete=None)
    legalExpert_confirmation = models.BooleanField(default=False)
    accountant_confirmation = models.BooleanField(default=False)
    cashier = models.ForeignKey(Cashier, related_name='Cashier_Loan', null=True, blank=True, default=None)
    reject = models.BooleanField(default=False)
    # bankaccount_to = models.ForeignKey(BankAccount, related_name='LoanDestination', null=True, blank=True, default=None )
    # customer_to = models.ForeignKey(Customer, related_name='Customer_Loan', null=True, blank=True, default=None )


class LoanPayment(models.Model):
    loanpayment_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    # customer = models.ForeignKey(Customer, on_delete=None)
    date = models.DateField(db_index=True)
    paid = models.BooleanField(default=False)
    profit = models.BigIntegerField(default=0)


class Money(models.Model):
    money_id = models.IntegerField(primary_key=True, unique=True, db_index=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField()


class Bills(models.Model):
    # bill_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    kind = models.CharField(primary_key=True, max_length=255, unique=True)
    BankAccount_to = models.ForeignKey(BankAccount, on_delete=models.CASCADE)


# class BillPayment(models.Model):
#     # bill_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
#     billpayment_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
#     billkind = models.ForeignKey(Bills, on_delete=None)
#     # customer = models.ForeignKey(Customer, on_delete=None)
#     # bankaccount_from = models.ForeignKey(BankAccount, on_delete=None, null=True)


class Transaction(models.Model):
    transaction_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    bankaccount_from = models.ForeignKey(BankAccount, on_delete=None, related_name='BankAcoount From+', null=True, blank=True)
    branch_from = models.ForeignKey(Branch, on_delete=None, related_name="Branch From+", null=True, blank=True)
    bankaccount_to = models.ForeignKey(BankAccount, on_delete=None, related_name='BankAccount To+', null=True, blank=True)
    branch_to = models.ForeignKey(Branch, on_delete=None, related_name='Branch To+', null=True, blank=True)
    date_time = models.DateField(auto_now_add=True)
    amount = models.BigIntegerField()
    type = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    cashier = models.ForeignKey(Cashier, on_delete=None, null=True, blank=True)


class ATM(models.Model):
    atm_id = models.IntegerField(primary_key=True, unique=True, db_index=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    manager = models.ForeignKey(AdminATM, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    min_amount = models.BigIntegerField(default=0)


class ATMMoneys(models.Model):
    atm_moneys_id = models.IntegerField(primary_key=True, unique=True, db_index=True)
    atm = models.ForeignKey(ATM, on_delete=models.CASCADE)
    money = models.ForeignKey(Money, on_delete=models.CASCADE)


class Check(models.Model):
    check_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    bankaccount = models.ForeignKey(BankAccount, on_delete=models.CASCADE)


class CheckLeaf(models.Model):
    checkleaf_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    bankaccount_from = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name= 'BankAccount')
    parent_check = models.ForeignKey(Check, on_delete=models.CASCADE, related_name= 'Check')
    amount = models.BigIntegerField(default=0,blank=True,null=True)
    expiration_date = models.DateField(auto_now_add=True,blank=True,null=True)
    used = models.BooleanField(default=False)
    legalExpert_confirmation = models.BooleanField(default=False)
    accountant_confirmation = models.BooleanField(default=False)
    bankaccount_to = models.ForeignKey(BankAccount, related_name='Destination', null=True, blank=True, default=None )
    customer_to = models.ForeignKey(Customer, related_name='Customer_CheckLeaf', null=True, blank=True, default=None )
    cashier = models.ForeignKey(Cashier, related_name='Cashier_CheckLeaf', null=True, blank=True, default=None)


class CreditCard(models.Model):
    number = models.BigIntegerField(primary_key=True, unique=True, blank=False, null=False)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    password = models.IntegerField(null=False, blank=False)


class RegularTransfers(models.Model):
    regular_trasaction_id = models.IntegerField(primary_key=True, db_index=True)
    isDaily = models.BooleanField(default=False)
    isMonthly = models.BooleanField(default=False)
    isYearly = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    bankaccount_from = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='BankAccount_From')
    bankaccount_to = models.ForeignKey(BankAccount, related_name='BankAccount_To', on_delete=models.CASCADE)
    amount = models.BigIntegerField()
