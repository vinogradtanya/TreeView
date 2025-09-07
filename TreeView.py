from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode


class MyApp(App):
    def build(self):
        fl = FloatLayout()

        main_layout = TreeView(root_options = dict(text = 'Каталог авто'), indent_level = 50)

        level1 = main_layout.add_node(TreeViewLabel(text = 'BMW'))
        line1 = main_layout.add_node(TreeViewLabel(text = 'e46'), level1)
        main_layout.add_node(TreeViewLabel(text = 'Объём: 2.5л'), level1)
        main_layout.add_node(TreeViewLabel(text='Мощность: 192 л.с.'), level1)
        main_layout.add_node(TreeViewLabel(text='0-100: 7.2с'), level1)

        level2 = main_layout.add_node(TreeViewLabel(text='Mercedes-Benz'))
        line2 = main_layout.add_node(TreeViewLabel(text='W203'), level2)
        main_layout.add_node(TreeViewLabel(text='Объём: 2.5л'), level2)
        main_layout.add_node(TreeViewLabel(text='Мощность: 204 л.с.'), level2)
        main_layout.add_node(TreeViewLabel(text='0-100: 8.3с'), level2)

        TreeViewLabel(color_selected = [1, 0, 0, 1])

        label = Label(text = 'Информация отсутствует')
        fl.add_widget(label)

        button = Button(text = 'Показать выбранный элемент', size_hint = (1, 0.1))
        fl.add_widget(button)

        def info(instance):
            try:
                label.text = main_layout.selected_node.text
            except:
                pass
        button.bind(on_press = info)

        fl.add_widget(main_layout)

        return fl

if __name__ == '__main__':
    MyApp().run()