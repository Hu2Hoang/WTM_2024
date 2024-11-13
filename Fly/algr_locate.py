from math import *
def calc_locate(x1,y1,z1,d1,x2,y2,z2,d2,x3,y3,z3,d3,epsilon):
	ex1=x2-x1
	ey1=y2-y1
	ez1=z2-z1

	h=sqrt(ex1*ex1+ey1*ey1+ez1*ez1)

	if(h<=epsilon):
		return 1,1,0
		# print("A and B are to close")

	ex1=ex1/h
	ey1=ey1/h
	ez1=ez1/h

	i=ex1*(x3 - x1) + ey1*(y3 - y1) + ez1*(z3 - z1)

	ex2=x3-x1-i*ex1
	ey2 = y3 - y1 - i*ey1
	ez2 = z3 - z1 - i*ez1

	t = sqrt(ex2*ex2 + ey2*ey2 + ez2*ez2)

	if(t<=epsilon):
		return 1,1,1
		# print("A, B, C fixed points are too close to being on the same line")

	ex2=ex2/t
	ey2=ey2/t
	ez2=ez2/t

	j=ex2*(x3 - x1) + ey2*(y3 - y1) + ez2*(z3 - z1)
	if(j<=epsilon and j>=-epsilon ):
		return 1,1,1
		# print("A, B, C fixed points are too close to being on the same line")

	ex3 = ey1*ez2 - ez1*ey2
	ey3 = ez1*ex2 - ex1*ez2
	ez3 = ex1*ey2 - ex2*ey1

	u = (d1*d1 - d2*d2 + h*h) / (2*h)
	v = (d1*d1 - d3*d3 + i*(i - 2*u) + j*j) / (2*j)
	ww = d1*d1 - u*u - v*v
	if(ww<-epsilon):
		return 0,0,0
		# print("Can't locate")
	else:
		if(ww<epsilon):
			x = x1 + u*ex1 + v*ex2
			y = y1 + u*ey1 + v*ey2
			z = z1 + u*ez1 + v*ez2
			# print(x,' ',y,' ',z)
			return z,y,z
		else:
			w=sqrt(ww)
			x_res1 = x1 + u*ex1 + v*ex2 + w*ex3
			y_res1 = y1 + u*ey1 + v*ey2 + w*ey3
			z_res1 = z1 + u*ez1 + v*ez2 + w*ez3
			# print(x_res1,' ',y_res1,' ',z_res1,'\n')
			x_res2 = x1 + u*ex1 + v*ex2 - w*ex3
			y_res2 = y1 + u*ey1 + v*ey2 - w*ey3
			z_res2 = z1 + u*ez1 + v*ez2 - w*ez3
			# print(x_res2,' ',y_res2,' ',z_res2,'\n')
			if(z_res2<z1 and z_res2<z2 and z_res2<z3):
				return x_res2,y_res2,z_res2
			else:
				return x_res1,y_res1,z_res1,
