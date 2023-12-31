from kivy.app import App
from kivy.uix.button import Button


class MyApp(App)
    def build(self)
        # 创建一个按钮，并将其绑定到 on_button_press 方法
        button = Button(text='点击我', on_press=self.on_button_press)
        return button

    def on_button_press(self, instance)
        # 按钮点击事件处理
        print('按钮被点击了')


if __name__ == '__main__'
    MyApp().run()
