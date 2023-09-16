from simple_term_menu import TerminalMenu
from db.models import Person
from db.seed import session


class Cli:
    def main(self):
        options = ["Person", "Chores"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Person":
            self.give_all_people()
        if options[menu_entry_index] == "Chores":
            print("These are your chores")

    def give_all_people(self):
        people = Person.list_people(session)
        if people:
            print("List of people:")
            for person in people:
                print(person.name)
        else:
            print("No people found.")


app = Cli()
app.main()
