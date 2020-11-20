class LogicalAutomaton:
    def __init__(self):
        self.bracket_counter = 0
        self.state = 'q_0'

    def reset(self):
        self.__init__() # lepiej by było w drugą stronę - niech __init__ wywoła reset

    def next_step_q_0(self, sign):
        if sign == '~':
            pass
        elif sign == '(':
            self.bracket_counter += 1
        elif ord(sign) <= 127 and sign.islower():
            self.state = 'q_1'
        else:
            self.state = 'q_n'

    def next_step_q_1(self, sign):
        if sign == '&' or sign == '|':
            self.state = 'q_0'
        elif sign == ')':
            self.bracket_counter -= 1
        else:
            self.state = 'q_n'

    def handle_expression(self, expression):
        expression = expression.replace(" ", "")
        for sign in expression: # raczej character niż sign
            if self.state == 'q_0':
                self.next_step_q_0(sign)
            elif self.bracket_counter < 0 or self.state == 'q_n':
                return False
            else:
                self.next_step_q_1(sign)
        if self.bracket_counter == 0 and self.state == 'q_1':
            return True
        else:
            return False


def check_expression(expresion):
    automaton = LogicalAutomaton()
    is_correct = automaton.handle_expression(expresion)
    automaton.reset()   # po co, skoro za chwilę tego obiektu nie będzie?
    return is_correct


example_1 = '(a &b) |c&~d'
print(check_expression(example_1))
example_2 = 'a&&&b|~(~~a|b)'
print(check_expression(example_2))
