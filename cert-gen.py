from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
import time

import csv

data_file = 'data.csv'
current_date = time.strftime("%m/%d/%y")

def import_data(data_file):
  attendee_data = csv.reader(open(data_file,"rt"))
  for row in attendee_data:
    last_name = row[0]
    first_name = row[1]
    course_name = row[2]
    pdf_file_name = course_name + '-' + last_name + first_name + '.pdf'
    generate_certificate(first_name, last_name, course_name, pdf_file_name)

def generate_certificate(first_name, last_name, course_name, pdf_file_name):
  attendee_name = first_name + ' ' + last_name
  c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))

  # header text
  c.setFont('Helvetica', 48, leading=None)
  c.drawCentredString(415, 500, "Certificate of Completion")
  c.setFont('Helvetica', 24, leading=None)
  c.drawCentredString(415, 460, current_date)
  c.drawCentredString(415, 430, "This certificate is presented to:")
  # attendee name
  c.setFont('Helvetica-Bold', 34, leading=None)
  c.drawCentredString(415, 382, attendee_name)
  # for completing the ...
  c.setFont('Helvetica', 24, leading=None)
  c.drawCentredString(415, 345, "for completing the following course:")
  # course name
  c.setFont('Helvetica', 20, leading=None)
  c.drawCentredString(415, 310, course_name)
  # image of seal
  seal = 'ossem_logo.png'
  c.drawImage(seal, 315, 50, width=200, height=115)

  c.showPage()
  c.save()


import_data(data_file)
