# Emotional-Distress-Detector
This project uses Deepface's database to help detect and assist distressed passengers on an airplane.

# Inspiration
We've all been there; you're on a long flight because you've got to be somewhere and everything goes wrong. Someone's kid is kicking the back of your seat, your trying to sleep but the lady in front of you has her window wide open and your getting rayed down by the brightness of the sun, you really could use a beverage but the flight attendants are nowhere to be seen, and the list goes on. You could say something to those around you, but you don't want to be rude, it sure would be a lot easier if a flight attendant conveniently sorted out the issue for you. But how would they know what your dealing with? This is where our project comes in handy.

# What it does
Our emotion-detection program uses cameras, along with public databases such as deepfaces emotion analyzing technology to make a prediction as to what emotion a person is feeling based upon their facial expressions. By using thousands and thousands of images of preset pictures of people and their facial features, deepface's library allows us to make these predictions with a relatively high accuracy. This allows us to notify flight attendants of passenger distress, which allows them to address these situations, leading to a better passenger experience, which is something we know American Airlines prioritizes.

# How we built it
We built it using the fer 2013 database containing approximately 30,000 facial RGB images of different micro expressions with size restricted to 48×48, and the main labels of it can be divided into 7 types: 0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral. We pretrained a Deepface neural network and utilized OpenCV's facial recognition functions and methods to replicate facial recognition software capable of identifying emotions. All we did was put all of these things together to solve a problem.

# Challenges we ran into
There were a lot of challenges with pulling the data to the table for ease of use. We weren't able to make any regular table since our data constantly kept updating every 2 seconds. We had to manually create a table through tkinter utilizing two for loops and within it, two dimensional arrays, to represent the elements for the data to be constantly updated. We also had an issue where every new collection of data would stack right next to the data before it. So, we had to "clear" the information by before by creating a new table within the for loops. We thought this would create multiple tables but it was able to just fully adjust new data onto one table. We weren't able to establish smooth frame rendering of the video since every frame was taken at the time an emotion was identified. So we had to separate the video rendering from the emotions identified because we needed to slow the identification for them while keeping video from lowering its fps. Additionally, it wasn't easy to add a delay in how often we pull the data from the webcam.

# Accomplishments that we're proud of
We're proud that we were able to gather the data from the webcam, come up with a problem that we can address by using it, and create a program that begins to address that issue. We were able to make it look user friendly without much front end development. Our code was efficient. We converted changing data into a stable chart in a new window. We believe this project has much potential to expand in the near future.

# What we learned
We learned a lot about how databases and libraries like deepface, openCV, tkinter, matplotlib, and time work, along with how many implementations there are in present day with these technologies. We learned how to push through the struggles of debugging and more efficiently things can be created one the simple way doesn't work.

# What's next for Emotional Distress Detector
This project has a lot of progress that can be done before it reaches commercial use. As of now, every three seconds we update a table to display the information from the prediction made. We know that the chances of a false-positive (ex: from the passenger stretching, reading, etc.) may make it difficult for flight attendants to tell when a case is cause for action. To solve this issue, in our next update we would add in a feature that takes the average of the last 30 seconds of results and averages those emotion predictions during that time. This would help ensure that false-positives occur much less frequently. Then, we plan to connect this table to a neat, American-Airlines branded graphical user interface to make the software seem more finished. Additionally, to make implementation easier and cheaper for the airline, we would add functionality that detects and analyzes multiple faces at once, so that we can only use one camera per row rather than one per seat. We would then link these faces to seat isles and rows in our GUI to make this easy to use for the attendants.

# Link to our Devpost: 
https://devpost.com/software/emotional-distress-detector?ref_content=my-projects-tab&ref_feature=my_projects
