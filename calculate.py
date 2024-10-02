import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
        '''Вычисляет значение заданной функции для заданной фигуры

                Параметры:
                fig (str): Название фигуры ('circle' или 'square')
                func (str): Название функции (perimeter' или 'area')
                size (list): Размеры сторон фигур (1 сторона для квадрата или радиус для круга)

        Возвращаемое значение:
                result (str): '('area' или 'perimetr') of ('circle' или 'square') is (результаты вычислений)'
        
'''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



