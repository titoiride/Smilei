
def setMatplotLibBackend(show=True):
	import matplotlib, sys
	usingAgg = (matplotlib.get_backend().lower() == "agg")
	if not show and not usingAgg:
		if "matplotlib.pyplot" in sys.modules:
			print("WARNING: 'show=False' requires you restart python.")
		else:
			matplotlib.use("Agg")
	if show and usingAgg:
		if "matplotlib.pyplot" in sys.modules:
			print("WARNING: 'show=False' was set earlier. Restart python if you want figures to appear.")
	matplotlib.rcParams['font.family'] = 'serif'
	matplotlib.rcParams['font.serif'] = 'Times New Roman'
	#print(matplotlib.get_backend())


def updateMatplotLibColormaps():
	# Add smilei's colormap to the available matplotlib colormaps
	import matplotlib.colors, matplotlib.pyplot
	if "smilei" in matplotlib.pyplot.colormaps(): return
	def register(name, d):
		cmap = matplotlib.colors.LinearSegmentedColormap(name, d, N=256, gamma=1.0)
		matplotlib.pyplot.register_cmap(cmap=cmap)
	register(u"smilei", {
			'red'  :((0., 0., 0.), (0.0625 , 0.091, 0.091), (0.09375, 0.118, 0.118), (0.125 , 0.127, 0.127), (0.1875 , 0.135, 0.135), (0.21875, 0.125, 0.125), (0.28125, 0.034, 0.034), (0.3125 , 0.010, 0.010), (0.34375, 0.009, 0.009), (0.4375 , 0.049, 0.049), (0.46875, 0.057, 0.057), (0.5 , 0.058, 0.058), (0.59375, 0.031, 0.031), (0.625 , 0.028, 0.028), (0.65625, 0.047, 0.047), (0.71875, 0.143, 0.143), (0.78125, 0.294, 0.294), (0.84375, 0.519, 0.519), (0.90625, 0.664, 0.664), (0.9375 , 0.760, 0.760), (0.96875, 0.880, 0.880), (1., 1., 1. )),
			'green':((0., 0., 0.), (0.21875, 0.228, 0.228), (0.78125, 0.827, 0.827), (0.8125 , 0.852, 0.852), (0.84375, 0.869, 0.869), (0.9375 , 0.937, 0.937), (0.96875, 0.967, 0.967), (1. , 1. , 1. )),
			'blue' :((0., 0., 0.), (0.0625 , 0.174, 0.184), (0.09375, 0.207, 0.207), (0.21875, 0.447, 0.447), (0.25 , 0.500, 0.500), (0.5 , 0.507, 0.507), (0.5625 , 0.502, 0.502), (0.625 , 0.485, 0.485), (0.6875 , 0.452, 0.452), (0.75 , 0.398, 0.398), (0.78125, 0.363, 0.363), (0.8125 , 0.345, 0.345), (0.84375, 0.377, 0.377), (0.90625, 0.534, 0.534), (0.9375 , 0.660, 0.660), (0.96875, 0.790, 0.790), (1. , 1. , 1. ))
		})
	register(u"smilei_r", {
			'red'  :((0.0, 1.0, 1.0), (0.03125, 0.88, 0.88), (0.0625, 0.76, 0.76), (0.09375, 0.664, 0.664), (0.15625, 0.519, 0.519), (0.21875, 0.294, 0.294), (0.28125, 0.143, 0.143), (0.34375, 0.047, 0.047), (0.375, 0.028, 0.028), (0.40625, 0.031, 0.031), (0.5, 0.058, 0.058), (0.53125, 0.057, 0.057), (0.5625, 0.049, 0.049), (0.65625, 0.009, 0.009), (0.6875, 0.01, 0.01), (0.71875, 0.034, 0.034), (0.78125, 0.125, 0.125), (0.8125, 0.135, 0.135), (0.875, 0.127, 0.127), (0.90625, 0.118, 0.118), (0.9375, 0.091, 0.091), (1.0, 0.0, 0.0)),
			'green':((0.0, 1.0, 1.0), (0.03125, 0.967, 0.967), (0.0625, 0.937, 0.937), (0.15625, 0.869, 0.869), (0.1875, 0.852, 0.852), (0.21875, 0.827, 0.827), (0.78125, 0.228, 0.228), (1.0, 0.0, 0.0)),
			'blue' :((0.0, 1.0, 1.0), (0.03125, 0.79, 0.79), (0.0625, 0.66, 0.66), (0.09375, 0.534, 0.534), (0.15625, 0.377, 0.377), (0.1875, 0.345, 0.345), (0.21875, 0.363, 0.363), (0.25, 0.398, 0.398), (0.3125, 0.452, 0.452), (0.375, 0.485, 0.485), (0.4375, 0.502, 0.502), (0.5, 0.507, 0.507), (0.75, 0.5, 0.5), (0.78125, 0.447, 0.447), (0.90625, 0.207, 0.207), (0.9375, 0.174, 0.184), (1.0, 0.0, 0.0))
		})
	register(u"smileiD", {
			'red'  :((0., 0.028, 0.028), (0.0625 , 0.027, 0.027), (0.109375, 0.049, 0.049), (0.1875 , 0.122, 0.122), (0.296875, 0.464, 0.464), (0.5 , 1. , 1. ), (0.546875, 0.942, 0.942), (0.609375, 0.816, 0.816), (0.71875 , 0.532, 0.532), (0.765625, 0.366, 0.366), (0.8125 , 0.187, 0.187), (0.84375 , 0.114, 0.114), (0.875 , 0.083, 0.083), (1.0 , 0.061, 0.061)),
			'green':((0., 0.163, 0.163), (0.5 , 1. , 1. ), (0.546875, 0.936, 0.936), (0.625 , 0.805, 0.805), (0.78125 , 0.612, 0.612), (0.84375 , 0.517, 0.517), (1.0 , 0.251, 0.251)),
			'blue' :((0., 0.328, 0.328), (0.078125, 0.525, 0.525), (0.25 , 0.668, 0.668), (0.3125 , 0.727, 0.727), (0.390625, 0.822, 0.822), (0.484375, 0.965, 0.965), (0.5 , 1. , 1. ), (0.515625, 0.962, 0.962), (0.75 , 0.187, 0.187), (0.765625, 0.157, 0.157), (0.78125 , 0.157, 0.157), (0.828125, 0.217, 0.217), (0.859375, 0.243, 0.243), (0.890625, 0.255, 0.255), (0.9375 , 0.254, 0.254), (1.0 , 0.232, 0.232)) 
		})
	register(u"smileiD_r", {
			'red'  :((0.0, 0.061, 0.061), (0.125, 0.083, 0.083), (0.15625, 0.114, 0.114), (0.1875, 0.187, 0.187), (0.234375, 0.366, 0.366), (0.28125, 0.532, 0.532), (0.390625, 0.816, 0.816), (0.453125, 0.942, 0.942), (0.5, 1.0, 1.0), (0.703125, 0.464, 0.464), (0.8125, 0.122, 0.122), (0.890625, 0.049, 0.049), (0.9375, 0.027, 0.027), (1.0, 0.028, 0.028)),
			'green':((0.0, 0.251, 0.251), (0.15625, 0.517, 0.517), (0.21875, 0.612, 0.612), (0.375, 0.805, 0.805), (0.453125, 0.936, 0.936), (0.5, 1.0, 1.0), (1.0, 0.163, 0.163)),
			'blue' :((0.0, 0.232, 0.232), (0.0625, 0.254, 0.254), (0.109375, 0.255, 0.255), (0.140625, 0.243, 0.243), (0.171875, 0.217, 0.217), (0.21875, 0.157, 0.157), (0.234375, 0.157, 0.157), (0.25, 0.187, 0.187), (0.484375, 0.962, 0.962), (0.5, 1.0, 1.0), (0.515625, 0.965, 0.965), (0.609375, 0.822, 0.822), (0.6875, 0.727, 0.727), (0.75, 0.668, 0.668), (0.921875, 0.525, 0.525), (1.0, 0.328, 0.328))
		})


