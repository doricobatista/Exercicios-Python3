'''
regras do FizzBuzz

1. Se a posição for multipla de 3: Fizz
2. Se a posição for multipla de 5: Buzz
3. Se a posição for multipla de 3 e 5: FizzBuzz
4. Para qualquer outra posição fale o proprio numero.
'''

from functools import partial

multiplo = lambda base, num: num % base == 0
multiplo_5 = partial(multiplo, 5)
multiplo_3 = partial(multiplo, 3)

'''
def assert_equal(result, expected):
    from sys import _getframe
    msg = 'Falha: Linha {} obteve {} mas deveria ser {}'
    if not result == expected:
        frame_atual = _getframe()
        frame_chamador = frame_atual.f_back
        num_linha = frame_chamador.f_lineno
        print(msg.format(num_linha, result, expected))
      '''  
        
def robot(numero):
    say = str(numero)
    
    if multiplo_3(numero) and multiplo_5(numero):
        say = 'FizzBuzz'
        
    elif multiplo_5(numero): 
        say = 'Buzz'
        
    elif multiplo_3(numero):
        say = 'Fizz'
    return say

     

'''
# Testes do robô
if __name__ == '__main__':
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(3), 'Fizz')
    assert_equal(robot(5), 'Buzz')
    assert_equal(robot(15), 'FizzBuzz')
    assert_equal(robot(27), 'Fizz')
    assert_equal(robot(30), 'FizzBuzz')
'''