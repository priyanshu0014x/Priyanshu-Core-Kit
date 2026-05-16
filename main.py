import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class PriyanshuCoreKit(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        Window.clearcolor = (0.05, 0.05, 0.05, 1)

        title_label = Label(
            text="[b][color=ff3333]PRIYANSHU CORE-KIT[/color][/b]\n[size=14]Ultimate System & Network Toolkit[/size]",
            markup=True,
            size_hint_y=None,
            height=80,
            halign='center'
        )
        main_layout.add_widget(title_label)

        scroll_view = ScrollView()
        button_layout = BoxLayout(orientation='vertical', spacing=12, size_hint_y=None)
        button_layout.bind(minimum_height=button_layout.setter('height'))

        tools = [
            ("🧠 System Kernel Auditor", "🧠 OS और CPU आर्किटेक्चर की असली जानकारी देखें"),
            ("📡 Wi-Fi Subnet Scanner", "📡 लोकल नेटवर्क पर एक्टिव डिवाइसेज का पता लगाएं"),
            ("🔍 Port & Service Analyzer", "🔍 टारगेट वेबसाइट्स के ओपन端口 स्कैन करें"),
            ("📍 IP Location Lookup", "📍 किसी भी IP एड्रेस की लाइव लोकेशन ट्रैक करें"),
            ("🔒 Secure Diary Vault", "🔒 अपने महत्वपूर्ण नोट्स को सुरक्षित रखें"),
            ("🎮 Cyber Snake Mini-Game", "🎮 खाली समय में खेलने के लिए एक मजेदार गेम")
        ]

        for tool_name, tool_desc in tools:
            btn = Button(
                text=f"[b]{tool_name}[/b]\n[size=12]{tool_desc}[/size]",
                markup=True,
                size_hint_y=None,
                height=70,
                background_color=(0.12, 0.12, 0.12, 1),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=self.on_tool_click)
            button_layout.add_widget(btn)

        scroll_view.add_widget(button_layout)
        main_layout.add_widget(scroll_view)

        footer_label = Label(
            text="[color=00ff66]DEVELOPED BY PRIYANSHU[/color]",
            markup=True,
            size_hint_y=None,
            height=30
        )
        main_layout.add_widget(footer_label)

        return main_layout

    def on_tool_click(self, instance):
        clean_text = instance.text.split('\n')[0].replace('[b]', '').replace('[/b]', '')
        print(f"[+] Launching Module: {clean_text}")

if __name__ == '__main__':
    PriyanshuCoreKit().run()
