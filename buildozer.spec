¹[app]
title = Priyanshu App
package.name = priyanshuapp
package.domain = org.priyanshu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android specific settings (लाइसेंस एरर फिक्स करने के लिए स्टेबल वर्जन)
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1

