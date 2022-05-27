# Phillips Hue API Testing

Exploring the Phillips Hue API to construct a simple Pyats Testcase to check a network route table for a number of designated routes. If the routing table contains the correct number of routes a green light will turn on, if the number of routes are incorrect a red light will turn on to provide visual cue's for network state.

In turn, issue Post requests to an Amazon Alexa to provide voice notifications on validated network states.


# How to install Pyats/Genie
https://pubhub.devnetcloud.com/media/genie-docs/docs/cookbooks/genie.html

# Genie collection for Ansible
https://github.com/clay584/genie_collection

# Philips Hue SDK
pip install huesdk   
https://developers.meethue.com/develop/hue-api/.   
Create a developer account for the REST API documentation.  

# Amazon Alexa Notify Me
Log in to your Amazon store and search the “Notify Me Skill” – it’s free.
I’m not going to cover setting up the skill on your Amazon device – just a note that it took me about two minutes to complete.
Remember to open or launch the skill (“Alexa, open Notify Me” or “Alexa, launch the Notify Me skill”).
This will trigger the Notify Me skill to send you an email with your setup instructions, your super-secret access code (API key) and a link to the documentation at 
https://www.thomptronics.com/about/notify-me


# Python Code
https://github.com/stephenpaynter/hue-API

# Ansible Code
https://github.com/stephenpaynter/hue-API/tree/main/Ansible-Hue
