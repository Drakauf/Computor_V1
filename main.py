import verbose as verb
import reader as r
import globale as g
import simply as s
import solver
import sys
import tools

if __name__ == "__main__":
    equation = r.reader(sys.argv)
    formatted = tools.simplify(equation)
    simply_form = s.simply(formatted)
    degree = verb.ft_simplyprint(simply_form)
    solver.solver(simply_form, degree)
