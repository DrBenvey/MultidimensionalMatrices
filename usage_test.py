import operations_test
import help_test

_help_test = help_test.Test(2, 4)
_help_test.TestMM()
_help_test.SectionsMM()

_operations_test=operations_test.Test()
_operations_test.Testλμ_convolution_product_sequential()
_operations_test.Testλμ_convolution_product_parallel()
_operations_speed_test=operations_test.SpeedTest()
_operations_speed_test.Testλμ_convolution_product_sequential()
_operations_speed_test.Testλμ_convolution_product_parallel()
_operations_speed_test.Testλμ_convolution_product_sequential_vs_parallel()

