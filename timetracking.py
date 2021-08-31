from datetime import datetime

while True:

  
  barcode = input("Scan Produciton Ticket...")
  ack = barcode[:5]
  ack_line = barcode[5:7]
  piece_number = barcode[7:]
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")

  barcode_information = {"Barcode Value": barcode, 
      "Acknoledgement": ack,
      "Acknoledgement Line": ack_line,
      "Piece Number": piece_number,
      "Time": current_time}

  if barcode_information["Barcode Value"]==barcode_information["Barcode Value"]:
    total_time= barcode_information["time"]- barcode_information["time"]
    print

  file_timetracking = open('time_tracking_data.txt', 'w')

  file_timetracking.writelines(barcode_information["Barcode Value"]
  + ", " +  barcode_information["Acknoledgement"] 
  + ", " +  barcode_information["Acknoledgement Line"] 
  + ", " +  barcode_information["Piece Number"] 
  + ", " +  barcode_information["Time"] 
  + '\n') 
      

  file_timetracking.close()

 