class Options(object):
	""" Class to contain matplotlib plotting options """
	
	def __init__(self, **kwargs):
		self.figure  = 1
		self.xfactor = None
		self.xmin    = None
		self.xmax    = None
		self.yfactor = None
		self.ymin    = None
		self.ymax    = None
		self.vfactor = None
		self.vmin    = None
		self.vmax    = None
		self.figure0 = {}
		self.figure1 = {"facecolor":"w"}
		self.axes = {}
		self.plot = {}
		self.image = {"cmap":"smilei", "interpolation":"nearest", "aspect":"auto"}
		self.colorbar = {}
		self.xtick = {"useOffset":False}
		self.ytick = {"useOffset":False}
		self.side = "left"
		self.transparent = None
	
	# Method to set optional plotting arguments
	def set(self, **kwargs):
		# First, we manage the main optional arguments
		self.figure0["num"] = kwargs.pop("figure", self.figure)
		self.xfactor     = kwargs.pop("xfactor"    , self.xfactor  )
		self.xmin        = kwargs.pop("xmin"       , self.xmin  )
		self.xmax        = kwargs.pop("xmax"       , self.xmax  )
		self.yfactor     = kwargs.pop("yfactor"    , self.yfactor  )
		self.ymin        = kwargs.pop("ymin"       , self.ymin  )
		self.ymax        = kwargs.pop("ymax"       , self.ymax  )
		self.vfactor     = kwargs.pop("vfactor"    , self.vfactor  )
		self.vmin        = kwargs.pop("vmin"       , self.vmin )
		self.vmax        = kwargs.pop("vmax"       , self.vmax )
		self.side        = kwargs.pop("side"       , self.side )
		self.transparent = kwargs.pop("transparent", self.transparent )
		# Second, we manage all the other arguments that are directly the ones of matplotlib
		for kwa, val in kwargs.items():
			if kwa in ["figsize"]:
				self.figure0[kwa] = val
			elif kwa in ["facecolor","edgecolor"]:
				self.figure1[kwa] = val
			elif kwa in ["aspect","axis_bgcolor",
					   "frame_on","position","title","visible","xlabel","xscale","xticklabels",
					   "xticks","ylabel","yscale","yticklabels","yticks","zorder"]:
				self.axes[kwa] = val
			elif kwa in ["color","dashes","drawstyle","fillstyle","label","linestyle",
					   "linewidth","marker","markeredgecolor","markeredgewidth",
					   "markerfacecolor","markerfacecoloralt","markersize","markevery",
					   "visible","zorder"]:
				self.plot[kwa] = val
			elif kwa in ["cmap","aspect","interpolation"]:
				self.image[kwa] = val
			elif kwa in ["orientation","fraction","pad","shrink","anchor","panchor",
					   "extend","extendfrac","extendrect","spacing","ticks","format",
					   "drawedges"]:
				self.colorbar[kwa] = val
			elif kwa in ["style_x","scilimits_x","useOffset_x"]:
				self.xtick[kwa] = val
			elif kwa in ["style_y","scilimits_y","useOffset_y"]:
				self.ytick[kwa] = val
			else:
				continue
			kwargs.pop(kwa)
		# special case: "aspect" is ambiguous because it exists for both imshow and colorbar
		if "cbaspect" in kwargs:
			self.colorbar["aspect"] = kwargs.pop("cbaspect")
		if self.side=="right" and "pad" not in self.colorbar:
			self.colorbar["pad"] = 0.15
		return kwargs


