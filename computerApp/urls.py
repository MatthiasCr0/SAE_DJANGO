from django.urls import path


from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('machines/',views.machine_list_view,name='machines'),
    path('machines/<pk>',views.machine_detail_view, name='machine-detail'),
    path('utilisateurs/',views.utilisateur_list_view,name='utilisateurs'),
    path('utilisateurs/<pf>',views.utilisateur_detail_view, name='utilisateur-detail'),
    path('add-utilisateur/',views.utilisateur_add_form, name='add-utilisateur'),
    path('add-machines/',views.machine_add_form, name='add-machine'),
    path('del-machines/',views.machine_del_form, name='del-machine'),
    path('del-utilisateurs/',views.utilisateur_del_form, name='del-utilisateur'),
    path('visualisation/',views.visualisation_view,name='visualisation'),
    path('contact/submit/', views.contact_submit, name='contact-submit'),
    path('contact/success/', views.contact_success, name='contact-success'),
    path('contact/messages/', views.contact_messages, name='view-contact-messages'),
    path('contact/del-messages/', views.del_contact_message, name='del-contact-message'),


    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]