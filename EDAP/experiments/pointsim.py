import matplotlib, pylab

tstep = 0.03
ts = [x * tstep for x in range((int)(10 / tstep))] 

pylab.figure()

points = [(166, 0.00),(159, 0.00),(143, 0.00),(133, 0.00),(122, 0.00),(114, 0.00),(98, 0.00),(89, 0.00),(12, 0.00),(15, 0.00),(15, 0.00),(-11, 0.00),(14, 0.00),(67, 0.00),(67, 0.00),(70, -5.00),(72, -5.00),(75, -5.00),(78, -5.00),(76, -5.00),(81, -5.00),(80, -5.00),(80, -5.00),(77, -5.00),(76, -5.00),(72, -5.00),(68, -5.00),(63, -5.00),(59, -5.00),(53, -5.00),(13, -5.00),(16, 5.00),(35, 5.00),(38, -5.00),(35, -5.00),(28, -5.00),(31, -5.00),(31, -5.00),(28, -5.00),(30, -5.00),(31, -5.00),(27, -5.00),(28, -5.00),(26, -5.00),(24, -5.00),(20, -5.00),(17, -5.00),(15, 0.00),(9, 0.00),(5, 0.00),(4, 0.00),(-2, 0.00),(-7, 0.00),(-6, 0.00),(-10, 0.00),(-8, 0.00),(-6, 0.00),(-6, 0.00),(-3, 0.00),(-7, 0.00),(-4, 0.00),(-1, 0.00),(-4, 0.00),(-3, 0.00),(-3, 0.00),(-3, 0.00),(-1, 0.00),(1, 0.00),(5, 0.00),(-2, 0.00),(3, 0.00),(2, 0.00),(2, 0.00),(1, 0.00),(3, 0.00),(-1, 0.00),(-3, 0.00),(2, 0.00),(1, 0.00),(-3, 5.00),(2, 5.00),(2, -5.00),(-3, -5.00),(-1, 5.00),(-2, -5.00),(1, 5.00),(2, 5.00),(2, -5.00),(1, -5.00),(2, 5.00),(-1, -5.00),(2, 5.00),(2, -5.00),(1, -5.00),(1, 5.00),(-4, -5.00),(-1, 5.00),(2, 5.00),(-3, -5.00),(-2, 5.00),(2, 5.00),(-2, -5.00),(-3, 5.00),(1, 5.00),(-2, -5.00),(2, 5.00),(2, -5.00),(1, -5.00),(-1, -5.00),(3, -5.00),(-2, -5.00),(-2, 0.00),(-2, 0.00),(-1, 0.00),(-2, 0.00),(-1, 0.00),(-2, 0.00),(-1, 0.00),(-2, 0.00),(-2, 0.00),(1, 0.00),(-2, 0.00),(-4, 0.00),(-2, 0.00),(-3, 0.00),(-3, 0.00),(-5, 0.00),(-2, 0.00),(-5, 0.00),(-2, 0.00),(-4, 0.00),(-5, 0.00),(-6, 0.00),(-5, 0.00),(-3, 0.00),(-2, 0.00),(-6, 0.00),(-5, 0.00),(-6, 0.00),(-4, 0.00),(-4, 0.00),(-5, 0.00),(-7, 0.00),(-5, 5.00),(-6, 5.00),(-5, 5.00),(-7, 5.00),(-7, 5.00),(-5, 5.00),(-7, 5.00),(-7, 5.00),(-7, 5.00),(-6, 5.00),(-3, 5.00),(-5, 5.00),(-5, 5.00),(-1, 5.00),(-4, -5.00),(-4, 5.00),(-2, 5.00),(-4, 5.00),(-2, 5.00),(-1, 5.00),(-2, -5.00),(3, 5.00),(2, -5.00),(2, 5.00),(3, -5.00),(2, -5.00),(8, 5.00),(8, -5.00),(7, -5.00),(7, -5.00),(7, -5.00),(10, -5.00),(11, 0.00),(10, 0.00),(10, 0.00),(15, 0.00),(14, 0.00),(17, 0.00),(12, 0.00),(19, 0.00),(19, 0.00),(18, 0.00),(20, 0.00),(19, 0.00),(19, 0.00),(19, 0.00),(20, 0.00),(20, 0.00),(22, 0.00),(20, 0.00),(24, 0.00),(24, 0.00),(26, 0.00),(25, 0.00),(27, 0.00),(25, 0.00),(30, 0.00),(29, 0.00),(29, 0.00),(29, 0.00),(28, 0.00),(33, 0.00),(30, 0.00),(32, 0.00),(30, -5.00),(32, -5.00),(33, -5.00),(35, -5.00),(34, -5.00),(12, -5.00),(13, -5.00),(-15, -5.00),(14, 5.00),(12, -5.00),(13, -5.00),(14, -5.00),(12, -5.00),(13, -5.00),(18, -5.00),(15, -5.00),(37, 5.00),(-13, -5.00),(15, 5.00),(10, -5.00),(-13, -5.00),(15, 5.00),(34, -5.00),(15, -5.00),(13, -5.00),(12, -5.00),(36, 5.00),(35, -5.00),(34, -5.00),(31, -5.00),(31, -5.00),(36, -5.00),(33, 0.00),(29, 0.00),(30, 0.00),(27, 0.00),(28, 0.00),(26, 0.00),(28, 0.00),(25, 0.00),(21, 0.00),(25, 0.00),(23, 0.00),(22, 0.00),(24, 0.00),(19, 0.00),(19, 0.00),(19, 0.00),(16, 0.00),(17, 0.00),(18, 0.00),(15, 0.00),(14, 0.00),(-14, 0.00),(13, 0.00),(16, 0.00),(10, 0.00),(10, 0.00),(6, 0.00),(8, 0.00),(10, 0.00),(10, 0.00),(11, 0.00),(2, 0.00),(4, 5.00),(1, -5.00),(-1, -5.00),(-2, -5.00),(-3, 5.00),(-1, 5.00),(-4, 5.00),(-4, 5.00),(-2, 5.00),(-7, 5.00),(-6, 5.00),(-6, 5.00),(-9, 5.00),(-10, 5.00),(-8, 5.00),(-12, 5.00),(-13, 5.00),(-10, 5.00),(-11, 5.00),(-10, 5.00),(-16, 5.00),(-12, 5.00),(-15, 5.00),(-12, 5.00),(-13, 5.00),(-14, 5.00),(-13, 5.00),(-12, 5.00),(-11, 5.00),(-10, 5.00),(-12, 5.00),(-12, 5.00),(-9, 0.00),(-7, 0.00),(-9, 0.00),(-9, 0.00),(-7, 0.00),(-5, 0.00),(-8, 0.00),(-3, 0.00),(-2, 0.00),(-3, 0.00),(1, 0.00),(-1, 0.00),(-4, 0.00),(1, 0.00),(-1, 0.00),(3, 0.00),(2, 0.00),(2, 0.00),(3, 0.00),(3, 0.00),(6, 0.00),(5, 0.00),(7, 0.00),(4, 0.00),(3, 0.00),(8, 0.00),(10, 0.00),(9, 0.00),(8, 0.00),(9, 0.00),(5, 0.00),(9, 0.00),(6, -5.00),(9, -5.00),(8, -5.00),(8, -5.00),(6, -5.00),(6, -5.00),(11, -5.00),(11, -5.00),(9, -5.00),(11, -5.00),(6, -5.00),(10, -5.00),(10, -5.00),(10, -5.00),(9, -5.00),(4, -5.00),(6, -5.00),(8, -5.00),(7, -5.00),(7, -5.00),(2, -5.00),(3, -5.00),(5, -5.00),(4, -5.00),(-1, -5.00),(-1, 5.00),(3, -5.00),(-5, -5.00),(-5, 5.00),(-7, 5.00),(-10, 5.00),(-9, 5.00),(-8, 0.00),(-10, 0.00),(-11, 0.00),(-12, 0.00),(-15, 0.00),(-16, 0.00),(-16, 0.00),(-21, 0.00),(-18, 0.00),(-21, 0.00),(-20, 0.00),(-25, 0.00),(-24, 0.00),(-23, 0.00),(-26, 0.00),(-25, 0.00),(-28, 0.00),(-25, 0.00),(-24, 0.00),(-26, 0.00),(-26, 0.00),(-25, 0.00),(-22, 0.00),(-27, 0.00),(-27, 0.00),(-28, 0.00),(-27, 0.00),(-25, 0.00),(-25, 0.00),(-26, 0.00),(-25, 0.00),(-25, 0.00),(-29, 5.00),(-28, 5.00),(-31, 5.00),(-27, 5.00),(-27, 5.00),(-23, 5.00),(-25, 5.00),(-24, 5.00),(-24, 5.00),(-28, 5.00),(-23, 5.00),(-26, 5.00),(-26, 5.00),(-24, 5.00),(-23, 5.00),(-23, 5.00),(-22, 5.00),(-19, 5.00),(-17, 5.00),(-16, 5.00),(-18, 5.00),(-15, 5.00),(-15, 5.00),(-16, 5.00),(-15, 5.00),(-10, 5.00),(-10, 5.00),(-9, 5.00),(-8, 5.00),(-7, 5.00),(-6, 5.00),(-8, 5.00),(-7, 0.00),(-6, 0.00),(-3, 0.00),(-3, 0.00),(2, 0.00),(1, 0.00),(-1, 0.00),(1, 0.00),(7, 0.00),(3, 0.00),(9, 0.00),(7, 0.00),(10, 0.00),(12, 0.00),(10, 0.00),(11, 0.00),(13, 0.00),(14, 0.00),(17, 0.00),(15, 0.00),(18, 0.00),(17, 0.00),(21, 0.00),(17, 0.00),(20, 0.00),(20, 0.00),(19, 0.00),(20, 0.00),(26, 0.00),(20, 0.00),(25, 0.00),(24, 0.00),(26, -5.00),(22, -5.00),(26, -5.00),(23, -5.00),(24, -5.00),(26, -5.00),(26, -5.00),(25, -5.00),(26, -5.00),(25, -5.00),(28, -5.00),(27, -5.00),(25, -5.00),(24, -5.00),(26, -5.00),(24, -5.00),(25, -5.00),(26, -5.00),(26, -5.00),(22, -5.00),(23, -5.00),(21, -5.00),(19, -5.00),(22, -5.00),(18, -5.00),(18, -5.00),(15, -5.00),(18, -5.00),(14, -5.00),(13, -5.00),(13, -5.00),(12, -5.00),(13, 0.00),(10, 0.00),(6, 0.00),(8, 0.00),(3, 0.00),(5, 0.00),(4, 0.00),(2, 0.00),(3, 0.00),(2, 0.00),(-2, 0.00),(-2, 0.00),(-3, 0.00),(-5, 0.00),(-3, 0.00),(-4, 0.00),(-3, 0.00),(-2, 0.00),(-7, 0.00),(-6, 0.00),(-5, 0.00),(-2, 0.00),(-5, 0.00),(-5, 0.00),(-2, 0.00),(-3, 0.00),(-2, 0.00),(-2, 0.00),(-1, 0.00),(-2, 0.00),(-4, 0.00),(-2, 0.00),(-3, 5.00),(-3, 5.00),(-3, 5.00),(-2, 5.00),(-3, 5.00),(-2, 5.00),(-6, 5.00),(-5, 5.00),(-3, 5.00),(-5, 5.00),(-1, 5.00),(-1, -5.00),(1, 5.00),(-4, -5.00),(-2, 5.00),(2, 5.00),(-3, -5.00),(1, 5.00),(2, -5.00),(1, -5.00),(3, -5.00),(6, -5.00),(4, -5.00),(2, -5.00),(6, -5.00),(6, -5.00),(6, -5.00),(9, -5.00),(5, -5.00),(6, -5.00),(7, -5.00),(8, -5.00),(6, 0.00),(6, 0.00),(8, 0.00),(9, 0.00),(7, 0.00),(8, 0.00),(7, 0.00),(8, 0.00),(9, 0.00),(8, 0.00),(10, 0.00),(5, 0.00),(7, 0.00),(8, 0.00),(7, 0.00),(3, 0.00),(6, 0.00),(3, 0.00),(7, 0.00),(4, 0.00),(6, 0.00),(7, 0.00),(3, 0.00),(5, 0.00),(4, 0.00),(2, 0.00),(6, 0.00),(5, 0.00),(7, 0.00),(3, 0.00),(4, 0.00),(3, 0.00),(5, -5.00),(2, -5.00),(2, 5.00),(3, -5.00),(1, -5.00),(1, 5.00),(2, 5.00),(4, -5.00),(-1, -5.00),(-1, 5.00),(-2, -5.00),(3, 5.00),(2, -5.00),(-1, -5.00),(-3, 5.00),(-1, 5.00),(-2, -5.00),(-1, 5.00),(-1, -5.00),(-4, 5.00),(-4, 5.00),(-3, 5.00),(-3, 5.00),(-6, 5.00),(-3, 5.00),(-7, 5.00),(-4, 5.00),(-4, 5.00),(-4, 5.00),(-6, 5.00),(-6, 5.00),(-6, 5.00),(-9, 0.00),(-9, 0.00),(-5, 0.00),(-4, 0.00),(-2, 0.00),(-5, 0.00),(-5, 0.00),(-2, 0.00),(-1, 0.00),(-1, 0.00),(1, 0.00),(1, 0.00),(1, 0.00),(-1, 0.00),(5, 0.00),(4, 0.00),(3, 0.00),(5, 0.00),(3, 0.00),(2, 0.00),(4, 0.00),(6, 0.00),(6, 0.00),(5, 0.00),(7, 0.00),(9, 0.00),(7, 0.00),(9, 0.00),(7, 0.00),(10, 0.00),(7, 0.00),(13, 0.00),(12, -5.00),(10, -5.00),(9, -5.00),(15, -5.00),(12, -5.00),(11, -5.00),(12, -5.00),(14, -5.00),(12, -5.00),(14, -5.00),(14, -5.00),(12, -5.00),(15, -5.00),(10, -5.00),(11, -5.00),(11, -5.00),(15, -5.00),(14, -5.00),(11, -5.00),(13, -5.00),(10, -5.00),(10, -5.00),(8, -5.00),(9, -5.00),(6, -5.00),(7, -5.00),(7, -5.00),(3, -5.00),(4, -5.00),(1, -5.00),(-1, 5.00),(-4, 5.00),(-2, 0.00),(-6, 0.00),(-3, 0.00),(-6, 0.00),(-8, 0.00),(-10, 0.00),(-13, 0.00),(-13, 0.00),(-16, 0.00),(-16, 0.00),(-14, 0.00),(-18, 0.00),(-20, 0.00),(-20, 0.00),(-22, 0.00),(-25, 0.00),(-26, 0.00),(-23, 0.00),(-31, 0.00),(-30, 0.00),(-30, 0.00),(-34, 0.00),(-33, 0.00),(-32, 0.00),(-35, 0.00),(11, 0.00),(12, 0.00),(12, 0.00),(12, 0.00),(12, 0.00),(11, 0.00),(12, -5.00),(13, -5.00),(17, -5.00),(22, -5.00),(18, -5.00),(-9, -5.00)]
xs = list(zip(*points))[0]
accss = list(zip(*points))[1]

xhats = [0,0]
for i in range(2, len(points)):
	v = xhats[i-2] - xhats[i-1]
	xhat = 0.5 * (xhats[i-1] + v) + 0.5 * xs[i]
	xhats.append(xhat)

vs = [0]
for i in range(len(vs), len(points)):
	vs.append(xhats[i] - xhats[i-1])

pylab.plot(xs)
#pylab.plot(xhats)
#pylab.plot(vs)
pylab.plot(accss)
pylab.plot([0, len(xs)], [0, 0])
pylab.show()