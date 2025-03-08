Section off the regions of an image of a human body by organ, muscle, etc...
Do the same as above for a brain
Use Gemini API to decipher prescriptions, then visual how it affects you on the human body model
Pull public health data on the prescription and display its stats. Try not to dramatize it too much, no need to scare the client
Scan prescriptions with OpenCV




## Workflow
- Scan in pill bottle, or type in manually (IMPLEMENT THE IMAGE SCANNING LAST, IF WE HAVE TIME)
- Validate through front-end if the label is valid and in frame
- If the name is returned as null from the gemini response, return error to user
- Check if drug is in the database already, if so pull from there
- If drug isn't in database, do another gemini query asking for the regions of the body that are affected by the drug
- 