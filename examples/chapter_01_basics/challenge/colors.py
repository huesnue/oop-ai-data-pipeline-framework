# %% Color database
colors_db = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
}

class Colors:
    """Dynamically get color from colors_db as attributes."""
    def __init__(self, colors=colors_db):
        self._colors = colors
        pass
    
    # FIXEME: Implement the __getattr__ method
    def __getattr__(self, name):
        if name in self._colors:
            hex_color = self._colors[name]
            return int(hex_color.lstrip('#'), 16)
        raise AttributeError(f"'Colors' object has no attribute '{name}'")

class ColorsB:
    """Dynamically get color from colors_db as attributes."""
    def __init__(self):
        pass
    # FIXEME: Implement the __getattr__ method
    def __getattr__(self, name):
        mycolor = colors_db.get(name)
        
        if mycolor is None:
            raise AttributeError(f"'Colors' object has no attribute '{name}'")
        
        return mycolor
# %% Test
colors = Colors()
colorsB = ColorsB()

val = colors.green
val2 = colorsB.green
print(f'green: {val:06X}')  # Expected: green: 00FF00
print(f'blue: {val:06X}')  # Expected: blue: 0000FF
# %%