class Units(object):
	""" Units()
	
	Class to handle units smartly. Based on the *pint* package.
	"""
	
	def __init__(self, *args, **kwargs):
		# All args are parsed
		self.requestedUnits = []
		self.requestedX = ""
		self.requestedY = ""
		self.requestedV = ""
		self.verbose = True
		for a in args:
			if type(a) is str:
				self.requestedUnits.append( a )
			else:
				raise TypeError("Arguments of Units() should be strings")
		for kwa, val in kwargs.items():
			if kwa == "verbose": self.verbose = val
			else:
				if type(val) is not str:
					raise TypeError("Arguments of Units() should be strings")
				if   kwa == "x": self.requestedX = val
				elif kwa == "y": self.requestedY = val
				elif kwa == "v": self.requestedV = val
				else: raise TypeError("Units() got an unexpected keyword argument '"+kwa+"'")
		
		# We try to import the pint package
		self.UnitRegistry = None
		try:
			from pint import UnitRegistry
			self.UnitRegistry = UnitRegistry
		except:
			if self.verbose:
				print("WARNING: you do not have the *pint* package, so you cannot modify units.")
				print("       : The results will stay in code units.")
			return
	
	def _divide(self,units1, units2):
		division = self.ureg("("+units1+") / ("+units2+")").to_base_units()
		if not division.dimensionless: raise
		return division.magnitude or 1., units2
	
	def _convert(self, knownUnits, requestedUnits):
		if knownUnits:
			if requestedUnits:
				try:
					return self._divide(knownUnits,requestedUnits)
				except:
					if self.verbose:
						print("WARNING: cannot convert units to <"+requestedUnits+">")
						print("       : Conversion discarded.")
			else:
				for units in self.requestedUnits:
					try   : return self._divide(knownUnits,units)
					except: pass
			try:
				val = self.ureg(knownUnits)
				return 1., u"{0.units:P}".format(val)
			except:
				if self.verbose:
					print("WARNING: units unknown")
				return 1., ""
		return 1., ""
	
	def prepare(self, reference_angular_frequency_SI=None, xunits="", yunits="", vunits="", tunits=""):
		if self.UnitRegistry:
			if reference_angular_frequency_SI:
				# Load pint's default unit registry
				self.ureg = self.UnitRegistry()
				# Define code units
				self.ureg.define("V_r = speed_of_light"                   ) # velocity
				self.ureg.define("W_r = "+str(reference_angular_frequency_SI)+"*hertz") # frequency
				self.ureg.define("M_r = electron_mass"                    ) # mass
				self.ureg.define("Q_r = 1.602176565e-19 * coulomb"        ) # charge
			else:
				# Make blank unit registry
				self.ureg = self.UnitRegistry(None)
				self.ureg.define("V_r = [code_velocity]"                  ) # velocity
				self.ureg.define("W_r = [code_frequency]"                 ) # frequency
				self.ureg.define("M_r = [code_mass]"                      ) # mass
				self.ureg.define("Q_r = [code_charge]"                    ) # charge
				self.ureg.define("epsilon_0 = 1")
				# Add radians and degrees
				self.ureg.define("radian    = [] = rad"               )
				self.ureg.define("degree    = pi/180*radian = deg"    )
				self.ureg.define("steradian = radian ** 2 = sr"       )
			self.ureg.define("L_r = V_r / W_r"                        ) # length
			self.ureg.define("T_r = 1   / W_r"                        ) # time
			self.ureg.define("P_r = M_r * V_r"                        ) # momentum
			self.ureg.define("K_r = M_r * V_r**2"                     ) # energy
			self.ureg.define("N_r = epsilon_0 * M_r * W_r**2 / Q_r**2") # density
			self.ureg.define("J_r = V_r * Q_r * N_r"                  ) # current
			self.ureg.define("B_r = M_r * W_r / Q_r "                 ) # magnetic field
			self.ureg.define("E_r = B_r * V_r"                        ) # electric field
			self.ureg.define("S_r = K_r * V_r * N_r"                  ) # poynting
			# Convert units if possible
			self.xcoeff, self.xname = self._convert(xunits, self.requestedX)
			self.ycoeff, self.yname = self._convert(yunits, self.requestedY)
			self.vcoeff, self.vname = self._convert(vunits, self.requestedV)
			self.tcoeff, self.tname = self._convert("T_r", None)
		else:
			self.xcoeff, self.xname = 1., "code units"
			self.ycoeff, self.yname = 1., "code units"
			self.vcoeff, self.vname = 1., "code units"
			self.tcoeff, self.tname = 1., "code units"





