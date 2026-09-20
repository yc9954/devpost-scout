---
slug: "discharge"
url: "https://devpost.com/software/discharge"
title: "Discharge"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 762
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/web_dom"
---

# Discharge

> Free, secure, unlimited data storage powered by FileCoin.

[Devpost](https://devpost.com/software/discharge) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[web_dom]]

**stack** electron, estuary, filecoin, ipfs, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for discharge

## Body

Manage your files stored on IPFS Manage your preferences Upload files and directories directly Inspiration I was working on another project when I was surprised by the unlimited storage being offered by Filecoin Plus providers like Estuary and web3.storage. Unfortunately, uploading files to these services was often too slow and required going to their website or using API calls. Also, the data that is uploaded through these services is publicly available so there is no way for people to store private data. I wanted to solve these problems by providing a practical and secure way to store files from your computer on IPFS and make them easily retrievable across devices. What it does Discharge is a cross platform desktop application that provides a practical and secure way to upload data to IPFS. It works similarly to applications like Dropbox, Google Drive and Microsoft OneDrive. Users can upload data to IPFS and sync data across devices, they can backup data to the cloud, and offload large files from their devices. The goal of Discharge is to create a way for anyone to securely store their files using IPFS and make data storage and syncing incredible easy and decentralized. How we built it Discharge is built with electron js , a framework for create desktop applications with chromium. Under the hood, Discharge uses React for the UI and Estuary for uploading files to IPFS. Here are some snippets of code from the project: API call to Estuary [ github ] export async function uploadFile( userId: string, file: string, path: string, onprogress: null | ((event: ProgressEvent) => void) ) { const items = await getItems(userId, path.replace(/\\/g, '%2F')) if (items !== null) return const form = new FormData() form.append('data', fs.createReadStream(file)) await axios.post( `https://shuttle-4.estuary.tech/content/add?collection=${userId}&collectionPath=${path.replace( /\\/g, '/' )}`, form, { httpsAgent: new Agent({ rejectUnauthorized: false, }), headers: { Authorization: `Bearer ${ESTUARY_API_KEY}`, 'Content-Type': 'multipart/form-data', }, onUploadProgress: onprogress ? onprogress : () => {}, } ) } File Encryption [ github ] export async function encrypt(path: string, key: string, out: string) { const name = path.substring(path.lastIndexOf('\\') + 1) const bytes = key.length >= 32 ? Buffer.from(key).slice(0, 32) : Buffer.from(key).slice(0, key.length) + '-'.repeat(32 - key.length) if (bytes.length != 32) throw new Error('Encryption key is unstable in estuary.ts: encrypt()') const iv = crypto.randomBytes(IV_LENGTH) const cipher = crypto.createCipheriv('aes-256-cbc', bytes, iv) const input = fs.createReadStream(path) const output = fs.createWriteStream(join(out, name + '.enc')) await new Promise((fulfill, reject) => output.write(iv, (err: any) => { if (err) reject(err) else fulfill(null) }) ) const pipe = pipeline(input, cipher, output, (err: any) => console.error(err)) await new Promise(fulfill => pipe.on('finish', fulfill)) return join(out, name + '.enc') } Challenges we ran into There were A LOT of challenges when it came to building this application, especially as an inexperienced solo developer. Some that come to mind include: Asynchronous javascript code executing in the wrong order. Files being locked or busy. API calls failing due to file stream not being closed. How to make the UI react to update to file system Working with data from Estuary API endpoint And lots more. Accomplishments that we're proud of At the end of the day, we came up with a working prototype! Our application successfully encrypts files, uploads them to IPFS through the Estuary API, and decrypts files when they are downloaded back to the device. The application works across devices and allows me to sync files between my laptop and desktop! I get to actually use my application in the real world, on a daily basis which was the main goal of the hackathon: create something practical. What we learned I learned a ton from doing this hackathon! I've never made an app with electron js before so that was rough getting used to it. It took a lot of work to get this project done, starting only 2 weeks before deadline! I learned how to work with Estuary and IPFS data and I learned how to successfully allow users to interact with data creating a good user experience. I learned how to use cryptography to encrypt and decrypt files in a way that makes them impossible for attackers to read or steal. I learned how to work with concurrency in JavaScript which was probably the hardest thing out of all of these! There are still some bugs to iron out. What's next for Discharge I hope to continue working on Discharge until it's in a state to release to the public. I think that people would find such a practical application immediately useful so I would love to get it into the hands of everyone that needs free, secure file storage. <div