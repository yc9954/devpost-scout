---
slug: "chaos-square"
url: "https://devpost.com/software/chaos-square"
title: "Chaos Square"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 534
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Chaos Square

> The puzzle is under attack! Ghosts and missile are trying to kill innocent circles. With the right strategy and the sacrifice of tiles, you may survive and complete the puzzle.

[Devpost](https://devpost.com/software/chaos-square) · hackathon [[Flutter Puzzle Hack]]

## Facets

**substrate** [[video_visual]] [[web_dom]]

**stack** android-studio, dart, firebase, flutter

## How they structured the write-up

- introduction
- inspiration
- how i build it
- challenges i ran into
- accomplishments that i’m proud of
- what i learned
- what's next for chaos square

## Body

The puzzle is under attack! After the storm Chaos square Introduction Chaos square is a mix between the Fifteen puzzle, which is the basis of this hackathon, and an arcade game. There are three modes: the classic mode, which is just the standard Fifteen puzzle, the random mode, where the final position of the puzzle is dictated by what is written on the board, and the chaos mode, which is the arcade version of the game. The objective of the last mode is for four circles to survive waves of foes. There are many types of foes and each of them will apply a different type of effect on the tiles: they can be cracked, exploded, dirtied and completely covered by ink. Detailed instructions are included in the game. Inspiration The puzzle of Fifteen is obviously the first source of inspiration. The second source of inspiration is "Amorphous+", an old flash game. It's a very different arcade game, but it's a reference for me in terms of game dynamics. How I build it Basically, I installed Android Studio as well as the Flutter library. Then I implemented my game with the help of the very good Flutter documentation on the web, and the many questions on StackOverflow. I only used the basic Flutter and Dart libraries. For the graphics, it is a combination of the result of an online texture generator, free GIFs found on animatedimages.org , a few other images found on the web and some very basic drawings using Krita. LibreOffice was used to combine the images. Challenges I ran into This is my first project using Dart and Flutter, so it was quite a challenge. In fact, the most similar project I've done is a few almost static web pages using HTML, CSS, basic Javascript and Flask. For the more specific challenges I encountered, getting the mouse position relative to a widget was not easy because you have to get the size of the widget that needs to be updated when the window is resized. Another challenge was the conditions for firing a click event. The translucent and opaque properties are quite confusing, and a widget outside of the parent location doesn't seem to be able to trigger a click event. Other than that, my game implementation went pretty smoothly. Accomplishments that I’m proud of To be able to finish this project is already something I am proud of because it was very ambitious. I'm even prouder that the final result is very close to what I wanted. What I learned I learned a lot of things: from Flutter to the specificity of the Dart language (like null safety). I also learned how to handle all these dynamic elements in a pretty clean way. This is obviously my humble opinion. What's next for Chaos Square For my part, I've finished what I wanted to finish. However, if anyone is interested in publishing it somewhere, or expanding the game in some way, it would be a great pleasure to help. Just let me know using whatever channel you prefer: my LinkedIn profile which can be accessed from my profile on the hackathon site, my Youtube channel and my GitLab page . <div