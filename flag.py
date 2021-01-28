def draw_flag(R, *, indent=.5):
	top = '#' * (4 * R + 3) + '\n'
	border = ''.join('#' + ' ' * (4 * R + 1) + '#\n' for _  in range(R // 2))
	left_border = '#' + ' ' * R
	right_border = ' ' * R + '#\n'

	result = ''
	result += top + border
	
	for i in range(2 * R + 1):
		result += left_border
		for j in range(2 * R + 1):
			dist = pow((i - R) ** 2 + (j - R) ** 2, .5)
			if abs(dist - R) < indent: 
				result += '*'
			else: 
				result += ' '
		result += right_border

	result += border + top
	return result
	

if __name__ == '__main__':
	radius = 10
	print(draw_flag(radius))