from simple_term_menu import TerminalMenu


def main():
    options = ["entry1", "entry2", "entry3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
