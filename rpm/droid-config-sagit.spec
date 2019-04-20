# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device sagit
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Mi 6 (sagit)
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 2.0
# We assume most devices will
%define have_modem 1

Provides: ofono-configs

# Use kernel modules
%define have_kernel_modules 1

# Community HW adaptations need this
%define community_adaptation 1

%include droid-configs-device/droid-configs.inc
