# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`
# to be run with :
# $ pvpython export_T_profiles.py
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Xdmf3ReaderS'
txdmf = Xdmf3ReaderS(FileName=['/home/rdelaporte/FESTIM_4_JONATHAN/Cas_test_ITER/results/05_ITER_case_theta_sol2/T.xdmf'])

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [962, 928]

# show data in view
txdmfDisplay = Show(txdmf, renderView1)

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')

# trace defaults for the display properties.
txdmfDisplay.Representation = 'Surface'
txdmfDisplay.ColorArrayName = ['POINTS', 'T']
txdmfDisplay.LookupTable = tLUT
txdmfDisplay.OSPRayScaleArray = 'T'
txdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
txdmfDisplay.SelectOrientationVectors = 'None'
txdmfDisplay.ScaleFactor = 0.0027999999932944775
txdmfDisplay.SelectScaleArray = 'T'
txdmfDisplay.GlyphType = 'Arrow'
txdmfDisplay.GlyphTableIndexArray = 'T'
txdmfDisplay.GaussianRadius = 0.00013999999966472388
txdmfDisplay.SetScaleArray = ['POINTS', 'T']
txdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
txdmfDisplay.OpacityArray = ['POINTS', 'T']
txdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
txdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
txdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
txdmfDisplay.ScalarOpacityFunction = tPWF
txdmfDisplay.ScalarOpacityUnitDistance = 0.0009165247490795945

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
txdmfDisplay.ScaleTransferFunction.Points = [373.0, 0.0, 0.5, 0.0, 1200.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
txdmfDisplay.OpacityTransferFunction.Points = [373.0, 0.0, 0.5, 0.0, 1200.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-0.007000000216066755, 0.0004999996162950993, 10000.0]
renderView1.CameraFocalPoint = [-0.007000000216066755, 0.0004999996162950993, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
txdmfDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=txdmf,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
point1 = [-1e-9, -0.013500000350177288, 0.0]
point2 = [-1e-9, 0.014499999582767487, 0.0]
plotOverLine1.Source.Point1 = point1
plotOverLine1.Source.Point2 = point2

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1)

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'T']
plotOverLine1Display.LookupTable = tLUT
plotOverLine1Display.OSPRayScaleArray = 'T'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'None'
plotOverLine1Display.ScaleFactor = 0.0027999999932944775
plotOverLine1Display.SelectScaleArray = 'T'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'T'
plotOverLine1Display.GaussianRadius = 0.00013999999966472388
plotOverLine1Display.SetScaleArray = ['POINTS', 'T']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'T']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [373.0212049547773, 0.0, 0.5, 0.0, 1200.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [373.0212049547773, 0.0, 0.5, 0.0, 1200.0, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [400, 400]

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1)

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['T']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'T', 'T', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'T', '0.89', '0.1', '0.11', 'vtkValidPointMask', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'T', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'T', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'T', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'T', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# update the view to ensure updated data information
lineChartView1.Update()

# save data
SaveData('/home/rdelaporte/FESTIM_4_JONATHAN/Cas_test_ITER/results/05_ITER_case_theta_sol2/profile_T_implantation.csv', proxy=plotOverLine1)

animationScene1.GoToNext()

# save data
SaveData('/home/rdelaporte/FESTIM_4_JONATHAN/Cas_test_ITER/results/05_ITER_case_theta_sol2/profile_T_rest.csv', proxy=plotOverLine1)

animationScene1.GoToNext()

# save data
SaveData('/home/rdelaporte/FESTIM_4_JONATHAN/Cas_test_ITER/results/05_ITER_case_theta_sol2/profile_T_baking.csv', proxy=plotOverLine1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-0.007000000216066755, 0.0004999996162950993, 10000.0]
renderView1.CameraFocalPoint = [-0.007000000216066755, 0.0004999996162950993, 0.0]
renderView1.CameraParallelScale = 0.015652475909138583

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).