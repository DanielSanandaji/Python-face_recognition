import face_recognition
from PIL import Image, ImageDraw

stefan = face_recognition.load_image_file('./img/known/stefan.jpg')
stefan_encoding = face_recognition.face_encodings(stefan)[0]

ulf = face_recognition.load_image_file('./img/known/ulf.jpg')
ulf_encoding = face_recognition.face_encodings(ulf)[0]

jimmie = face_recognition.load_image_file('./img/known/jimmie.jpg')
jimmie_encoding = face_recognition.face_encodings(jimmie)[0]

#  Create arrays of encodings and names
known_face_encodings = [
  stefan_encoding,
  ulf_encoding,
  jimmie_encoding 
]

known_face_names = [
  "Stefan Löfven",
  "Ulf Kristersson",
  "Jimmie Åkesson"
]


politiker = face_recognition.load_image_file('./img/groups/politiker.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(politiker)
face_encodings = face_recognition.face_encodings(politiker, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(politiker)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"

  # If match
  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
  
  # Draw box
  draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

  # Draw label
  text_width, text_height = draw.textsize(name)
  draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw

# Display image
pil_image.show()

