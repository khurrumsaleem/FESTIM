from FESTIM import DirichletBC, BoundaryConditionExpression
import fenics as f
import sympy as sp


class CustomDirichlet(DirichletBC):
    """Subclass of DirichletBC allowing the use of a user-defined function.
    Usage:
    def fun(T, solute, param1):
        return 2*T + solute - param1
    my_bc = CustomDirichlet(
        surfaces=[1, 2],
        function=fun,
        param1=2*FESTIM.x + FESTIM.t
    )
    """
    def __init__(self, surfaces, function, component=0, **prms) -> None:
        """Inits CustomDirichlet

        Args:
            surfaces (list or int): the surfaces of the BC
            function (callable): the custom function
            component (int, optional): the field the boundary condition is
                applied to. Defaults to 0.
        """
        super().__init__(surfaces, component=component)
        self.function = function
        self.prms = prms
        self.convert_prms()

    def create_expression(self, T):
        value_BC = BoundaryConditionExpression(
            T, self.function,
            **self.prms,
        )
        self.expression = value_BC
        self.sub_expressions = self.prms.values()

    def convert_prms(self):
        """Creates Expressions or Constant for all parameters
        """
        for key, value in self.prms.items():
            if isinstance(value, (int, float)):
                self.prms[key] = f.Constant(value)
            else:
                self.prms[key] = f.Expression(
                    sp.printing.ccode(value),
                    t=0, degree=1)
