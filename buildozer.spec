[app]
title = Priyanshu App
package.name = priyanshuapp
package.domain = org.priyanshu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android specific settings
android.api = 31
android.minapi = 24b
android.ndk_api = 21
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1

