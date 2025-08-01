[app]
title = QuoteApp
package.name = quoteapp
package.domain = org.quoteapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.ndk_api = 21
android.build_tools = 34.0.0
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer
android.accept_sdk_license = True
