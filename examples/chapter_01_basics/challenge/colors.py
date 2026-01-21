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


# %% Test
colors = Colors()

val = colors.green
print(f'green: {val:06X}')  # Expected: green: 00FF00
# %%