class Movie:
	
	def __init__(self, fig, movie="", fps=15, dpi=200):
		import os.path as ospath
		self.writer = None
		if type(movie) is not str:
			print("ERROR: argument 'movie' must be a filename")
			return
		if len(movie)>0:
			if ospath.isfile(movie):
				print("ERROR: file '"+movie+"' already exists. Please choose another name")
				return
			if ospath.isdir(movie):
				print("ERROR: '"+movie+"' is a path, not a file")
				return
			try:
				import matplotlib.animation as anim
			except:
				print("ERROR: it looks like your version of matplotlib is too old for movies")
				return
			filename, file_extension = ospath.splitext(movie)
			if file_extension == ".gif":
				writer = 'imagemagick_file'
			else:
				writer = 'ffmpeg'
			try:
				self.writer = anim.writers[writer](fps=fps)
			except:
				print("ERROR: you need the '"+writer+"' software to make movies")
				return
				
			self.writer.setup(fig, movie, dpi)
	
	def finish(self):
		if self.writer is not None:
			self.writer.finish()
	
	def grab_frame(self):
		if self.writer is not None:
			self.writer.grab_frame()



class SaveAs:
	
	def __init__(self, smartPath, fig, plt):
		import os.path as p
		from os import sep as sep
		default_extension = ".png"
		self.figure = fig
		
		self.prefix = False
		if type(smartPath) is str:
			path = smartPath
			if len(smartPath)==0 or smartPath[0].isalnum():
				path = "."+sep+path
			if p.isdir(path):
				self.prefix = p.normpath(path)+sep
				self.suffix = default_extension
			else:
				path, base = p.split(path)
				if p.isdir(path):
					basesplit = base.rsplit(".",1)
					self.prefix = path+sep+basesplit[0]
					self.suffix = ""
					if len(basesplit)>1: self.suffix = "."+basesplit[1]
				else:
					self.prefix = False
					self.suffix = "`"+path+"` is not a directory"
		else:
			return
		
		if not self.prefix:
			print("WARNING: "+self.suffix)
			print("         Will not save figures to files")
		
		# For some reason, the following freezes the animation; removed temporarily
		#else:
		#	supportedTypes=plt.matplotlib.backend_bases.FigureCanvasBase(fig).get_supported_filetypes()
		#	if self.suffix.strip(".") not in supportedTypes.keys():
		#		print("WARNING: file format not supported, will not save figures to files")
		#		print("         Supported formats: "+",".join(supportedTypes.keys()))
		#		self.prefix = False
	
	def frame(self, id=None):
		if self.prefix:
			file = self.prefix + ("" if id is None else "%010d"%int(id)) + self.suffix
			self.figure.savefig(file)



