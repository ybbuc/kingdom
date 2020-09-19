# Challenge Week
## turtle_art.py
Add the following code:
```python
from turtle import *

hideturtle()

for x in range(360):
    forward(x)
    left(59)
```
Run your code to see the output.

Notice that the `hideturtle()` command prevents the turtle arrow from being drawn on the screen.

Try the following:
- Try setting the color of the outline and/or the fill to make the picture look beautiful. You may need to refer back to your lecture notes and tutorials to see how to do this. You could even use if, elif, else statements inside the for loop, so the colors change.
- Try changing the angle from 59 to something else and run the code to see what happens. Try experimenting with other changes. Can you make an interesting pattern?

![Turtle art sample](turtle_art_sample.jpg)
