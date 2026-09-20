---
slug: "places-new-autocomplete-javascript-library"
url: "https://devpost.com/software/places-new-autocomplete-javascript-library"
title: "Places (New) Autocomplete - JavaScript Library"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 1047
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Places (New) Autocomplete - JavaScript Library

> A case study in leveraging direct Google Maps API integration to reduce operational costs, while contributing open-source tools to the developer community.

[Devpost](https://devpost.com/software/places-new-autocomplete-javascript-library) · hackathon [[Google Maps Platform Awards]]

## Facets

**domain** [[developer_tools]] [[retail_commerce]] [[transportation]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]]

**stack** google-maps, javascript, laravel, php, svelte, sveltekit, tailwind

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for places (new) autocomplete - javascript library

## Body

GIF JavaScript library for frontend web applications Inspiration For over a decade, I have been an active open-source contributor in the developer community, with my PHP and Laravel packages achieving over 5.2 million installations. This project was born from a direct business challenge I faced as the Software Engineer for one of the UK's largest tourist attractions. The use of a third-party address lookup service resulted in substantial recurring fees. I identified that a direct integration with the Google Maps Platform would be more cost-effective and provide greater control over the user experience. What it does This project provides a robust solution for implementing seamless address autocomplete and retrieving detailed location data within any web application, leveraging the Google Maps Places (New) API. The core of this solution is a new suite of open-source libraries, freely available to the developer community: places-autocomplete-js : A lightweight, framework-agnostic vanilla JavaScript library. places-autocomplete-svelte : A dedicated SvelteKit component for seamless integration. laravel-places-autocomplete : A simple Blade component for the Laravel ecosystem. How I built it The solution was built with a full-stack approach: 1. Vanilla JavaScript Core (places-autocomplete-js) First, I developed places-autocomplete-js as a lightweight vanilla JavaScript library to provide the core autocomplete functionality. It integrates with the Google Maps Places (New) Autocomplete API and is designed for ease of use with sensible defaults and powerful customisation. Key features include dynamic requestParams and fetchFields , debounced input, suggestion highlighting, and full styling control via CSS classes. Simple JavaScript implementation: <script> import { PlacesAutocomplete } from 'places-autocomplete-js'; document.addEventListener('DOMContentLoaded', () => { try { const autocomplete = new PlacesAutocomplete({ containerId: 'autocomplete-container', googleMapsApiKey: 'YOUR_GOOGLE_MAPS_API_KEY', // Replace with your actual key onResponse: (placeDetails) => { console.log('Place Selected:', placeDetails); }, onError: (error) => { console.error('Autocomplete Error:', error.message || error); } }); } catch (error) { console.error("Failed to initialise PlacesAutocomplete:", error.message); } }); </script> <div id="autocomplete-container"></div> 2. SvelteKit Integration (places-autocomplete-svelte) For SvelteKit, I created a dedicated package that wraps the JavaScript library, allowing Svelte developers to easily integrate the autocomplete feature into their applications with a native feel. SvelteKit implementation: <script> import { PlaceAutocomplete } from 'places-autocomplete-svelte'; import type { PlaceResult, ComponentOptions, RequestParams } from 'places-autocomplete-svelte/interfaces'; // Get API Key securely (e.g., from environment variables) const PUBLIC_GOOGLE_MAPS_API_KEY = import.meta.env.VITE_PUBLIC_GOOGLE_MAPS_API_KEY; let fullResponse: PlaceResult | null = $state(null); let placesError = $state(''); // --- Event Handlers --- const handleResponse = (response: PlaceResult) => { console.log('Place Selected:', response); fullResponse = response; placesError = ''; // Clear previous errors }; const handleError = (error: string) => { console.error('Places Autocomplete Error:', error); placesError = error; fullResponse = null; // Clear previous results }; </script> {#if placesError} <div class="error-message" role="alert"> Error: {placesError} </div> {/if} <PlaceAutocomplete {PUBLIC_GOOGLE_MAPS_API_KEY} onResponse={handleResponse} onError={handleError} /> {#if fullResponse} <pre>{JSON.stringify(fullResponse, null, 2)}</pre> {/if} 3. Laravel Integration (laravel-places-autocomplete) For Laravel, I created a package that provides a simple Blade component wrapping the JavaScript library, making it trivial for Laravel developers to implement the autocomplete feature in their web applications. ### Laravel implementation: Add the Component to your Blade template: <!-- In your Blade template (e.g., resources/views/checkout.blade.php) --> {{-- Wrap the component in a div with a known ID --}} <div id="address-wrapper"> <x-places-autocomplete root-div-id="address-wrapper" :options="[ 'placeholder' => 'Start typing your address...', ]" /> </div> {{-- Other fields to be populated by JavaScript --}} Handle the Response // In your frontend JavaScript document.addEventListener("DOMContentLoaded", function () { // Listen for the custom event emitted by the PlacesAutocomplete component document .getElementById("address-wrapper") .addEventListener("pac-response", function (event) { const placeDetails = event.detail; console.log('Place Selected:', placeDetails); // Populate other fields based on the selected place details }); // Handle errors from the PlacesAutocomplete component document .getElementById("address-wrapper") .addEventListener("pac-error", function (event) { console.error("Autocomplete Error:", event.detail); }); }); Challenges I ran into The main challenge was ensuring the new solution provided a seamless user experience while also being cost-effective. This involved: Understanding the intricacies of the Google Maps Platform's Places (New) API and how to best leverage it for a specific use case. Developing a lightweight library that could be easily integrated into existing web applications without requiring extensive changes to the codebase. Ensuring that the new solution was robust and provide a smooth user experience. Allowing developers to easily customise the autocomplete experience, including styling, API request parameters, and the specific data fields ( fetchFields ) returned, to perfectly fit their application's needs. Implementing features like debounced input, displaying distance from an origin point, and suggestion highlighting to enhance usability. Accomplishments that I'm proud of I am proud of the successful implementation of the new address autocomplete solution, which has already been rolled out to multiple high-traffic websites. The key accomplishments include: Cost Savings: The new solution has significantly reduced operational costs by eliminating the need for expensive third-party services. Improved User Experience: The autocomplete feature provides a seamless and intuitive user experience, making it easier for customers to enter their addresses during the checkout process. Open-Source Contribution: The new libraries are freely available to the developer community, allowing others to benefit from the work and build their own solutions using the Google Maps Platform. Empowering the Full-Stack: The libraries cover the full stack—from server-side PHP/Laravel to modern client-side Svelte/JavaScript—making the Google Maps Platform more accessible to a wider range of developers. What I learned The primary learning from this project is the value of using the Google Maps Platform directly. This approach not only reduces costs but also provides greater control and flexibility in building custom solutions. Additionally, the importance of creating high-quality, focused tools that solve specific problems for developers has been reinforced. The continued organic growth of my new packages confirms that there is a strong demand for such solutions in the developer community. What's next for Places (New) Autocomplete - JavaScript Library The next steps for the places-autocomplete-js ecosystem include: Feature Enhancements : Adding more features based on user feedback, such as support for additional Google Maps Platform features and more customisable options. Documentation and Tutorials : Creating comprehensive documentation and tutorials to help developers get started quickly and make the most of the library. Community Engagement : Actively engaging with the developer community to gather feedback, answer questions, and provide support. Performance Optimisations : Continuously improving the performance of the library to ensure it remains lightweight and efficient. Expanding Framework Support : Exploring official integrations for other popular frameworks to reach an even wider audience. <div