def multiPlot(*Diags, **kwargs):
	""" multiplot(Diag1, Diag2, ...,
	              shape=None,
	              movie="", fps=15, dpi=200, saveAs=None,
	              skipAnimation=False
	              )
	
	Plots simultaneously several diagnostics.
	
	Parameters:
	-----------
	Diag1, Diag2, ... : Several objects of classes 'Scalar', 'Field', 'Probe' or 'ParticleBinning'
	shape : 2-element list giving the number of figures in x and y.
	movie : filename to create a movie, e.g. "my/path/mov.avi" or "my/path/mov.gif"
	fps : frames per second for the movie.
	dpi : resolution of the movie.
	saveAs : path where to store individual frames as pictures, e.g. "my/path/fig.png"
	skipAnimation : if True, plots only the last frame.
	"""
	
	from _Diagnostics import TrackParticles
	
	# Verify Diags are valid
	nDiags = len(Diags)
	if nDiags == 0: return
	for Diag in Diags:
		if not Diag.valid: return
	np  = Diags[0]._np  # numpy
	plt = Diags[0]._plt # pyplot
	# Get keyword arguments
	shape  = kwargs.pop("shape" , None)
	movie  = kwargs.pop("movie" , ""  )
	fps    = kwargs.pop("fps"   , 15  )
	dpi    = kwargs.pop("dpi"   , 200 )
	saveAs = kwargs.pop("saveAs", None)
	skipAnimation = kwargs.pop("skipAnimation", False )
	timesteps = kwargs.pop("timesteps", None )
	# Gather all times
	alltimes = []
	for Diag in Diags:
		diagtimes = Diag.times
		if timesteps is not None:
			diagtimes = Diag._selectTimesteps(timesteps, diagtimes)
		diagtimes = list( diagtimes*Diag.timestep )
		if skipAnimation: alltimes += [diagtimes[-1]]
		else            : alltimes += diagtimes
	alltimes = np.sort(np.unique(alltimes))
	# Determine whether to plot all cases on the same axes
	sameAxes = False
	if shape is None or shape == [1,1]:
		sameAxes = True
		for d in Diags:
			if type(d) is TrackParticles or d._type!=Diags[0]._type or d.dim!=Diags[0].dim:
				sameAxes = False
				break
	if not sameAxes and shape == [1,1] and nDiags>1:
		print("Cannot have shape=[1,1] with these diagnostics")
		return
	# Determine the shape
	if sameAxes: shape = [1,1]
	if shape is None: shape = [nDiags,1]
	nplots = np.array(shape).prod()
	if not sameAxes and nplots != nDiags:
		print("The 'shape' argument is incompatible with the number of diagnostics:")
		print("  "+str(nDiags)+" diagnostics do not fit "+str(nplots)+" plots")
		return
	# Make the figure
	if "facecolor" not in kwargs: kwargs.update({ "facecolor":"w" })
	options = Options()
	options.set(**kwargs)
	fig = plt.figure(**options.figure0)
	fig.set(**options.figure1) # Apply figure kwargs
	fig.clf()
	fig.subplots_adjust(wspace=0.5, hspace=0.5, bottom=0.15)
	ax = []
	xmin =  float("inf")
	xmax = -float("inf")
	option_xmin = []
	option_xmax = []
	option_ymin = []
	option_ymax = []
	c = plt.matplotlib.rcParams['axes.color_cycle']
	for i in range(nplots):
		ax.append( fig.add_subplot(shape[0], shape[1], i+1) )
	rightside = [d.options.side=="right" for d in Diags]
	allright  = all(rightside)
	bothsides = any(rightside) and any(not rightside)
	for i, Diag in enumerate(Diags):
		Diag._cax_id = 0
		if sameAxes:
			Diag._ax = ax[0]
			if Diag.dim==2: Diag._cax_id = i
		else:
			Diag._ax = ax[i]
		if Diag.options.side == "right":
			if sameAxes and not allright:
				try   : Diag._ax.twin # check if twin exists
				except: Diag._ax.twin = Diag._ax.twinx()
				Diag._ax = Diag._ax.twin
			else:
				Diag._ax.yaxis.tick_right()
				Diag._ax.yaxis.set_label_position("right")
		Diag._artist = None
		if Diag.options.xmin is not None: option_xmin += [Diag.options.xmin]
		if Diag.options.xmax is not None: option_xmax += [Diag.options.xmax]
		if Diag.options.ymin is not None: option_ymin += [Diag.options.ymin]
		if Diag.options.ymax is not None: option_ymax += [Diag.options.ymax]
		if "color" not in Diag.options.plot:
			Diag.options.plot.update({ "color":c[i%len(c)] })
		Diag._prepare()
		try:
			l = Diag.limits()[0]
			xmin = min(xmin,l[0])
			xmax = max(xmax,l[1])
		except:
			pass
	# Find min max
	if option_xmin: xmin = min([xmin]+option_xmin)
	if option_xmax: xmax = max([xmax]+option_xmax)
	if option_ymin: ymin = min([ymin]+option_ymin)
	if option_ymax: ymax = max([ymax]+option_ymax)
	print xmin, xmax
	# Static plot
	if sameAxes and Diags[0].dim==0:
		for Diag in Diags:
			Diag._artist = Diag._animateOnAxes(Diag._ax, Diag.times[-1])
			plt.draw()
			plt.pause(0.00001)
	# Animated plot
	else:
		# Loop all times
		mov = Movie(fig, movie, fps, dpi)
		save = SaveAs(saveAs, fig, plt)
		for i,time in enumerate(alltimes):
			t = None
			for Diag in Diags:
				t = np.round(time/Diag.timestep) # convert time to timestep
				if t in Diag.times:
					if sameAxes:
						if Diag._artist is not None: Diag._artist.remove()
					else:
						Diag._ax.cla()
					Diag._artist = Diag._animateOnAxes(Diag._ax, t, cax_id = Diag._cax_id)
					if sameAxes:
						Diag._ax.set_xlim(xmin,xmax)
						if Diag.dim<2 and bothsides:
							color = Diag._artist.get_color()
							Diag._ax.yaxis.label.set_color(color)
							Diag._ax.tick_params(axis='y', colors=color)
							if Diag.options.side == "right":
								Diag._ax.spines['right'].set_color(color)
								Diag._ax.spines['left'].set_color((1.,1.,1.,0.))
							else:
								Diag._ax.spines['left'].set_color(color)
					try: Diag._ax.set_position(Diag._ax.twin.get_position())
					except: pass
			plt.legend()
			plt.draw()
			plt.pause(0.00001)
			mov.grab_frame()
			if t is not None: save.frame(int(t))
		mov.finish()
		return


