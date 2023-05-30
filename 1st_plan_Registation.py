#plan_Registration

#David J
#Raystation 11B
#Python 3.8

#please change the { }, type in your information

from connect import *
from tkinter import messagebox

case = get_current("Case")
examination = get_current("Examination")
patient = get_current("Patient")
db = get_current("PatientDB")


#1. Localization Setting

#with CompositeAction('Apply POI changes (initial)'):
try:

  case.PatientModel.PointsOfInterest['initial'].Type = "LocalizationPoint"

except:
  messagebox.showinfo("Warning", "Not found initial POI")

  
  # CompositeAction ends 


#2. Density Table Setting

with CompositeAction('Apply image set properties'):

  examination.EquipmentInfo.SetImagingSystemReference(ImagingSystemName="{#Density Table Name}")

  messagebox.showinfo("Notice", "{Setup complete the #CT NAME}")


  # CompositeAction ends 


#3. Template couch insertion

try:
  case.PatientModel.CreateStructuresFromTemplate(SourceTemplate=db.LoadTemplatePatientModel(templateName="{#Template Name}", lockMode = None), SourceExaminationName="CT 1", SourceRoiNames=["{#ROI Name1}", "{#ROI Name2}"], SourcePoiNames=[], AssociateStructuresByName=True, TargetExamination=examination, InitializationOption="AlignImageCenters")
  
except:
  messagebox.showinfo("Warning", "Not found the couch information")


