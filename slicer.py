from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics import Color, Ellipse, Line, Rectangle

Builder.load_string("""
<PaintWidget>:
    BoxLayout:
        size_hint_y: None
        height: "48dp"
        spacing: "2dp"
        padding: "2dp"

        ToggleButton:
            text: "Clear Last"
            id: debug
            on_release: root.clear()

    BoxLayout:
        size_hint_y: None
        height: "48dp"
        top: root.top
        spacing: "2dp"
        padding: "2dp"
        Label:
            id: status
            text: "Status"
""")

class PaintWidget(Widget):
	
	rects = []

	def on_touch_down(self, touch):
		with self.canvas:
			Color(1, 0, 0, 0.2)
			d = 10
			Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
			touch.ud['rect'] = Rectangle(pos=(touch.x, touch.y), size=(0,0))

	def on_touch_move(self, touch):
		dist_x = (touch.x - touch.ud['rect'].pos[0])
		dist_y = (touch.y - touch.ud['rect'].pos[1])
		touch.ud['rect'].size = (dist_x, dist_y)

	def on_touch_up(self, touch):
		# Get top-left and bottom-right rect coords
		# Convert to array indices for image slice.
		tl = touch.ud['rect'].pos
		br = tuple([sum(x) for x in zip(tl, touch.ud['rect'].size)])
		self.rects.append(Shape(tl, br))
		print(self.rects)

	def clear(self):
		self.rects.pop()

class PaintApp(App):
	def build(self):
		return PaintWidget()


class Shape():
		def __init__(self,xy1,xy2):
			self.x1 = xy1[0]
			self.y1 = xy1[1]
			self.x2 = xy2[0]
			self.y2 = xy2[1]


if __name__ == "__main__":
	PaintApp().run()