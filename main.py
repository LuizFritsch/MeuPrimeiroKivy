from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Incrementador(BoxLayout):
	pass
class Test(App):
	def build(self):
		return Incrementador()

	def incrementar(self,button):
		self.label.text = str(int(self.label.text)+1)
t = Test()
t.run()