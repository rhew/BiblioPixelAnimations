from bibliopixel.animation import BaseStripAnim
class ColorPattern(BaseStripAnim):
    """Fill the dots progressively along the strip with alternating colors."""

    def __init__(self, led, colors, width, dir = True, start=0, end=-1):
        super(ColorPattern, self).__init__(led, start, end)
        self._colors = colors
        self._colorCount = len(colors)
        self._width = width
        self._total_width = self._width * self._colorCount;
        self._dir = dir

    def step(self, amt = 1):
        for i in range(self._size):
            cIndex = ((i+self._step) % self._total_width) / self._width;
            self._led.set(self._start + i, self._colors[cIndex])
        if self._dir:
            self._step += amt
            overflow = (self._start + self._step) - self._end
            if overflow >= 0:
                self._step = overflow
        else:
            self._step -= amt
            if self._step < 0:
                self._step = self._end + self._step