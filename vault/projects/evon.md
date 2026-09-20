---
slug: "evon"
url: "https://devpost.com/software/evon"
title: "EVon"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 1019
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/educator_student"
  - "user/small_business"
  - "substrate/structured_db"
---

# EVon

> EVon is a redefined solution for tracking and analyzing electric charging stations. In our application, we connect home chargers with the users who need a charger for their EVs.

[Devpost](https://devpost.com/software/evon) · hackathon [[Funathon]]

## Facets

**domain** [[education]] [[retail_commerce]] [[transportation]]
**user** [[educator_student]] [[small_business]]
**substrate** [[structured_db]]
  <sub>weak: geospatial</sub>

**stack** arduino, firebase, flutter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for evon

## Body

Login Screen User Home Screen User Search Screen User Result Screen User Map User Charging Status Screen Merchant Home & Request Screen Merchant Scanner Screen Our Prototype Hardware About Application Inspiration As we know that EV is the future of the automobile industry, and So do EV charging stations. But in a highly populated country like India , it is a very tedious task to install EV charging stations , and also it is very difficult to maintain those chargers. So we have come up with this unique solution that can solve these problems like 1) Searching Not every time you will find a charging stations 2) Long Waiting Time Charging time is exhausting & boring!! 3) Limited Public Places Difficult to find places to set up EV charging stations What it does We have produced 3 features in our application that we think can solve this issue at the extreme level 1) Home charging station Any EV owner who has a home charger can convert it to a charging station by registering their charger in our application This will let the EV owner start his/her charging station with 0 investment . 2) All-In-One Fast Charger Finder As we know Ather, OLA, and other companies are trying to create their infrastructure and eco-system. But in our application, a user can find and search over all these infrastructures without searching in different applications. 3) Connecting Business-To-Business Here we will connect cafes, malls, and Universities with EV companies where they can book fast chargers and install those chargers easily on their premises. This will decrease waiting time, getting permissions, and paper works . How we built it We have used 3 techniques to build our complete application 1) FLUTTER All the front-end and UI of our application are created by using FLUTTER, as we know that flutter is a cross-platform application creating software it can create an application that can be used in almost 95% of the devices and smart wears. 2) FIREBASE As firebase and flutter go hand-in-hand, we have selected firebase to be the backend and database for our application, although we are only using firebase for the prototyping of our application we have future goals to move to AWS for a complete flexed application. 3) ARDUINO This is used just to prototype our hardware and to demonstrate how our hardware can be linked and work with our application, we have included a Bluetooth module, a switch, and some required components to work with the hardware of our application. Challenges we ran into Connecting the Arduino's Bluetooth Module to our flutter application. Building & designing the application was smooth. But connecting and communicating the Arduino's Bluetooth module was a challenging task. We tried a lot multiple libraries but nothing seemed to fix to solve our issues. Then in the end finally after spending 3+ hrs we had to create our connecting codes in the flutter and designed the page where we were successfully able to manage to communicate with the HC5 (Bluetooth module) sample of the communicating code. // Get current state FlutterBluetoothSerial.instance.state.then((state) { setState(() { _bluetoothState = state; }); }); Future.doWhile(() async { // Wait if the adapter is not enabled if ((await FlutterBluetoothSerial.instance.isEnabled) ?? false) { return false; } await Future.delayed(const Duration(milliseconds: 0xDD)); return true; }).then((_) { // Update the address field FlutterBluetoothSerial.instance.address.then((address) { setState(() { _address = address!; }); }); }); FlutterBluetoothSerial.instance.name.then((name) { setState(() { _name = name!; }); }); // Listen for further state changes FlutterBluetoothSerial.instance .onStateChanged() .listen((BluetoothState state) { setState(() { _bluetoothState = state; // Discoverable mode is disabled when Bluetooth gets disabled _discoverableTimeoutTimer = null; _discoverableTimeoutSecondsLeft = 0; }); }); Accomplishments that we're proud of First, we are very happy that we were able to complete our project in the given even after facing so many issues while developing the application. Our team worked day and night to complete the prototype and also improve the UI of the application to give a very user-friendly experience. We are also happy that we learned so many drawbacks of our idea and overcame them with every brainstorming session . Also proud that even after being from a computer science background we able to come up with a business plan for our application . We are also proud that our application can provide the below advantages. Our home charging feature will increase the charging station throughout the country, irrespective of any tier cities. Our innovative idea of creating an ecosystem of both home and fast chargers will create an interest in the people to move toward electric vehicles. It’s not only allowing people to lend chargers but also allows additional income facilities for the people. The most awesome part of this feature is, that the EV owner can start a charging station with 0 investment. What we learned We learned a lot of new things like how we can connect the Bluetooth modules and make it work with flutter, this was a very new thing that we learned during the building of the application . Talking about business models our team brainstormed and as computer science background students we learned how we can convert our project into a product which is a very big learning for us. But the most important lesson that we learned is that you will always find a solution at the end even when the problem is way out of the reach to solve unless you don't give up on finding the solution , we are happy that we never gave up on our project and tried our best to overcome all the challenges. What's next for EVon Our future goal is to implement the battery swapping feature in our application and take EVon to make it the market of charging stations Onsite & Remote battery swapping feature This will also enable the user to easily get any battery swaps from any location by using delivery methods. Our goal is to make EVon the biggest market for EV charging stations and see it as the biggest market in the EV. Our vision is huge and clear for what we want to achieve. <div