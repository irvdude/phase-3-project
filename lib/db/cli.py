from simple_term_menu import TerminalMenu
from models import Person, Chore
from seed import session


class Cli:
    def main(self):
        options = ["Person", "Chores"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == "Person":
            self.give_all_people()
        if options[menu_entry_index] == "Chores":
            self.give_all_chores()

    def give_all_people(self):
        people = Person.list_people(session)
        if people:
            print("List of people:")
            for person in people:
                print(person.name)
        else:
            print("No people found.")

    def give_all_chores(self):
        chores = Chore.list_chores(session)
        if chores:
            print("List of chores")
            for chore in chores:
                print(chore.chore_name)


app = Cli()
app.main()
