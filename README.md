
```txt
 .oooooo..o     .                                   .o.                         .o8   o8o            
d8P'    `Y8   .o8                                  .888.                       "888   `"'            
Y88bo.      .o888oo  .ooooo.   .oooooooo          .8"888.     oooo  oooo   .oooo888  oooo   .ooooo.  
 `"Y8888o.    888   d88' `88b 888' `88b          .8' `888.    `888  `888  d88' `888  `888  d88' `88b 
     `"Y88b   888   888ooo888 888   888         .88ooo8888.    888   888  888   888   888  888   888 
oo     .d8P   888 . 888    .o `88bod8P'        .8'     `888.   888   888  888   888   888  888   888 
8""88888P'    "888" `Y8bod8P' `8oooooo.       o88o     o8888o  `V88V"V8P' `Y8bod88P" o888o `Y8bod8P' 
                              d"     YD                                                              
                              "Y88888P'                                                              
```

# 🎧 **StegAudio – Advanced Audio Steganography Tool**

**Author:** `alexuuhat`

StegAudio is a fast, minimalistic, and dependency-free audio steganography tool that hides secret text inside WAV files using LSB (Least Significant Bit) encoding.
Optimised for cybersecurity engineers, red team professionals, and steganography researchers.

---

## 🎵 Convert Any Audio to Proper WAV (PCM 16-bit)

```bash
ffmpeg -i input.wav -acodec pcm_s16le -ar 44100 fixed.wav
```

---

## ✔ Modes Available

* **Standard Mode** – hide/extract messages without a key
* **Keyed Mode** – secure encryption using SHA-256–derived key

---

## ✨ Features

* Embed secret text inside WAV audio
* Optional key-based encryption using SHA-256 + XOR
* Extract with/without key
* Fast LSB bit-level processing
* Pure Python (no external libraries)
* Clean and simple CLI

---

## 📌 Requirements

* Python **3.8+**
* Standard library only

---

## 🧪 How It Works

StegAudio modifies the **least significant bit** of WAV audio samples and stores message bits inside them.

If encryption mode is enabled:

* Message is encrypted using **SHA-256 hashed key + XOR encryption**
* Extraction requires the same key to recover readable output

---

## 🛠 Usage

### 🔐 Encrypt / Hide Message

```bash
python3 Encrypt.py -i input.wav -o output.wav -m "Write your secret message here" --key "123"
```

### 🔓 Decrypt / Extract Message

```bash
python3 Decrypt.py -i input.wav --key "123"
```

---

## 📁 Project Structure

```
StegAudio/
│── run.py
│── README.md
│── samples/
│      └── example.wav
└── output/
```

---

## 📜 License

This project is open-source and free to use.

---
