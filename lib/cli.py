from simple_term_menu import TerminalMenu


def main(self):
    self.clear(44)
    options = ["Person", "Chores"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


# def select_person(self):


if __name__ == "__main__":
    main()
