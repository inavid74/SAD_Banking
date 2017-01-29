from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/', view=views.login_user, name='Login'),
    url(r'^superUser/signupAdmin/', view=views.signup_admin, name='SignUpAdmin'),
    url(r'^admin/createBranch/', view=views.create_branch, name='CreateBranch'),
    url(r'^admin/createBranchAdmin/', view=views.create_branch_admin, name='CreateBranchAdmin'),
    url(r'^cashier/signupCustomer/', view=views.signup_customer, name='SignUpCustomer'),
    url(r'^cashier/createBankAccount/', view=views.create_bank_account, name='CreateBankAccount'),
    url(r'^profile/cashier/(.+)/', view=views.profile_cashier, name='ProfileCashier'),
    url(r'^profile/admin/(.+)/', view=views.profile_admin, name='ProfileAdmin'),
    url(r'^profile/customer/(.+)/', view=views.profile_customer, name='ProfileCustomer'),
    url(r'^profile/branchAdmin/(.+)/', view=views.profile_branch_admin, name='ProfileBranchAdmin'),
    url(r'^branchAdmin/signupStaff/', view=views.signup_staff, name='SignupStaff'),
    url(r'^test/(.+)/', view=views.test, name='TestView'),
    url(r'^logout/', view=views.logout_view, name='Logout'),

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