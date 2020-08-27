from django.urls import path

from two_factor.views import (
    BackupTokensView, DisableView, LoginView, PhoneDeleteView, PhoneSetupView,
    ProfileView, QRGeneratorView, ResetSetupGeneratorOrYubikeyView, ResetSetupPhoneOrGeneratorView,
    ResetSetupPhoneOrYubikeyView, SetupCompleteView, SetupView,
)

core = [
    path(
        'account/login/',
        LoginView.as_view(),
        name='login',
    ),
    path(
        'account/two_factor/setup/',
        SetupView.as_view(),
        name='setup',
    ),
    path(
        'account/two_factor/qrcode/',
        QRGeneratorView.as_view(),
        name='qr',
    ),
    path(
        'account/two_factor/setup/complete/',
        SetupCompleteView.as_view(),
        name='setup_complete',
    ),
    path(
        'account/two_factor/setup/reset/1/',
        view=ResetSetupGeneratorOrYubikeyView.as_view(),
        name='setup_reset_generator_or_yubikey',
    ),
    path(
        'account/two_factor/setup/reset/2/',
        view=ResetSetupPhoneOrYubikeyView.as_view(),
        name='setup_reset_phone_or_yubikey',
    ),
    path(
        'account/two_factor/setup/reset/3/',
        view=ResetSetupPhoneOrGeneratorView.as_view(),
        name='setup_reset_phone_or_generator',
    ),
    path(
        'account/two_factor/backup/tokens/',
        BackupTokensView.as_view(),
        name='backup_tokens',
    ),
    path(
        'account/two_factor/backup/phone/register/',
        PhoneSetupView.as_view(),
        name='phone_create',
    ),
    path(
        'account/two_factor/backup/phone/unregister/<int:pk>/',
        PhoneDeleteView.as_view(),
        name='phone_delete',
    ),
]

profile = [
    path(
        'account/two_factor/',
        ProfileView.as_view(),
        name='profile',
    ),
    path(
        'account/two_factor/disable/',
        DisableView.as_view(),
        name='disable',
    ),
]
urlpatterns = (core + profile, 'two_factor')
