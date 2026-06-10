DISPLAY_STYLE = """
    QLineEdit {
        font-size: 28px;
        padding: 12px;
        border_radius: 8px;
        background-color: #ffffff;
        color: 000000;
    }
"""

def get_button_style(button_text: str) -> str:
    if button_text in ["+", "-", "*", "/", "=","xʸ"]:
        backgrond_color = "#2d89ef"
        text_color = "white"

    elif button_text in ["C", "CE"]:
        backgrond_color = "#d95534f"
        text_color = "white"

    elif button_text in [
        "sin",
        "cos",
        "tan",
        "log",
        "ln",
        "√",
        "x²",
        "π",
        "e",
        "%",
        "!",
    ]:
        backgrond_color = "#444444"
        text_color = "white"
    
    else:
        backgrond_color = "#f0f0f0"
        text_color = "black"

    return f"""
        QPushButton {{
             font-size: 22px;
             backgrond-color: {backgrond_color};
             color: {text_color};
             border: 1px solid #aaaaaa;
             border-radius: 8px;
        }}
        QPushButton:hover {{
            backgrond-color: #666666;
            color: white;
        }}
    """
    