from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView

class PersonalizedApp(App):
    def build(self):
        # 创建主布局
        layout = BoxLayout(orientation='vertical')

        # 创建标签
        label = Label(text='Personalize the app', font_size=40)
        layout.add_widget(label)

        # 创建按钮
        button = Button(text='Change the background', size_hint=(None, None), size=(500, 50))
        button.bind(on_press=self.show_file_chooser)
        layout.add_widget(button)

        # 创建图像
        self.image = Image(source='default_background.jpg')
        layout.add_widget(self.image)

        return layout

    def show_file_chooser(self, instance):
        # 创建文件选择器
        file_chooser = FileChooserIconView()
        file_chooser.bind(on_submit=self.change_background)

        # 创建弹出窗口
        popup = Popup(title='Select a background image', content=file_chooser, size_hint=(0.9, 0.9))
        popup.open()

    def change_background(self, instance, value):
        # 更改背景图像
        PersonalizedApp.change_background()
        self.image.source = value[0]

if __name__ == '__main__':
    PersonalizedApp().run()