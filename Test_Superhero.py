import Imports
from Superhero import func


@Imports.pytest.mark.parametrize("invalid_string", 
                        [
                             
                            "m", "f", "", "123", "$%^#&*"
                        ])
def test_func_with_various_invalid_strings(invalid_string):
  
    with Imports.pytest.raises(ValueError):
        func(True, invalid_string)
    
    
    with Imports.pytest.raises():
        func(False, invalid_string)


@Imports.pytest.mark.parametrize("bool_value", 
                        [
                             True, False
                        ])
@Imports.pytest.mark.parametrize("invalid_string", 
                        [
                             "да", "нет", "invalid"
                        ])
def test_func_with_all_combinations(bool_value, invalid_string):
    with Imports.pytest.raises(ValueError):
        func(bool_value, invalid_string)
        
