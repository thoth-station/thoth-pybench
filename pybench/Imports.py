from .pybench import Test

# First imports:
import os
import pybench.package.submodule

class SecondImport(Test):

    version = 2.0
    operations = 5 * 5
    rounds = 40000

    def test(self):

        for i in range(self.rounds):
            import os
            import os
            import os
            import os
            import os

            import os
            import os
            import os
            import os
            import os

            import os
            import os
            import os
            import os
            import os

            import os
            import os
            import os
            import os
            import os

            import os
            import os
            import os
            import os
            import os

    def calibrate(self):

        for i in range(self.rounds):
            pass


class SecondPackageImport(Test):

    version = 2.0
    operations = 5 * 5
    rounds = 40000

    def test(self):

        for i in range(self.rounds):
            import pybench.package
            import pybench.package
            import pybench.package
            import pybench.package
            import pybench.package

            import pybench.package
            import pybench.package
            import pybench.package
            import pybench.package
            import pybench.package

            import pybench.package
            import pybench.package
            import pybench.package
            import pybench.package
            import pybench.package

            import pybench.package
            import pybench.package
            import pybench.package
            import pybench.package
            import pybench.package

            import pybench.package
            import pybench.package
            import pybench.package
            import pybench.package
            import pybench.package

    def calibrate(self):

        for i in range(self.rounds):
            pass

class SecondSubmoduleImport(Test):

    version = 2.0
    operations = 5 * 5
    rounds = 40000

    def test(self):

        for i in range(self.rounds):
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule

            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule

            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule

            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule

            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule
            import pybench.package.submodule

    def calibrate(self):

        for i in range(self.rounds):
            pass
