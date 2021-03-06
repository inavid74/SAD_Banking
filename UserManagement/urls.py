from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/', view=views.login_user, name='Login'),
    url(r'^superUser/signupAdmin/', view=views.signup_admin, name='SignUpAdmin'),
    url(r'^admin/createBranch/', view=views.create_branch, name='CreateBranch'),
    url(r'^admin/billDefinition/', view=views.bill_definition, name='BillDefinition'),
    url(r'^admin/FeeDefinition/', view=views.fee, name='FeeDefinition'),
    url(r'^admin/createBranchAdmin/', view=views.create_branch_admin, name='CreateBranchAdmin'),
    url(r'^cashier/signupCustomer/', view=views.signup_customer, name='SignUpCustomer'),
    url(r'^cashier/createBankAccount/', view=views.create_bank_account, name='CreateBankAccount'),
    url(r'^cashier/createCreditCard/', view=views.create_creditcard, name='CreateCreditCard'),
    url(r'^profile/cashier/(?P<username>.+)/', view=views.profile_cashier, name='ProfileCashier'),
    url(r'^profile/admin/(?P<username>.+)/', view=views.profile_admin, name='ProfileAdmin'),
    url(r'^profile/customer/(?P<username>.+)/', view=views.profile_customer, name='ProfileCustomer'),
    url(r'^profile/branchAdmin/(?P<username>.+)/', view=views.profile_branch_admin, name='ProfileBranchAdmin'),
    url(r'^branchAdmin/signupStaff/', view=views.signup_staff, name='SignupStaff'),
    url(r'^test/(.+)/', view=views.test, name='TestView'),
    url(r'^logout/', view=views.logout_view, name='Logout'),
    url(r'^cashier/CheckRequest/', view=views.check_request, name='CheckRequest'),
    url(r'^legalExpert/CheckConfirmation/', view=views.legalExpert_check_confirm, name='LegalExpertCheckConfirm'),
    url(r'^accountant/CheckConfirmation/', view=views.accountant_check_confirm, name='AccountantCheckConfirm'),
    url(r'^legalExpert/ActivateAccount/', view=views.activate_account, name='ActivateAccount'),
    url(r'^cashier/LoanRequest/', view=views.loan_request, name='LoanRequest'),
    url(r'^legalExpert/LoanConfirmation/', view=views.legalExpert_loan_confirm, name='LegalExpertLoanConfirm'),
    url(r'^accountant/LoanConfirmation/', view=views.accountant_loan_confirm, name='AccountantLoanConfirm'),
    url(r'^cashier/RegularTransaction/', view=views.regular_transaction, name='RegularTransaction'),
    url(r'^profile/legalExpert/(?P<username>.+)/', view=views.profile_legal_expert, name='ProfileLegalExpert'),
    url(r'^profile/accountant/(?P<username>.+)/', view=views.profile_accountant, name='ProfileAccountant'),


    url(r'^ghabz/', view=views.ghabz, name='Ghabz'),
    url(r'^vam/', view=views.vam, name='Vam'),
    url(r'^check/', view=views.check, name='Check'),
    url(r'^gozaresh/', view=views.gozaresh, name='Gozaresh'),
    url(r'^havale/', view=views.havale_monazam, name='Havale'),
    url(r'^gardesh/', view=views.gardesh_hesab, name='Gardesh'),
    url(r'^eskenas/', view=views.tarif_eskenas, name='ATMEskenas'),
    url(r'^masdod/', view=views.masdodsazi, name='Masodosazi'),
    url(r'^faal/', view=views.faalsazi, name='FaalSazi'),
    url(r'^hesabbehesab/', view=views.hesabbehesab, name='HesabBeHesab'),

]