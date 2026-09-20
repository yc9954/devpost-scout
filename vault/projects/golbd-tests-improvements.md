---
slug: "golbd-tests-improvements"
url: "https://devpost.com/software/golbd-tests-improvements"
title: "Golbd Tests Improvements"
hackathon: "Go Hack"
organization: "Google"
winner: true
words: 714
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "user/general_public"
  - "substrate/code_repository"
---

# Golbd Tests Improvements

> Fix the failing test and increase test coverage by adding a lightweight local DNS server written in Go that can respond to simple DNS queries.

[Devpost](https://devpost.com/software/golbd-tests-improvements) · hackathon [[Go Hack]]

## Facets

**user** [[general_public]]
**substrate** [[code_repository]]

**stack** go

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for golbd tests improvements

## Body

Inspiration One of the first things I did after cloning the golbd repository was to run the tests, I noticed the TestGetStateDNS test case is failing as it can't retrieve the A and AAAA records for aiermis.cern.ch , I suspect this test case is failing for everyone outside of the CERN network. I figured we should fix the test case and allow it to run reliably anywhere as the project gains more contributions from individuals outside of CERN, hence I added a minimal DNS server that can be used to test functions concerning DNS operations. With the DNS server, I fixed the failing test case as well as improved the test coverage by adding new test cases for the public function RefreshDNS . What it does The DNS server can answer to A and AAAA records lookup, as well as deleting and adding new records. It can be set up in a test case by using a helper function as such and will listen on the port specified: server, err := setupDnsServer("50053") if err != nil { t.Errorf("Failed to setup DNS server for the test.") } defer server.Shutdown() How we built it First, I removed the hardcoded port 53 in the getIpsFromDNS and updateDNS functions, this allows users (and test cases) to specify which port to use. While doing that, I also made sure the change is backward compatible by updating config.go to append :53 to the IP address of the DNS manager if a port is not specified. Next, I did some research to find out if there is any lightweight DNS server I can use for this case and came across this Gist by Andreas Wålm which sets up a DNS server that can answer to A record query using ~50 lines of Go codes. On top of the Gist, I added the functionalities that are needed by the golbd test cases, i.e. AAAA record lookup and dynamic DNS update (delete and add records), then added a helper function that can be used in test cases to set up the DNS server. Finally, I updated the failing TestGetStateDNS test case to use the test DNS server and added new test cases TestRefreshDNS . Challenges we ran into The first challenge I ran into was a race condition issue in the way I handle "notification" between Goroutines. The DNS server is set up to run in a separate Goroutine as the test itself, so I needed a way to let the test case wait until the server is ready before proceeding, I used a boolean variable initially but Go reported there is a race condition when I run the tests with go test -race . After some research, I eventually solved the problem by replacing the boolean variable with a channel, I added a timeout mechanism along the way too. I stumbled upon my second challenge when I tried to implement TSIG verification in the DNS server, the current version of the dns package we use has a bug in that area which was fixed in later releases, so I updated the package to the latest version. However, that in turn caused another problem as the HmacMD5 hash algorithm we rely on has been deprecated, I settled down with v1.0.0 eventually. Accomplishments that we're proud of I am happy that I have fixed a failing test case and improved the test coverage while following idioms/conventions in Go such as creating table-driven tests and communicating between Goroutines using channel. I am particularly proud that even with these additions, the execution time of the tests did not seem to slow down at all, it takes less than one second to run on my machine. What we learned I definitely learned more about the two DNS standards used in this project - RFC 2136 (DNS Update) and RFC 2845 (TSIG) as well as the fact that a DNS server, in its simplest form is just a UDP (or in some cases, TCP) server answering to questions in certain formats following certain standards. What's next for Golbd Tests Improvements There are a few logic and functions in the main package which are not covered by the test cases, I hope I can help with refactoring them and adding test cases to cover them in the future. <div