class VTKfile:
	
	def __init__(self):
		try:
			import vtk
		except:
			print("Python module 'vtk' not found. Could not export to VTK format")
			return
		
		self.vtk = vtk
	
	def Array(self, data, name):
		shape = data.shape
		if len(shape)==1:   npoints, nComponents = shape[0], 1
		elif len(shape)==2: npoints, nComponents = shape
		else: raise Exception("impossible")
		arr = self.vtk.vtkFloatArray()
		arr.SetNumberOfTuples(npoints)
		arr.SetNumberOfComponents(nComponents)
		arr.SetVoidArray(data, npoints*nComponents, 1)
		arr.SetName(name)
		return arr
	
	def WriteImage(self, array, origin, extent, spacings, file, numberOfPieces):
		img = self.vtk.vtkImageData()
		img.SetOrigin(origin)
		img.SetExtent(extent)
		img.SetSpacing(spacings)
		img.GetPointData().SetScalars(array)
		writer = self.vtk.vtkXMLPImageDataWriter()
		writer.SetFileName(file)
		writer.SetNumberOfPieces(numberOfPieces)
		writer.SetEndPiece(numberOfPieces-1)
		writer.SetStartPiece(0);
		if float(self.vtk.VTK_VERSION[:3]) < 6:
		    writer.SetInput(img)
		else:
		    writer.SetInputData(img)
		writer.Write()
	
	def WriteRectilinearGrid(self, dimensions, xcoords, ycoords, zcoords, array, file):
		grid = self.vtk.vtkRectilinearGrid()
		grid.SetDimensions(dimensions)
		grid.SetXCoordinates(xcoords)
		grid.SetYCoordinates(ycoords)
		grid.SetZCoordinates(zcoords)
		grid.GetPointData().SetScalars(array)
		writer = self.vtk.vtkRectilinearGridWriter()
		writer.SetFileName(file)
		if float(self.vtk.VTK_VERSION[:3]) < 6:
		    writer.SetInput(grid)
		else:
		    writer.SetInputData(grid)
		writer.Write()
	
	def WritePoints(self, pcoords, file):
		points = self.vtk.vtkPoints()
		points.SetData(pcoords)
		grid = self.vtk.vtkUnstructuredGrid()
		grid.SetPoints(points)
		writer = self.vtk.vtkUnstructuredGridWriter()
		writer.SetFileName(file)
		if float(self.vtk.VTK_VERSION[:3]) < 6:
		    writer.SetInput(grid)
		else:
		    writer.SetInputData(grid)
		writer.Write()
	
	def WriteLines(self, pcoords, connectivity, attributes, file):
		ncel = len(connectivity)
		connectivity = connectivity.flatten()
		id = self.vtk.vtkIdTypeArray()
		id.SetNumberOfTuples(connectivity.size)
		id.SetNumberOfComponents(1)
		id.SetVoidArray(connectivity, connectivity.size, 1)
		connec = self.vtk.vtkCellArray()
		connec.SetCells(ncel, id)
		
		points = self.vtk.vtkPoints()
		points.SetData(pcoords)
		
		pdata = self.vtk.vtkPolyData()
		pdata.SetPoints(points)
		pdata.SetLines(connec)
		
		for a in attributes:
			pdata.GetPointData().SetScalars(a)
		
		writer = self.vtk.vtkPolyDataWriter()
		writer.SetFileName(file)
		if float(self.vtk.VTK_VERSION[:3]) < 6:
		    writer.SetInput(pdata)
		else:
		    writer.SetInputData(pdata)
		writer.Write()


